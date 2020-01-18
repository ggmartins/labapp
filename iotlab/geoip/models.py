from django.db import models
#from datetime import datetime
from django.utils import timezone

class GeoIP(models.Model):
    ip = models.CharField(max_length=46, unique=True)
    is_ipv4 = models.BooleanField(blank=True, null=True)
    city = models.CharField(max_length=100,blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    continent = models.CharField(max_length=100,blank=True, null=True)
    conntype = models.CharField(max_length=100,blank=True, null=True)
    datecached = models.DateTimeField(default=timezone.now, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6,blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6,blank=True, null=True)
    org = models.CharField(max_length=100,blank=True, null=True)
    isp = models.CharField(max_length=100,blank=True, null=True)
    domain = models.CharField(max_length=100,blank=True, null=True)
    ASnum = models.IntegerField(blank=True, null=True) 
    ASorg = models.CharField(max_length=100,blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
