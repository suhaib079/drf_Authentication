  
from django.db import models
from rest_framework import serializers

from .models import Motor

class SerializerMotor(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'type', 'model', 'color', 'manufacturer')
        model = Motor