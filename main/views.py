import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import logging
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

logger = logging.getLogger(__name__)

@login_required(login_url='/login')
def product_detail(request):
    products = Product.objects.filter(user=request.user)
    form = ProductForm()  # Tambahkan ini
    context = {
        'products': products,
        'last_login': request.COOKIES.get('last_login'),
        'form': form,  # Tambahkan ini
    }
    return render(request, 'main.html', context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:product_detail"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:product_detail'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main:product_detail')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def delete_product(request, id):
    products = Product.objects.get(pk=id)
    products.delete()  
    return HttpResponseRedirect(reverse('main:product_detail'))

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ProductForm

@csrf_exempt
def create_product_ajax(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({
                'status': 'success',
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'price': str(product.price),
                    'type': product.type,
                    'sound_profile': product.sound_profile,
                    'image': product.image.url if product.image else '',
                }
            })
        else:
            errors = {field: error[0] for field, error in form.errors.items()}
            return JsonResponse({'status': 'error', 'errors': errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@login_required(login_url='/login')
def get_product_json(request):
    products = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', products), content_type="application/json")

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(
            user=request.user,
            name=data["name"],
            description=data["description"],
            price=data["price"],
            type=data["type"],
            sound_profile=data["sound_profile"],
            image=data.get("image")  # Pastikan untuk menangani file gambar jika ada
        )
        return JsonResponse({
            "status": "success",
            "product": {
                "id": str(product.id),
                "name": product.name,
                "description": product.description,
                "price": str(product.price),
                "type": product.type,
                "sound_profile": product.sound_profile,
                "image": product.image.url if product.image else '',
            }
        }, status=201)
    else:
        return JsonResponse({"status": "error"}, status=400)