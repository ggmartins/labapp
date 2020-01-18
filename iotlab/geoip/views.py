from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse
from django.forms.models import model_to_dict
from geoip.models import GeoIP
import json
import re
from . import geoipquery

#lift from https://gist.github.com/mnordhoff/2213179
ipv4re = re.compile(
    '^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
    )
ipv6re = re.compile(
    '^(?:(?:[0-9A-Fa-f]{1,4}:){6}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|::(?:[0-9A-Fa-f]{1,4}:){5}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){4}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){3}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,2}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){2}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,3}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}:(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,4}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,5}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}|(?:(?:[0-9A-Fa-f]{1,4}:){,6}[0-9A-Fa-f]{1,4})?::)$'
    )

def index(request, ipaddr):
    o={}
    is_ipv4 = True
    if request.method != 'GET':
        return JsonResponse("ERROR: Only GET method allowed.")
    else:
        if (ipaddr.startswith("10.") or
              ipaddr.startswith("127.0.0.1") or
              ipaddr.startswith("192.168.") or
              ipaddr.startswith("172.16.")):
            o['error']='local ipv4 address'
            return JsonResponse(o)

        if(ipv4re.match(ipaddr)):
            print("geoip: valid ipv4 address")
        elif (ipv6re.match(ipaddr)):
            print("geoip: valid ipv6 address")
            is_ipv4 = False
        else:
            o['error']='not valid ipv4 / ipv6 address'
            return JsonResponse(o)
        
        try:
          o=model_to_dict(GeoIP.objects.get(ip=ipaddr))
          print("geoip: hit")
        except GeoIP.DoesNotExist:

          d=geoipquery.mmquery(ipaddr)
          print("geoip: query executed.")
          if (d == {}):
              d['error'] = 'unable to query API'
              return JsonResponse(d)
          print("geoip: caching...")
          obj=GeoIP(
              ip=d['ip'],
              is_ipv4 = is_ipv4,
              city=d['city'],
              state=d['state'],
              country=d['country'],
              continent=d['continent'],
              conntype=d['conntype'],
              lat=d['lat'],
              lng=d['long'],
              isp=d['isp'],
              org=d['org'],
              domain=d['domain'],
              ASnum=d['ASnum'],
              ASorg=d['ASorg'],
              hits=1
          )
          obj.save()
          o=model_to_dict(obj)
        
        #if(o=={}):
        #    return HttpResponseNotFound()
        print("geoip: OK")
        return JsonResponse(o)
    
