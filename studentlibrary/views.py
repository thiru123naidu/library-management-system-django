from datetime import date, timedelta,datetime

#from datetime import datetime

from django.shortcuts import render

#from library.loginenum import ROLLNIMBER
from library import loginenum

from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from library.models import student
from Books.models import books
from Books.serializers1 import *
import jwt
from library import views

#MY_SECREATE="nsdjcdjs12344t!@#$%^&*()_++-vfdmngbnfgfgntihtoh"
'''@api_view(['GET'])

def read(request):
    studentlibraryobj  = studentlibrary.objects.all()
    serializers1=studentlibraryserializers(studentlibraryobj,many=True)
    return Response(serializers1.data)'''


@api_view(['POST'])
def create(request,id):
    token = request.COOKIES.get('jwt')
    try:
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
        
        student_obj= admin1.objects.get(rollnumber=k)
        serializersdata = admin1serializer(student_obj)
        #print(serializersdata.data)
        if serializersdata.data:
            student_id = student.objects.get(rollnumber = id)
            serializersdata12 = studentserializer(student_id)
            data11=serializersdata12.data[loginenum.ROLLNIMBER]
            #print(data11)
            if data11 == id:
                request.data["issue_date"]=date.today()
                request.data["time_period"]=request.data["issue_date"]+timedelta(days=10)
                serializersdata1=studentlibraryserializers(data=request.data)
                if serializersdata1.is_valid():
                    serializersdata1.save()
                    
                    
                return Response({'success':serializersdata1.data})
        
        else:
            return Response({"status":401,"msg":"your not an admin"})         
        
    
    except:
        return Response({"msg":f"please provide valid rollnumber {id} it is not present in the database"})
    
@api_view(['GET'])
def read(request):
    token = request.COOKIES.get('jwt')
    try:
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
        print(k)
        student_obj= admin1.objects.filter(rollnumber=k).first()
        serializersdata = admin1serializer(student_obj)
        print(serializersdata.data)
        if serializersdata.data[loginenum.ROLLNIMBER]!=None:
           
            student_obj1=studentlibrary.objects.all()
       
            serializersdata111 = studentlibraryserializers(student_obj1,many=True)
           
            return Response({"payload": serializersdata111.data})

            
            
        else:
            return Response({"status":401,"msg":"your not elegible  to see all the student's related information because your not an admin"})
    except:
        return Response({"msg":"please login with your account"})



@api_view(['GET'])
def retrive(request,id):
    token=request.COOKIES.get('jwt')
    try:
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
        print(k)
        student_obj= admin1.objects.filter(rollnumber=k).first()
        serializersdata = admin1serializer(student_obj)
        print(serializersdata.data)
        if serializersdata.data[loginenum.ROLLNIMBER]!=None:
            student_id=studentlibrary.objects.filter(student_rollnumber=id).first()
            print("hi")
            serializersdata111 = studentlibraryserializers(student_id)
            return Response({"payload":serializersdata111.data})
        else:
            return Response({"status":401,"msg":"your not an admin"})
    except:
        return Response({"msg":f"please provide valid rollnumber {id} it is not present in the database"})


    
@api_view(['DELETE'])
def delete(request,id):
    token=request.COOKIES.get('jwt')
    try:
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
        #print(k)
        student_obj= admin1.objects.filter(rollnumber=k).first()
        serializersdata = admin1serializer(student_obj)
        
        if serializersdata.data[loginenum.ROLLNIMBER]!=None:
            studentid1=studentlibrary.objects.all().filter(student_rollnumber=id).first()
            studentid1.delete()

            return Response({"msg":f"successfully deleted rollnumber of {id}"})
        else:
            return Response({"status":401,"msg":"your not an admin"})
                
    except:
        return Response({"msg":f"please provide valid rollnumber {id} it is not present in the database"})
    
@api_view(['POST'])
def update(request,id):
    try:
        studentid=studentlibrary.objects.all().filter(student_rollnumber=id).first()
        serializersdata=studentlibraryserializers(instance=studentid,data=request.data)
        if serializersdata.is_valid():
            serializersdata.save()
            return Response({"msg":f"successfully updated rollnumber of {id}"})
    except:
        return Response({"msg":f"please provide valid rollnumber {id} it is not present in the database"})
    
