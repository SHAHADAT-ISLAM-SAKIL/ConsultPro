from rest_framework import serializers
from .models import Appointment
from . import models

class AppointmentSerializer(serializers.ModelSerializer):
    time = serializers.PrimaryKeyRelatedField(queryset=models.AvailableTime.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=models.Client.objects.all())
    consulter = serializers.PrimaryKeyRelatedField(queryset=models.Consulter.objects.all())

    class Meta:
        model = Appointment
        fields = '__all__'

        
    