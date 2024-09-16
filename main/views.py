from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

def product_detail(request):
    product = Product.objects.first()  
    context = {
        'product': product 
    }
    return render(request, 'main.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:product_detail')  
    else:
        form = ProductForm()
    
    return render(request, 'create_product.html', {'form': form})


def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def about_app(request):
    context = {
        'app_name': 'Switchtify',  
        'student_name': 'Khairul Bintang',
        'class_name': 'PBP F',
    }
    return render(request, 'main.html', context)
