from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime

def index(request):
    context = {
        "num": get_random_string(length=14)
    }
    return render(request,'first_app/index.html', context)
def rand(request):
    if request.method == "POST":
        return redirect("/")
    else:
        return redirect("/")
