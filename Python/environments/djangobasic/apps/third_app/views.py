from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)
def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)
def user(request):
    response = "placeholder for users list"
    return HttpResponse(response)