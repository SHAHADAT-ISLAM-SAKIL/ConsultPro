from rest_framework import serializers
from . import models

class ConsulterSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many= False)
    designation =  serializers.StringRelatedField(many = True) #ekane designation ta onek gula hote pare tai true hoyeche but user sudu ekjon(one relationship)tai false hoyeche.
    specialization = serializers.StringRelatedField(many = True)
    available_time = serializers.StringRelatedField(many = True)
    class Meta:
        model = models.Consulter
        fields = '__all__'
        
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'

class DesignationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = '__all__'
    
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = '__all__'
    
class ReviewSerializer(serializers.ModelSerializer):   
    consulter = serializers.StringRelatedField(many= False)
    reviewer = serializers.StringRelatedField(many = False)
    
    
    class Meta:
        model = models.Review
        fields = '__all__'