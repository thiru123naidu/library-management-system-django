from rest_framework import serializers
from .models import *

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = books

        fields ='__all__'