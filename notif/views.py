from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from notif.models import SupplierNotif, UserNotif, FarmTradeNotif, SupporterNotif
from notif.notifserializer import  NotifSerializer
from profils.models import UsersProfiles

####user
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def userNotif(request):
    get_id= UsersProfiles.objects.get(name=request.user)
    instance = UserNotif.objects.filter(name=get_id,read=False)
    for i in instance:
        i.read = True
        i.save()
    data = {}
    if instance:
        data = NotifSerializer(instance, many=True).data
    return Response(data)


##### suplier

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def supplierNotif(request):
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = SupplierNotif.objects.filter(trader=get_farm,read=False)
    for i in instance:
        i.read = True
        i.save()
    data = {}
    if instance:
        data = NotifSerializer(instance, many=True).data
    return Response(data)


##### Farm trade

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmTradeNotif(request):
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = FarmTradeNotif.objects.filter(trader=get_farm,read=False)
    for i in instance:
        i.read = True
        i.save()
    data = {}
    if instance:
        data = NotifSerializer(instance, many=True).data
    return Response(data)

# supporter

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def supporternotif(request):
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = SupporterNotif.objects.filter(trader=get_farm,read=False)
    for i in instance:
        i.read = True
        i.save()
    data = {}
    if instance:
        data = NotifSerializer(instance, many=True).data
    return Response(data)