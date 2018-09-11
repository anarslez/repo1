from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "YOU TYPED NEW WELL WOOPTY FRICKEN DO"
    return HttpResponse(response)
def create(request):
    return redirect('/blogs')
def show(request, num):
    response = 'placeholder to display blog '+num
    return HttpResponse(response)
def edit(request, num):
    response = 'placeholder to edit blog '+num
    return HttpResponse(response)
def delete(request):
    return redirect('/')