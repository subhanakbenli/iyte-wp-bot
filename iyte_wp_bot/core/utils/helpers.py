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
    categorized_messages,  # Kategorize edilmiş mesajlar dict'i
    header_text="Başlık",
    footer_text="Seçeneğinizi işaretleyiniz",
    button_text="Seçenekleri Göster"
):
    """
    categorized_messages: dict yapısında, örneğin:
    {
        "Ulaşım": messages_queryset_1,
        "Menü": messages_queryset_2
    }
    Her mesaj objesi -> .message_id, .message_text, opsiyonel olarak .message_description
    """
    sections = []
    for section_title, messages in categorized_messages.items():
        rows = []
        for msg in messages:
            row = {
                "id": str(msg.message_id),
                "title": msg.message_text[:24],
            }
            if hasattr(msg, "message_description") and msg.message_description:
                row["description"] = msg.message_description[:72]
            rows.append(row)
        
        sections.append({
            "title": section_title[:24],  # Section başlığı maksimum 24 karakter!
            "rows": rows
        })

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
            "sections": sections
        }
    }
    return interactive_data

