from rest_framework import serializers
from . import models
class AppointmentSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many = False)
    client = serializers.StringRelatedField(many = False)
    consulter = serializers.StringRelatedField(many = False)
    
    class Meta :
        model = models.Appointment
        fields = '__all__'
        
    