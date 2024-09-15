from django.shortcuts import render
from .models import Product


from django.shortcuts import render
from .models import Product

def product_detail(request):
    product = Product.objects.first()  
    context = {
        'product': product 
    }
    return render(request, 'main.html', context)


def about_app(request):
    context = {
        'app_name': 'Switchtify',  # Nama aplikasimu
        'student_name': 'Khairul Bintang',
        'class_name': 'PBP F',
    }
    return render(request, 'main.html', context)
