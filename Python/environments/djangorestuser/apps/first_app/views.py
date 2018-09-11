from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request): 
    context = {
        'list' : User.objects.all()
    }
    return render(request,'first_app/index.html', context)
def new(request):
    return render(request,'first_app/adduser.html')
def add(request):
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
    return redirect("/")
def edit(request,id):
    user = User.objects.get(id = id)
    context = {
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'email' : user.email,
        'id': user.id
    }
    return render(request,'first_app/edituser.html', context)
def edituser(request):
    user_id = request.POST['id']
    return redirect("edit", id = user_id)
def update(request):
    user = User.objects.get(id = request.POST['id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name'] 
    user.email = request.POST['email']
    user.save()
    return redirect("/")
def showuser(request):
    user_id = request.POST['id']
    return redirect("show", id = user_id)
def show(request,id):
    user = User.objects.get(id = id)
    context = {
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'email' : user.email,
        'id': user.id
    }
    print(context)
    return render(request,'first_app/show.html', context)
