# core/utils/messaging.py
import os
import requests

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

HEADERS = {
    "Authorization": f"Bearer {WHATSAPP_TOKEN}",
    "Content-Type": "application/json"
}

def send_whatsapp_text(to_number, message):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "text",
        "text": {
            "body": message
        }
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    print("Text message response:", response.status_code, response.text)
    return response.json()

def send_image_message(to_number, image_url):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "image",
        "image": {
            "link": image_url
        }
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    print("Image message response:", response.status_code, response.text)
    return response.json()

def send_document_message(to_number, doc_url):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "document",
        "document": {
            "link": doc_url,
            "filename": "ornek.pdf"
        }
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    print("Document message response:", response.status_code, response.text)
    return response.json()

def send_audio_message(to_number, audio_url):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "audio",
        "audio": {
            "link": audio_url
        }
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    print("Audio message response:", response.status_code, response.text)
    return response.json()

def send_video_message(to_number, video_url):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "video",
        "video": {
            "link": video_url
        }
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    print("Video message response:", response.status_code, response.text)
    return response.json()

def send_button_message(phone_number,interactive_data):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "interactive",
        "interactive": interactive_data
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    
    print("Button message response:", response.status_code, response.text)
    return response.json()

def send_list_message(phone_number, interactive_data):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "interactive",
        "interactive": interactive_data
    }

    response = requests.post(url, headers=HEADERS, json=payload)
    print("List message response:", response.status_code, response.text)

    try:
        return response.json()
    except Exception as e:
        print("JSON parse hatası:", e)
        return None

def send_template_message(to_number):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
                "code": "en_US"
            }
        }
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    print("Template message response:", response.status_code, response.text)
    return response.json()

def send_location_message(to_number):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "location",
        "location": {
            "latitude": 37.7749,
            "longitude": -122.4194,
            "name": "Konum İsmi",
            "address": "123 Konum Adresi"
        }
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    print("Location message response:", response.status_code, response.text)
    return response.json()

def send_contact_message(to_number):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "contacts",
        "contacts": [
            {
                "name": {
                    "formatted_name": "Sübhan Akbenli",
                    "first_name": "Sübhan",
                    "last_name": "Akbenli"
                },
                "phones": [
                    {
                        "phone": "+905522612829",
                        "type": "mobile"
                    }
                ]
            }
        ]
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    print("Contact message response:", response.status_code, response.text)
    return response.json()
