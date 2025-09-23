from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="hermes/index"),
    path("index", views.index, name="hermes/index"),
    path("login", views.login, name="hermes/login"),
    path("inventory", views.inventory, name="inventory"),
    path("add_item", views.add_item, name="add_item")
]