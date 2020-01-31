from django.db import models
#from datetime import datetime
from django.utils import timezone


class ArpStatus(models.Model):
    status = models.CharField(max_length=12, null=True)

class ArpMac(models.Model):
    mac = models.CharField(max_length=60, unique=True)
    ouiman = models.CharField(max_length=100, unique=True)
    input_man = models.CharField(max_length=100, unique=True)
    input_type = models.CharField(max_length=100, unique=True)
    input_model = models.CharField(max_length=100, unique=True)

class ArpBuffer(models.Model):
    ts = models.DateTimeField(default=timezone.now, unique=True)
    mac = models.ForeignKey(ArpMac, on_delete=models.CASCADE)
    status = models.ForeignKey(ArpStatus, on_delete=models.CASCADE)

class ArpReading(models.Model):
    ts = models.ForeignKey(ArpBuffer, on_delete=models.CASCADE)
