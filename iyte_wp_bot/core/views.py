from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.db.models import Q

from core.utils.helpers import interactive_button_text, interactive_list_text
from core.utils.messaging import (
    send_whatsapp_text,
    send_button_message,
    send_list_message,
)
from core.models import Messages, populate_messages
from general import saatleri_guncelle
from bus.utils import get_schedule_with_busNo, get_schedule_with_from_to
from menu.utils import get_menu, add_like_to_menu, add_disslike_to_menu
FUNCTION_MAP = {
    11 : (get_menu, {"when": "today"}),
    12: (get_menu, {"when": "tomorrow"}),

    # 11: (add_like_to_menu, {}),
    # 12: (add_disslike_to_menu, {}),
    21: (get_schedule_with_from_to, {"from_station": "İYTE", "to_station": "heryer"}),
    22: (get_schedule_with_from_to, {"from_station": "İYTE", "to_station": "İzmir"}),
    23: (get_schedule_with_from_to, {"from_station": "İYTE", "to_station": "Urla"}),
    24: (get_schedule_with_from_to, {"from_station": "İYTE", "to_station": "Gulbahce"}),
    25: (get_schedule_with_from_to, {"from_station": "Urla", "to_station": "Çeşme"}),

    31: (get_schedule_with_from_to, {"from_station": "heryer", "to_station": "İYTE"}),
    32: (get_schedule_with_from_to, {"from_station": "İzmir", "to_station": "İYTE"}),
    33: (get_schedule_with_from_to, {"from_station": "Urla", "to_station": "İYTE"}),
    34: (get_schedule_with_from_to, {"from_station": "Gulbahce", "to_station": "İYTE"}),
    35: (get_schedule_with_from_to, {"from_station": "Çeşme", "to_station": "Urla"}),
    
    882: (get_schedule_with_busNo, {"bus_no": "882"}),
    883: (get_schedule_with_busNo, {"bus_no": "883"}),
    981: (get_schedule_with_busNo, {"bus_no": "981"}),
    982: (get_schedule_with_busNo, {"bus_no": "982"}),
    760: (get_schedule_with_busNo, {"bus_no": "760"}),
    761: (get_schedule_with_busNo, {"bus_no": "761"}),
    999: (get_schedule_with_busNo, {"bus_no": "999"}),
}

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")
def run_function_for_id(id):
    item = FUNCTION_MAP.get(id)
    if not item:
        return "None"
    func, kwargs = item
    return func(**kwargs)
@csrf_exempt
def webhook(request):

    if request.method == "GET":
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        return HttpResponse("Verification token mismatch", status=403)

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            messages = data['entry'][0]['changes'][0]['value'].get('messages', [])
            if not messages:
                return JsonResponse({"status": "no message"})

            msg = messages[0]
            wa_id = msg['from']

            # Varsayılan olarak incoming_code ve incoming_text boş
            incoming_text = ''
            incoming_code = ''

            # 1. Eğer text mesajı geldiyse
            if msg.get('type') == 'text':
                incoming_text = msg.get('text', {}).get('body', '').strip().lower()
                incoming_code = incoming_text.replace(" ", "").replace("-", "")

            # 2. Eğer butona basıldıysa
            elif msg.get('type') == 'interactive':
                interactive = msg.get('interactive', {})
                if interactive.get('type') == 'button_reply':
                    button_reply = interactive.get('button_reply', {})
                    incoming_code = button_reply.get('id', '').strip()
                    incoming_text = button_reply.get('title', '').strip().lower()
                elif interactive.get('type') == 'list_reply':
                    # Eğer ileride liste ile çalışacaksan burada da ayrıştırabilirsin
                    list_reply = interactive.get('list_reply', {})
                    incoming_code = list_reply.get('id', '').strip()
                    incoming_text = list_reply.get('title', '').strip().lower()
            

            # Nokta ile ilk menü
            if incoming_text in ["."]:
                text = "Sana yardımcı olabileceklerim şunlar:"
                messages_qs_menu = Messages.objects.filter(message_id__gt=10, message_id__lt=20)
                messages_qs_ulasim_iyteden = Messages.objects.filter(
                    Q(message_id=2) | Q(message_id__gt=21, message_id__lt=25)
                )

                # İYTEye Ulaşım: id=3 olan mesaj + 31-35 arası mesajlar
                messages_qs_ulasim_iyteye = Messages.objects.filter(
                    Q(message_id=3) | Q(message_id__gt=31, message_id__lt=35)
                )
                messages_dict = {"Menü": messages_qs_menu,
                                 "İYTEden Ulaşım": messages_qs_ulasim_iyteden,
                                 "İYTEye Ulaşım": messages_qs_ulasim_iyteye}
                
                interactive_data = interactive_list_text(body_text=text, 
                                                         categorized_messages=messages_dict,
                                                        header_text="İYTE Asistanı",
                                                         footer_text="Lütfen bir madde seçin.")
                send_list_message(wa_id, interactive_data=interactive_data)
                return JsonResponse({"status": "message sent"})
            if incoming_text =="update":
                populate_messages()
                saatleri_guncelle()
                
            # Kod/id gelen cevaplar (buton ID'si ya da yazı olarak sayı gelirse)
            if incoming_code.isdigit():
                message_id = int(incoming_code)
                print(f"Message ID: {message_id}")
                text = run_function_for_id(message_id)
                print(f"Function result: {text}")
                messages_sub = Messages.objects.filter(message_id__gt=message_id*10, message_id__lt=message_id*10+10)
                print(f"Sub-messages count: {messages_sub.count()}")
                if messages_sub.exists() and 0 < messages_sub.count() < 4:
                    interactive_data = interactive_button_text(text, messages_sub)
                    send_button_message(wa_id, interactive_data=interactive_data)
                elif messages_sub.exists() and messages_sub.count() >= 4:
                    if message_id == 2:
                        text = "*İYTE'den* ulaşım için lütfen bir yer seçin:"
                        messages_dict = {"İYTE'ye Ulaşım": messages_sub}
                        interactive_data = interactive_list_text(body_text=text, 
                                                                 categorized_messages=messages_dict,
                                                                header_text="İYTE Asistanı",
                                                                 footer_text="Lütfen bir madde seçin.")
                        send_list_message(wa_id, interactive_data=interactive_data)
                        
                    elif message_id ==3:
                        text = "*İYTE'ye* ulaşım için lütfen bir yer seçin:"
                        messages_dict = {"İYTE'den Ulaşım": messages_sub}
                        interactive_data = interactive_list_text(body_text=text, 
                                                                 categorized_messages=messages_dict,
                                                                 header_text="İYTE Asistanı",
                                                                 footer_text="Lütfen bir madde seçin.")
                        send_list_message(wa_id, interactive_data=interactive_data)
                        
                else:
                    send_whatsapp_text(wa_id, text)
                return JsonResponse({"status": "message processed"})
            
            # Diğer durumlar
            return JsonResponse({"status": "message processed"})

        except Exception as e:
            print("Error processing message:", str(e))
            return JsonResponse({"error": str(e)})

    return JsonResponse({"status": "Invalid method"})
