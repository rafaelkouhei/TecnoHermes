from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "hermes/index.html")

def login(request):
    return render(request, "hermes/login.html")

# tst products
item_list = ["first", "second", "third"]
def inventory(request):
    return render(request, "hermes/inventory.html", {
        "item_list": item_list
    })

def add_item(request):
    return render(request, "hermes/add_item.html")