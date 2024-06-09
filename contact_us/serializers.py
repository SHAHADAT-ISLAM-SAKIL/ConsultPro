from rest_framework import serializers
from . import models
class ContactUsserializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = '__all__'
    