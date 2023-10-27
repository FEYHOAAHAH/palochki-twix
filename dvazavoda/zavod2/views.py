from django.http import HttpRequest
from django.shortcuts import render

from .models import *


# Create your views here.
def show_products(request: HttpRequest):
    context = {'products': Confectionery.objects.filter(availability=True)}
    return render(request, 'product.html', context)


def show_product(request: HttpRequest, pk):
    context = {'product': Confectionery.objects.get(pk=pk)}
    return render(request, 'product_detailed.html', context)
