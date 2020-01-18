import sys
import geoip2.webservice
import shutil
import csv
from geoip2.errors import *
import iotlab.settings

# MaxMind GeoIP a
#TODO: need refactoring, ports & adapters

def s(s):
  if s is None:
      return ''
  else:
      return str(s).replace(',', ' ')

def i(i):
  if type(i) == int:
      return i
  else:
     try:
         int(i)
     except Exception as e:
         #print("ERROR: mmquery.i " + str(e))
         return -1

#if len(sys.argv) < 2:
#  print("usage: " + sys.argv[0]+" ipaddr")
#  sys.exit(1)
#ipaddr = sys.argv[1]

def mmquery(ipaddr):


    if ipaddr.startswith("127.0.0.1"):
        return {}

    if ipaddr.startswith("10."):
        return {}

    if ipaddr.startswith("192.168."):
        return {}

    if ipaddr.startswith("172.16."):
        return {}


    #fields = ["ip","city","state","country","lat","long","isp","org","domain","ASorg","hits"]

    #terrible:
    #with open(filename, 'r') as csvfile:
    #    reader = csv.DictReader(csvfile, fieldnames=fields)
    #    for row in reader:
    #        if row['ip'] == ipaddr:
    #            #print("hit")
    #            return row
    #            #sys.exit(0)

    #TODO: need adapter
    client = geoip2.webservice.Client(
        iotlab.settings.MMGEOIP_ID,
        iotlab.settings.MMGEOIP_KEY
    )

    try:
        response = client.city(ipaddr)
    except GeoIP2Error as ge:
        if ge is not None:
            print("(GeoIP2Error) Failed to query " + ipaddr)
            print(str(ge)) #TODO: message this
            return {}
    except HTTPError as he:
        if he is not None:
            print("(HTTPSerror) Failed to query " + ipaddr)
            print(str(he))
            return {}
    except Exception as e:
        print("(Exception) Failed to query " + ipaddr)
        print(str(e))
        return {}

    print("Queries remaining:", response.maxmind.queries_remaining)
    #row=(ipaddr+","+s(response.city.name)+","+
    #    s(response.subdivisions.most_specific.iso_code)+","+
    #    s(response.country.iso_code)+","+
    #    s(response.location.longitude)+","+
    #    s(response.traits.isp)+","+
    #    s(response.traits.organization)+","+
    #    s(response.traits.domain)+","+
    #    s(response.traits.autonomous_system_organization)+",\n")
    #print(row, end=""),
    #with open('geoip1.csv','a') as fd:
    #    fd.write(row)
    #    fd.close()
    return {'ip': ipaddr, 'city': s(response.city.name),
            'state': s(response.subdivisions.most_specific.iso_code),
            'country': s(response.country.iso_code),
            'continent': s(response.continent.name),
            'lat': s(response.location.latitude),
            'long': s(response.location.longitude),
            'isp': s(response.traits.isp),
            'org': s(response.traits.organization),
            'domain': s(response.traits.domain),
            'conntype': s(response.traits.connection_type),
            'ASnum': i(response.traits.autonomous_system_number),
            'ASorg': s(response.traits.autonomous_system_organization)}

