from django.db.models import Q
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
import decimal
import datetime

from countrymgt.models import CityZone
from profils.models import UsersProfiles

# Create your views here.
#########User
from vegefarm.farmserializer import SellingFarmProductsSerializer, SellingBulkFarmSerializer, \
    FarmSubmitedItemsSerializer, FarmSubmitedBulkSerializer, FarmGrowSerializer
from vegefarm.models import FarmSellingProducts, SellingFarmBulkProducts, FarmProducts, FarmProductsBulk, FarmGrow
from vegetrade.models import CategoryProducts, CategoryList
from vegetrade.traderserializer import CategoryProductsSerializer


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_FarmMarketFilter(request):

    sub = request.query_params.get('section')
    language = request.headers['Accept-language']
    location = request.headers['location']
    try:
        get_zone = CityZone.objects.get(id=location)
        today = datetime.datetime.now().date()
        get_sub = CategoryList.objects.get(id=sub)
        instance = FarmSellingProducts.objects.filter(zone=get_zone,product__category=get_sub,
                                                  inv_due_date__gte=today,inventory__gt=0)
        data = {}
        if instance:
            data=SellingFarmProductsSerializer(instance, many=True, context={'lang': language}).data
        return Response(data)
    except:
        pass
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_BulkFarmFilter(request):
    sub = request.query_params.get('section')
    language = request.headers['Accept-language']
    location = request.headers['location']
    try:
        get_zone = CityZone.objects.get(id=location)
        today = datetime.datetime.now().date()
        get_sub = CategoryList.objects.get(id=sub)
        instance = SellingFarmBulkProducts.objects.filter(zone=get_zone, product__category=get_sub,
                                                          inv_due_date__gte=today,inventory__gt=0)
        data = {}
        if instance:
            data = SellingBulkFarmSerializer(instance, many=True, context={'lang': language}).data
        return Response(data)
    except:
        pass

#########Farm Trade

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmProductCateg(request):
    get_ur = UsersProfiles.objects.get(name=request.user)
    sub = request.query_params.get('section')
    language = request.headers['Accept-language']
    instance = CategoryProducts.objects.filter(category=sub, country=get_ur.country)
    print(instance)
    data = {}
    if instance:
        data = CategoryProductsSerializer(instance, many=True, context={"lang": language}).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmSubmitoffer(request):
    get_farm = UsersProfiles.objects.get(name=request.user)
    today = datetime.datetime.now().date()
    cat_id = request.POST.get('id')
    quantity = request.POST.get('quantity')
    scale = request.POST.get('group')
    price = decimal.Decimal(request.POST.get('price'))
    get_date = int(request.POST.get('date'))
    cat = CategoryProducts.objects.get(id=cat_id)
    new_date = today + datetime.timedelta(get_date)
    new, create = FarmProducts.objects.get_or_create(trader=get_farm, product=cat)
    new.price = price
    new.symbl = get_farm.symbl
    new.inventory = quantity
    new.inv_due_date = new_date
    new.scale = scale
    new.status = 'NEW'
    new.save()
    return Response("Done")
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmBulkoffer(request):
    get_trade = UsersProfiles.objects.get(name=request.user)
    today = datetime.datetime.now().date()
    cat_id = request.POST.get('id')
    weight = decimal.Decimal(request.POST.get('weight'))
    scale = request.POST.get('group')
    quantity = request.POST.get('quantity')
    price = decimal.Decimal(request.POST.get('price'))
    get_date = int(request.POST.get('date'))
    cat = CategoryProducts.objects.get(id=cat_id)
    new_date = today + datetime.timedelta(get_date)
    get, create = FarmProductsBulk.objects.get_or_create(trader=get_trade, product=cat)
    get.price = price
    get.symbl = get_trade.symbl
    get.inventory = quantity
    get.inv_due_date = new_date
    get.scale = scale
    get.weight = weight
    get.status = 'NEW'
    get.save()
    return JsonResponse('Done', safe=False)
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmRemove(request):
    sub = request.POST.get('box_id')
    item = request.POST.get('item')
    if item == 'single':
        FarmProducts.objects.get(id=sub).delete()
        return Response("Item Removed")

    if item == 'bulk':
        FarmProductsBulk.objects.get(id=sub).delete()
        return Response("Item Removed")

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmItemsSubmitedList(request):
    language = request.headers['Accept-language']
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = FarmProducts.objects.filter(trader=get_farm)
    data = {}
    if instance:
        data = FarmSubmitedItemsSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmBulkSubmitedList(request):
    language = request.headers['Accept-language']
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = FarmProductsBulk.objects.filter(trader=get_farm)
    data = {}
    if instance:
        data = FarmSubmitedBulkSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)

# farm growing
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def createGrow(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    cat_id = request.POST.get('id')
    quantity = request.POST.get('quantity')
    system = request.POST.get('system')

    get_cat = CategoryProducts.objects.get(id=cat_id)
    FarmGrow.objects.create(trader=get_us,product=get_cat,quantity=quantity,system=system,
                            city=get_us.city,country=get_us.country)


    return JsonResponse('Done', safe=False)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmGrowList(request):
    language = request.headers['Accept-language']
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = FarmGrow.objects.filter(trader=get_farm)
    data = {}
    if instance:
        data = FarmGrowSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)