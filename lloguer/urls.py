from django.contrib import admin
from django.urls import include, path

from lloguer import views

urlpatterns = [
    path("menu", views.menu, name="menu"),
]