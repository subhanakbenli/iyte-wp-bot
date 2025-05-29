from django.db import models

# Create your models here.
class Messages(models.Model):
    message_id = models.IntegerField(primary_key=True)
    message_text = models.TextField()
    message_action = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.message_id} - {self.message_text}"

def populate_messages():
    messages_data = [
        (99, '99- Daha Fazla Bilgi', False),
        (11, '11- Bugün Yemekte Ne Var?', False),
        (12, '12- Yarın Yemekte Ne var', False),
        (2,  " 2- İYTE'den Daha Fazla", False),
        (21, '21- İYTE-Heryer', False),
        (22, '22- İYTE-İzmir', False),
        (23, '23- İYTE-Urla', False),
        (24, '24- İYTE-Gülbahçe', False),
        (25, '25- Urla-Çeşme', False),
        (3,  " 3- İYTE'ye Daha Fazla", False),
        (31, '31- Heryer-İYTE', False),
        (32, '32- İzmir-İYTE', False),
        (33, '33- Urla-İYTE', False),
        (34, '34- Gülbahçe-İYTE', False),
        (35, '35- Çeşme-Urla', False),
        
    ]

    for message_id, message_text, message_action in messages_data:
        Messages.objects.update_or_create(
            message_id=message_id,
            defaults={
                'message_text': message_text,
                'message_action': message_action
            }
        )

