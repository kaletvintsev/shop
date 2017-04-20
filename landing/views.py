from django.shortcuts import render
from products.models import *




def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_on_main = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True,
                                                  product__is_on_main=True)
    products_images_kurtki = products_images.filter(product__category__id=1)
    products_images_dublenki = products_images.filter(product__category__id=2)
    products_images_plashi = products_images.filter(product__category__id=3)
    return render(request, 'landing/home.html', locals())

