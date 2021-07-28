from django.shortcuts import render

# Create your views here.
from django.db import models
from rest_framework import generics
from .models import Motor
from .serializer import SerializerMotor
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostsListView(generics.ListCreateAPIView):
    serializer_class = SerializerMotor
    queryset = Motor.objects.all()

class PostDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializerMotor
    queryset = Motor.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)