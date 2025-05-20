from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from .utils import add_monthly_menu



def add_monthly(request):
    print("Adding monthly menu...")
    print(add_monthly_menu())
    return JsonResponse({'message': 'Monthly menu added successfully'})