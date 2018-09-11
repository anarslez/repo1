from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request): 
    return render(request,'first_app/index.html')
def buy(request):
    prod = Product.objects.get(id = request.POST['product_id'])
    cost = prod.price * int(request.POST['quantity'])
    name = prod.name
    Order.objects.create(name = prod.name, price = cost, quantity = request.POST['quantity'], product = prod)
    return redirect('/checkout')
def checkout(request):
    context = {
        'order' : Order.objects.last()
    }
    return render(request,'first_app/checkout.html', context)