@api_view(['PUT'])
def returning_book(request,id):
    token=request.COOKIES.get('jwt')
    try:
   
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
        print(k)
        student_obj= admin1.objects.filter(rollnumber=k).first()
        serializersdata = admin1serializer(student_obj)
        
        
        if serializersdata.data[loginenum.ROLLNIMBER]!=None:
            student_id=studentlibrary.objects.filter(student_rollnumber=id).first()
            serializerdata12=studentlibraryserializers(student_id)
            print(serializerdata12.data)                                                        
            if serializerdata12.data:
                return_date=datetime.strptime(request.data["return_date"],"%Y-%m-%d").date()
             
                value1=datetime.strptime(serializerdata12.data["time_period"],"%Y-%m-%d").date()
           
                days1=(return_date-value1).days
                print(days1)
                

                if days1<=0:
                    obj=studentlibrary.objects.get(student_rollnumber=id)
                    obj.return_date=return_date
                    obj.save()
                    return Response({"success": 400, "message": "you need not to pay money"})
                    
                    
                else:
                    penalty1=days1*10
                   
                    obj=studentlibrary.objects.get(student_rollnumber=id)
                    obj.return_date=return_date
                    obj.penalty=penalty1
                    obj.save()
                   
                    return Response({"msg":f"you need to pay penalty========{penalty1}"})
                    
            else:
                return Response({"status":201,"msg":"please give a valid student_id"})
        else:
            return Response({"status":401,"msg":"your not an admin"})
    except:
        return Response({"msg":f"please provide valid rollnumber {id} it is not present in the database"})
        

                    



@api_view(['GET'])
def retrive_studentid(request,id):
    token = request.COOKIES.get('jwt')
    try:
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
        print(k)
        student_obj= admin1.objects.filter(rollnumber=k).first()
        serializersdata = admin1serializer(student_obj)
        
        if serializersdata.data[loginenum.ROLLNIMBER]!=None:
            student_id = student.objects.get(rollnumber=id)
            serializersdata1 = studentserializer(student_id)
            return Response({"status": "success", "data": serializersdata1.data})
        else:
            return Response({"status": 401,"message":"your not an administrator"})
    except:
        return Response({"payload":f"please provide valid rollnumber {id} it is not present in the database"})

@api_view(['DELETE'])
def student_delete(request,id):
    token = request.COOKIES.get('jwt')
    try:
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
        print(k)
        student_obj= admin1.objects.filter(rollnumber=k).first()
        serializersdata = admin1serializer(student_obj)
        
        if serializersdata.data[loginenum.ROLLNIMBER]!=None:
            student_obj1= student.objects.filter(rollnumber=id).first()
            student_obj1.delete()
            return Response({"msg":"successfully deleted "})
        else:
            return Response({"status":401,"msg":"you are not allowed to delete this student because your not an admin"})
    except:
        return Response({"msg":"please provide valid rollnumber it is not present in the database"})
    

@api_view(['POST'])
def updatestuid(request,id):
    token = request.COOKIES.get('jwt')
    try:
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
      
        student_obj= admin1.objects.filter(rollnumber=k).first()
        serializersdata = admin1serializer(student_obj)
        if serializersdata.data[loginenum.ROLLNIMBER]!=None:
            
            student_obj1= student.objects.get(rollnumber = id)
           
            serializersdata1=studentserializer(instance=student_obj1,data=request.data)
            if serializersdata1.is_valid():
                serializersdata1.save()
    


            return Response({"payload":serializersdata1.data})
        else:
            return Response({"status":401,"msg":"you don't an access to updates because your not an admin"})
    except:
        return Response({"payload":f"please provide valid rollnumber {id} it is not present in the database"})


@api_view(['GET'])


def readallstuid(request):
    token = request.COOKIES.get('jwt')
    try:
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
        
        student_obj= admin1.objects.filter(rollnumber=k).first()
        serializersdata = admin1serializer(student_obj)
        
        if serializersdata.data[loginenum.ROLLNIMBER]!=None:
           
            student_obj1=student.objects.all()
       
            serializersdata111 = studentserializer(student_obj1,many=True)
           
            return Response({"payload": serializersdata111.data})

            
            
        else:
            return Response({"status":401,"msg":"your not elegible  to see all the student's related information because your not an admin"})
    except:
        return Response({"msg":"please provide valid rollnumber it is not present in the database"})


@api_view(['POST'])
def createstuid(request):
    token = request.COOKIES.get('jwt')
    try:
        payload1=jwt.decode(token,options={"verify_signature":False})
        k=payload1[loginenum.ROLLNIMBER]
      
        student_obj= admin1.objects.filter(rollnumber=k).first()
        serializersdata = admin1serializer(student_obj)
        
        if serializersdata.data[loginenum.ROLLNIMBER]!=None:
            serializersdata1=studentserializer(data=request.data)
            if serializersdata1.is_valid():
                serializersdata1.save()

         
            
        else:
            return Response({"status":401,"msg":"your not an admin"})
    except:
        return Response({"msg":"please provide valid rollnumber it is not present in the database"})