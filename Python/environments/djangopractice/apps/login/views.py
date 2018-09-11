from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request): 
    return render(request,'login/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = password)
        request.session['user_id'] = User.objects.get(email = request.POST['email']).id
        return redirect('/books') #THE ROUTE THAT LEADS TO INDEX OF APP TWO

def login(request): 
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        request.session['user_id'] = User.objects.get(email = request.POST['email']).id
        return redirect('/books') #THE ROUTE THAT LEADS TO INDEX OF APP TWO


def logout(request):
    del request.session['user_id']
    return redirect('/')