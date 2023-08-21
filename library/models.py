from django.db import models

# Create your models here.
class student(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    
    gender = models.CharField(max_length=10)
    role = models.CharField(max_length=10,default="student")
    #password1 = models.CharField(max_length=50)
    
class admin1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)

