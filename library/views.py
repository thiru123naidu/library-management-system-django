from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

from studentlibrary.models import *
from studentlibrary.serializer import *
from Books.models import *
from Books.serializers1 import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
import jwt
from library import loginenum

MY_SECREATE="nsdjcdjs12344t!@#$%^&*()_++-vfdmngbnfgfgntihtoh"


    

@api_view(['POST'])
def register(request):
    #insert1 = student.objects.all()
    serializersdata=studentserializer(data=request.data)
    if serializersdata.is_valid():
        serializersdata.save()

    return Response({"payload": serializersdata.data})




@api_view(['POST'])
def login(request):
    rollnumber = request.data['rollnumber']
    password = request.data['password']
    user=admin1.objects.filter(rollnumber=rollnumber).first()
    if user != None:
        serializersdata = admin1serializer(user)
        if serializersdata:
            payload = {loginenum.ROLLNIMBER: serializersdata.data[loginenum.ROLLNIMBER],"password": serializersdata.data["password"]}
            token = jwt.encode(payload=payload,key=MY_SECREATE, algorithm="HS256")
            response = Response()
            response.set_cookie(key="jwt",value=token,httponly=True)
            response.data ={
                "jwt":token,
            }
            return response
    else:
        user1=student.objects.filter(rollnumber=rollnumber).first()
        serializersdata123 = studentserializer(user1)
        if serializersdata123:
            payload = {loginenum.ROLLNIMBER: serializersdata123.data[loginenum.ROLLNIMBER],"password": serializersdata123.data["password"]}
            token = jwt.encode(payload=payload,key=MY_SECREATE, algorithm="HS256")
            response = Response()
            response.set_cookie(key="jwt",value=token,httponly=True)
            response.data ={
                "jwt":token,
            }
            return response


        else:
            return Response({"msg":"you are not a admin so please take admin access and then try login please"})
    
@api_view(['GET'])
def retrive(request):
    token = request.COOKIES.get('jwt')
    try:
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
       
        student_obj= student.objects.get(rollnumber=k)
        serializersdata = studentserializer(student_obj)
       
        if serializersdata.data:
            
            student_id = student.objects.get(rollnumber=k)
            serializersdata1 = studentserializer(student_id)
            return Response({"status": "success", "data": serializersdata1.data})
        else:
            return Response({"status": 401,"message":"your not an administrator"})
    except:
        return Response({"payload":"please login with your account"})



@api_view(['GET'])
def retrivelibrary(request):
    token = request.COOKIES.get('jwt')
    try:
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
       
        student_obj= student.objects.get(rollnumber=k)
        serializersdata = studentserializer(student_obj)
       
        if serializersdata.data:
          
            student_id = studentlibrary.objects.get(student_rollnumber=k)
           
            serializersdata1 = studentlibraryserializers(student_id)
         
            return Response({"status": "success", "data": serializersdata1.data})
        else:
            return Response({"status": 401,"message":"your not an administrator"})
    except:
        return Response({"payload":"this for student api"})

class bookslist(ListAPIView):
    queryset = books.objects.all()
    serializer_class = bookserializer
  


        
    

    






