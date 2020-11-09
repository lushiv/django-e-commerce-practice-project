from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math


def index(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + math.ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return  render(request, 'shop/index.html')


def about_us(request):
    return render(request, 'shop/about.html')



def contact(request):
    return HttpResponse("Contacts")


def tracker(request):
    return HttpResponse("Tracker")



def search(request):
    return HttpResponse("Search")


def prod_views(request):
    return HttpResponse("Products")

def checkout(request):
    return HttpResponse("Checkout")


