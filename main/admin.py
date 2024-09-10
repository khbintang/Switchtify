from django.contrib import admin
from .models import Product  # Assuming your model is in models.py

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type', 'sound_profile')  # Customize as needed
