from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class ServiceViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Service.objects.all()
    serializer_class = serializers.Serviceserializer
