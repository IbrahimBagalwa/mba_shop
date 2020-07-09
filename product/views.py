from django.shortcuts import render
from .models import Product
# Create your views here.

def products(request):
    prod= Product.objects.all()
    return render (request, 'product/products.html',{'products':prod})

def product_detail(request,id):
    product = Product.objects.get(uuid=id)
    return render(request,'product/detail.html', {'product':product})