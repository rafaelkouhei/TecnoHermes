from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="hermes/index"),
    path("login", views.login, name="hermes/login"),
]