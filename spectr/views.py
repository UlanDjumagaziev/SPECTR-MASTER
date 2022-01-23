
import telegram

from django.conf import settings

from django.shortcuts import redirect, render
from django.contrib import admin
from .models import Category, Product, Order, Carousel
from .forms import CommentForm
from spectr import utils

def index(request):
    categorys = Category.objects.all()
    carousel = Carousel.objects.filter()
    return render(request, 'index.html', context = {"categorys":categorys, 'carousel': carousel})

def category_detail(request, pk):
    categorys = Category.objects.all()
    products = Product.objects.filter(category__id=pk)
    return render(request,'shop.html', context = {'products':products,"categorys":categorys})

def product_detail(request, pk):
    categorys = Category.objects.all()
    product = Product.objects.filter(id=pk).first()
    return render(request,'shop-detail.html', context={'product':product,"categorys":categorys})

def contact_us(request):
    categorys = Category.objects.all() 
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        dict = request.POST.copy()
        dict.pop("csrfmiddlewaretoken")
        message = utils.message.format(**dict)
        message = message.replace('[','')
        message = message.replace(']','')
        message = message.replace("'","")
        bot = telegram.Bot(token=settings.BOT_TOKEN)
        bot.send_message(chat_id=settings.CHAT_ID, text=message)
        return redirect('spectr:index')
    return render(request,'contact-us.html', context={"categorys":categorys,"form":form})