from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    user_id = request.session['user_id']
    context = {
        'fname': User.objects.get(id = user_id).first_name,
        'reviews': Review.objects.all(),
        'books': Book.objects.all()
    }
    return render(request,'books/index.html', context)

def create(request):
    user_id = request.session['user_id']
    context = {
        'fname': User.objects.get(id = user_id).first_name,
        'authors' : Author.objects.all()
    }
    return render(request,'books/create.html', context)

def add(request):
    user_id = request.session['user_id']
    errors = Author.objects.author_validator(request.POST)
    if request.POST['id'].isdigit() == True:
        author = Author.objects.get(id = int(request.POST['id']))
    elif len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books/create')
    else:
        Author.objects.create(name = request.POST['name'])
        author = Author.objects.get(name = request.POST['name'])
    errors = Book.objects.book_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books/create')
    else:
        errors = Review.objects.review_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            Book.objects.create(title = request.POST['title'], author = author)
            return redirect('/books/create')
        else:
            Book.objects.create(title = request.POST['title'], author = author)
            book = Book.objects.last()
            Review.objects.create(content = request.POST['content'], rating = int(request.POST['rating']), reviewer = User.objects.get(id = user_id), book = book)
            return redirect('/books')

def show(request):
    pass

def delete(request):
    pass