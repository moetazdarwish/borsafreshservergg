from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from admanager.admanagerserializer import AdManagerSerializer
from admanager.models import Advertesing, AdCounter
from profils.models import UsersProfiles


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def getads(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    instance = Advertesing.objects.filter(country=get_us.country)
    data = {}
    if instance:
        data = AdManagerSerializer(instance, many=True).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def getadslink(request):
    ad_id = request.POST.get('id')
    get_us = UsersProfiles.objects.get(name=request.user)
    instance = Advertesing.objects.get(id=ad_id)
    AdCounter.objects.create(user=get_us, ad=instance)

    return JsonResponse(instance.link, safe=False)
