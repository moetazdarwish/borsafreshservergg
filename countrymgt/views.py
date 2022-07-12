from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse, HttpResponse
# Create your views here.
from countrymgt.countryserilazer import LocationSerializer, AllCountriesSerializer, CitySerializer, ZoneSerializer
from countrymgt.models import CityZone, NewZone, CountryManager, CityManagement


@api_view(['GET'])
def getLocation(request):
    latitude = request.query_params.get('latitude')
    longitude = request.query_params.get('longitude')
    try:
        get_zone = CityZone.objects.get(lat_greater__lte=latitude, lat_lower__gte=latitude, long_greater__lte=longitude,
                                        long_lower__gte=longitude)
        country = get_zone.country.country
        city = get_zone.city.city

        data = []
        city = city
        country = country
        data = {
            "key": "true",
            "zone": get_zone.id,
            "msg": "no Msg"
        }
        ser_loc = LocationSerializer(data).data
        return Response(ser_loc)
    except:
        NewZone.objects.create(lat=latitude, long=longitude)
        data = {
            "key": "false",
            "zone": "no zone",
            "msg": "Please Contact Support , to get nearest Area to You "
        }
        ser_loc = LocationSerializer(data).data
        return Response(ser_loc)

@api_view(['GET'])
def getCountry(request):
    instance = CountryManager.objects.all()
    data = AllCountriesSerializer(instance, many=True).data
    return Response(data)

@api_view(['POST'])
def getCity(request):
    data = json.loads(request.body)
    get_id = data['country_id']

    instance = CityManagement.objects.filter(country__id=get_id)
    data = CitySerializer(instance, many=True).data

    return Response(data)
@api_view(['POST'])
def getzone(request):
    data = json.loads(request.body)
    get_id = data['country_id']

    instance = CityZone.objects.filter(city__id=get_id)
    data = ZoneSerializer(instance, many=True).data
    return Response(data)
