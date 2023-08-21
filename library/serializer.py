from rest_framework import serializers

from .models import student,admin1

class studentserializer(serializers.ModelSerializer):
    
    class Meta:
        model = student
        
        fields = '__all__' 
        

class admin1serializer(serializers.ModelSerializer):
    class Meta:
        model = admin1
        fields = '__all__'