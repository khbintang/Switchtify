# views.py
from django.shortcuts import render


def product_list(request):
    
    
    context = {
        
        'name' : 'gateron linear fizzy oil keyboard switch',
        'price': '8000',         
        'description': 'Faculty of Computer Science'  
    }
    
    return render(request, 'main.html', context)
