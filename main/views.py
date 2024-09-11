from django.shortcuts import render
from .models import Product

# Product detail view
def product_detail(request):
    product = Product.objects.first()  # Get the product object, replace with your logic
    context = {
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'type': product.type,
        'sound_profile': product.sound_profile,
        'image_url': product.image.url,  # assuming image field exists
    }
    return render(request, 'main.html', context)

# About app view
def about_app(request):
    context = {
        'app_name': 'Switchtify',  # Nama aplikasimu
        'student_name': 'Khairul Bintang',
        'class_name': 'PBP F',
    }
    return render(request, 'main.html', context)
