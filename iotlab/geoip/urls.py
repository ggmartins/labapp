from django.urls import path
from django.conf.urls import include
from geoip.models import GeoIP
#from rest_framework import routers, serializers, viewsets, mixins
from . import views

#class GeoIPSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = GeoIP
#        fields =  ["ip","city","state","country","lat","lng","isp","org","domain","ASorg","hits"]

#class GeoIPViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
#    queryset = GeoIP.objects.all()
#    serializer_class = GeoIPSerializer


#router = routers.DefaultRouter()
#router.register(r'cached', GeoIPViewSet)

urlpatterns = [
    #path('', include(router.urls))
    path('<str:ipaddr>', views.index, name='index'),
]
