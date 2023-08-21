from django.contrib import admin
from django.urls import path
from .views import *
from Books import views
urlpatterns = [
    path("login/",login),
    path("retrive/",retrive),
    path("retrivelibrary/",retrivelibrary),
    path("bookslist/",views.bookslist.as_view())
]