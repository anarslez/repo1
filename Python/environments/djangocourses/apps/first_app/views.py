from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.
def index(request): 
    context = {
        'list' : Course.objects.all()
    }
    return render(request,'first_app/index.html', context)
def add(request):
    Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
    return redirect("/")
def deletewarning(request):
    course_id = request.POST['id']
    return redirect("delete", id = course_id)
def delete(request, id):
    course = Course.objects.get(id = id)
    context = {
        'name' : course.name,
        'desc' : course.desc,
        'id' : course.id,
    }
    return render(request,'first_app/delete.html', context)
def confirm(request):
    Course.objects.get(id = request.POST['id']).delete()
    return redirect("/")