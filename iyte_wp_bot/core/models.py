from django.db import models

# Create your models here.
class Messages(models.Model):
    message_id = models.IntegerField(primary_key=True)
    message_text = models.TextField()
    message_action = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.message_id} - {self.message_text}"