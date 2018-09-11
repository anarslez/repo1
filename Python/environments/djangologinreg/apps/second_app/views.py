from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    id = request.session['user_id']
    user = User.objects.get(id = id)
    context = {
        'fname': user.first_name,
        'posts' : Message.objects.all().order_by('-created_at'),
    } 
    return render(request,'second_app/index.html', context)

def post(request):
    id = request.session['user_id']
    user = User.objects.get(id = id)
    errors = Message.objects.message_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    else:
       Message.objects.create(content = request.POST['content'], author = user) 
       return redirect('/wall')

def comment(request):
    id = request.session['user_id']
    user = User.objects.get(id = id)
    errors = Message.objects.message_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    else:
        messid = request.POST['messid']
        mess = Message.objects.get(id = messid)
        Comment.objects.create(content = request.POST['content'], author = user, parent = mess) 
        return redirect('/wall')
