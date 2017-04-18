from django.shortcuts import render
from products.models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product.html', locals())
#
# # def last_four(request):
#     return render(request, 'landing/product_item.html', {'Product': Product})