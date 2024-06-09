from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ContactusViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsserializer
