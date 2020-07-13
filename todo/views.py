from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializer import TaskSerializer
# Create your views here.

class Taskslist(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAdd(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

