from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
import datetime

class itemForm(forms.Form):
    item_id = forms.CharField(label="Código")
    description = forms.CharField(label="Descrição")
    unity = forms.CharField(label="Unidade")
    qty = forms.IntegerField(label="Quantidade", min_value=1)
    date = forms.DateField(label="Data")

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "hermes/index.html")

def login(request):
    return render(request, "hermes/login.html")

# tst products
items = []
def inventory(request):
    return render(request, "hermes/inventory.html", {
        "item_list": items
    })

def add_item(request):
    if request.method == "POST":
        form = itemForm(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data["item_id"]
            items.append(item_id)
            return HttpResponseRedirect(reverse("hermes:inventory"))
        else:
            return render(request, "hermes/add_item.html", {
                "form": form
            })

    return render(request, "hermes/add_item.html", {
        "form": itemForm
    })