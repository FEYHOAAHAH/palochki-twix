from django.urls import path, re_path

from .views import *

app_name = 'zavod1'

urlpatterns = [
    path('', show_products, name='product'),
    path('product/<int:pk>/', show_product, name='product_detailed'),
]
