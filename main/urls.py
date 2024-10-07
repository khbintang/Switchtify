from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import product_detail, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product
from . import views
from .views import create_product_ajax
from .views import get_product_json, create_product_ajax

app_name = 'main'

urlpatterns = [
    path('', product_detail, name='product_detail'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>/', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('create-product/', views.create_product, name='create_product'),
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    # path('', views.home, name='home'),
    # path('cart/', views.cart, name='cart'),
    # path('contact/', views.contact, name='contact'),
]