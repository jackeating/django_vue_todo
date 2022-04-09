from django.shortcuts import render
from .serializers import TodoSerializer
from .models import TodoModel
from rest_framework.viewsets import ModelViewSet


class TodoViewSet(ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
