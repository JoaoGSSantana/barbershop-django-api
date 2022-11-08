from rest_framework import viewsets

from schedules.api import serializers
from schedules import models

class SchedulesViewSet(viewsets.ModelViewSet):
    serializer_class= serializers.SchedulesSerializer
    queryset=models.Schedule.objects.all()
    http_method_names= ['get', "post", 'put', 'patch', 'options', 'delete']
    
class BarberViewSet(viewsets.ModelViewSet):
    serializer_class= serializers.BarberSerializer
    queryset=models.Barber.objects.all()
    http_method_names= ['get', "post", 'put', 'patch', 'options', 'delete']

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class= serializers.ServiceSerializer
    queryset=models.Service.objects.all()
    http_method_names= ['get', "post", 'put', 'patch', 'options', 'delete']