from rest_framework import serializers
from schedules import models

class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
     model= models.Schedule
     fields= '__all__'
     
class BarberSerializer(serializers.ModelSerializer):
    class Meta:
     model= models.Barber
     fields= '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
     model= models.Service
     fields= '__all__'