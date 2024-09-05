# views.py
from django.shortcuts import render
from .models import MoodEntry  

def product_list(request):
    products = MoodEntry.objects.all()  
    
    context = {
        'products': products,
        'name' : 'gateron linear fizzy oil keyboard switch',
        'price': '8000',         
        'description': 'Faculty of Computer Science'  
    }
    
    return render(request, 'product_list.html', context)
