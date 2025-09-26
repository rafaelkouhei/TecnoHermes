from django.urls import path
from . import views

app_name = "hermes"
urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("login", views.login, name="login"),
    path("inventory", views.inventory, name="inventory"),
    path("add_item", views.add_item, name="add_item")
]