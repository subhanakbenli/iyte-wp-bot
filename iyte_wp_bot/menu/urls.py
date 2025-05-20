from django.contrib import admin
from django.urls import path, include
from .views import add_monthly
urlpatterns = [
    path('asd/', add_monthly, name='add_monthly_menu'),
]

