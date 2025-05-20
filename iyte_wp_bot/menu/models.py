from django.db import models

# Create your models here.
from django.db import models


class Menu(models.Model):
    date = models.DateField()
    is_day_off = models.BooleanField(default=False)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
     
    def add_like(self):
        self.likes += 1
        self.save()
    def add_dislike(self):
        self.dislikes += 1
        self.save()

    def __str__(self):
        return f"{self.date} - {self}"
    
class MenuItems(models.Model):
    menu_type = models.TextField(max_length=40) 
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="menu_items")
    item_name = models.CharField(max_length=100)
    calorie = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.item_name} ({self.menu_type})"
    
