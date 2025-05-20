def interactive_button_text(text, buttons_list):
    buttons = []
    for button in buttons_list:
        item = {
            "type": "reply",
            "reply": {
                "id": str(button.message_id),         # ID alanı
                "title": button.message_text[:20]     # Başlık, WhatsApp 20 karakter sınırı var!
            }
        }
        buttons.append(item)

    interactive_data = {
        "type": "button",
        "body": {
            "text": text
        },
        "action": {
            "buttons": buttons
        }
    }
    return interactive_data

def interactive_list_text(
    body_text, 
    messages_queryset, 
    header_text="Ulaşım", 
    footer_text="İstek Seçeneğinizi işaretleyiniz", 
    button_text="Seçenekleri Göster",
    section_title="Seçenekler"
):
    """
    messages_queryset: Messages queryseti (veya listesi)
    Her mesaj -> .message_id (id), .message_text (title), .message_description (opsiyonel, modeline ekleyebilirsin)
    """
    rows = []
    for msg in messages_queryset:
        row = {
            "id": str(msg.message_id),
            "title": msg.message_text[:24],  # WhatsApp'ta title max 24 karakter!
        }
        # Eğer açıklama alanı varsa ekle
        if hasattr(msg, "message_description") and msg.message_description:
            row["description"] = msg.message_description[:72]  # Description max 72 karakter!
        rows.append(row)
    
    interactive_data = {
        "type": "list",
        "header": {
            "type": "text",
            "text": header_text
        },
        "body": {
            "text": body_text
        },
        "footer": {
            "text": footer_text
        },
        "action": {
            "button": button_text,
            "sections": [
                {
                    "title": section_title,
                    "rows": rows
                }
            ]
        }
    }
    return interactive_data



