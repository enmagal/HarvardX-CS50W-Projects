from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def enzo(request):
    return HttpResponse("Hello, Enzo!")

def agathe(request):
    return HttpResponse("Hello, Agathe!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize
    })