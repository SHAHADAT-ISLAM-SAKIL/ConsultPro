from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class Appointmentviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    
    #custom query kortechi
    def get_queryset(self):
        queryset = super().get_queryset() #9 number line ke inherit korlam
        client_id = self.request.query_params.get('client_id')
        if client_id:
            queryset = queryset.filter(client_id = client_id)
        return queryset
        