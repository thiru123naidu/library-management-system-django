from django.contrib import admin
from django.urls import path
from Books import views
urlpatterns = [

    path("read/",views.bookslist.as_view()),
    path("create/",views.bookscreate.as_view()),
    path("retrive/<int:pk>/",views.booksretrive.as_view()),
    path("delete/<int:pk>/",views.booksdelete.as_view()),
    path("update/<int:pk>/",views.booksupdate.as_view()),
    
]