from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hermes/index.html")

def login(request):
    return render(request, "hermes/login.html")