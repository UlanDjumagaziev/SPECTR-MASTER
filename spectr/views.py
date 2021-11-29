from django.shortcuts import render
from django.contrib import admin
from .models import Category, Product, Order

def index(request):
    categorys = Category.objects.all()
    return render(request, 'index.html', context = {"categorys":categorys})

def category_detail(request, pk):
    products = Product.objects.filter(category__id=pk)
    return render(request,'shop.html', context = {'products':products})

def product_detail(request, pk):
    product = Product.objects.filter(id=pk).first()
    return render(request,'shop-detail.html', context={'product':product})

def contact_us(request):
    # orders = Order.object.all() 
    return render(request,'contact-us.html')