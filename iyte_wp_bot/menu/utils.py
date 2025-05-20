from .models import Menu, MenuItems
import datetime

MENU_TYPES = (
    ('GridView1' 'Günlük Menü'),
    ('GridViewGltensiz', 'Glutensiz Menü'),
    ('GridViewVegan', 'Vegan Menü'),
    ('GridViewVej', 'Vejetaryen Menü'),
)
MENU_TYPES_DICT = {
    'GridView1':'Günlük Menü'   ,
    'GridViewGltensiz':'Glutensiz Menü',
    'GridViewVegan':'Vegan Menü',
    'GridViewVej':'Vejetaryen Menü',
}

def format_menu(date,menu, menu_items):
    lines = []
    menu_list =[]
    lines.append(f"   *{date.strftime('%d %B %Y')}*")
    for item in menu_items:
        if item.menu_type not in menu_list:
            menu_list.append(item.menu_type)
            lines.append(f"🍽️ *{item.menu_type}* 🍽️")
        lines.append(f"_{item.item_name}_ ➔ *{item.calorie}* kcal")
    
    return "\n".join(lines)

def get_menu(when):
    today = datetime.date.today()
    menu = None
    menu_items = None
    date = None
    if when == "today":
        date = datetime.date.today()
        menu = Menu.objects.filter(date=today).first()
        menu_items = MenuItems.objects.filter(menu = menu)        
    elif when == "tomorrow":
        date = datetime.date.today() + datetime.timedelta(days=1)
        menu = Menu.objects.filter(date=today + datetime.timedelta(days=1)).first()
        menu_items = MenuItems.objects.filter(menu = menu)
    if menu and menu_items:
        result = format_menu(date,menu, menu_items)
        print(result)
        return result
    return "Güne ait menü bulunamadı."    
    

def add_like_to_menu(menu_id):
    try:
        Menu.objects.get(id=menu_id).add_like()
        return "Değerlendirmeniz menüye eklendi."       
    except Menu.DoesNotExist:
        return "Değerlendirme yapılamadı. Menü bulunamadı."
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"

def add_disslike_to_menu(menu_id):

    try:
        Menu.objects.get(id=menu_id).add_dislike()
        return "Değerlendirmeniz menüye eklendi."
    except Menu.DoesNotExist:
        return "Değerlendirme yapılamadı. Menü bulunamadı."
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"

def add_monthly_menu():
    with open ("2025-05.txt", "r", encoding="utf-8") as f:
        data_list = eval(f.read())

    for date,data in data_list:
        print(date)
        menu_obj, created = Menu.objects.get_or_create(
            date=date,
            defaults={'is_day_off': False}
        )
        if not menu_obj.pk:
            print(f"Hata: {date} günü için Menu kaydı oluşmadı.")
            continue
        for menu_id, menu_data in data:
            for row in menu_data:
                try:
                    food,calori = row
                except:
                    continue
                MenuItems.objects.create(
                    menu=menu_obj,
                    menu_type=MENU_TYPES_DICT.get(menu_id, menu_id),
                    item_name=food,
                    calorie=calori
                )
            
    return "Menü başarıyla eklendi."
