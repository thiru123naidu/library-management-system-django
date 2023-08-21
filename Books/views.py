from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers1 import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
import requests
#from rest_framework.response import Response

class bookslist(ListAPIView):
    queryset = books.objects.all()
    serializer_class = bookserializer

class bookscreate(CreateAPIView):
    queryset = books.objects.all()
    serializer_class = bookserializer

class booksretrive(RetrieveAPIView):
    queryset = books.objects.all()
    serializer_class = bookserializer

class booksdelete(DestroyAPIView):
    queryset = books.objects.all()
    serializer_class = bookserializer 

class booksupdate(UpdateAPIView):
    queryset = books.objects.all()
    serializer_class = bookserializer



'''def books_data():

    url = "https://www.googleapis.com/books/v1/volumes?q=books+inauthor:keyes&key=AIzaSyCLf1J-zhHycgx9PvwNX5lOAAXrcYiiNt0"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

print(books_data())'''
    
