from django.db import models
from uuid import uuid4
# Create your models here.
class Schedule(models.Model):
    scheduleID= models.UUIDField(primary_key=True, default=uuid4, editable=False)
    client = models.CharField(max_length=255)
    service= models.CharField(max_length=150)
    barber= models.CharField(max_length=255)
    date = models.CharField(max_length=10)
    time= models.CharField(max_length=6)
    createAt= models.DateTimeField(auto_now_add=True)
    
class Barber(models.Model):
    barberID= models.UUIDField(primary_key=True, default=uuid4, editable=False)
    barber= models.CharField(max_length=255)
    createAt= models.DateTimeField(auto_now_add=True)

class Service(models.Model):
    serviceID= models.UUIDField(primary_key=True, default=uuid4, editable=False)
    service= models.CharField(max_length=255)
