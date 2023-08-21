from rest_framework import serializers
from .models import *
class studentlibraryserializers(serializers.ModelSerializer):
    class Meta:
        model = studentlibrary
        fields = '__all__'