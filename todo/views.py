#from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from serializers import Todo,TodoSerializer
class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# Create your views here.
