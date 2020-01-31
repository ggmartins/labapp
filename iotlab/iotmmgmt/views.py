from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse
from django.forms.models import model_to_dict
from iotmmgmt.models import *
from . import jobs

def index(request, cmd):
   o = {}   
   return JsonResponse(o)  
