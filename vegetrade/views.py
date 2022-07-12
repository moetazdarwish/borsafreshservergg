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
from vegetrade.models import *
from vegetrade.traderserializer import *


#########User
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_MarketFilter(request):
    sub = request.query_params.get('section')
    language = request.headers['Accept-language']
    location = request.headers['location']
    try:
        get_zone = CityZone.objects.get(id=location)
        today = datetime.datetime.now().date()
        get_sub = CategoryList.objects.get(id=sub)
        instance = SellingProducts.objects.filter(zone=get_zone, product__category=get_sub,
                                                  inv_due_date__gte=today, inventory__gt=0)
        data = {}
        if instance:
            data = SellingProductsSerializer(instance, many=True, context={'lang': language}).data
        return Response(data)
    except:
        return Response("No Stock in Area")


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_BoxFilter(request):
    today = datetime.datetime.now().date()
    sub = request.query_params.get('section')
    location = request.headers['location']
    try:
        get_zone = CityZone.objects.get(id=location)
        get_sub = CategoryList.objects.get(id=sub)
        instance = SellingBoxProducts.objects.filter(zone=get_zone, product__category=get_sub,
                                                     inv_due_date__gte=today, inventory__gt=0)
        data = {}
        if instance:
            data = UserBoxSerializer(instance, many=True).data
        return Response(data)
    except:
        return Response("No Stock in Area")


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_BoxContainFilter(request):
    Pro_Id = request.query_params.get('Pro_Id')
    language = request.headers['Accept-language']
    get_id = SellingBoxProducts.objects.get(id=Pro_Id)
    instance = MixedBox.objects.filter(box=get_id.box)
    data = {}
    if instance:
        data = MixedProductsSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_BulkMarketFilter(request):

    sub = request.query_params.get('section')
    language = request.headers['Accept-language']
    location = request.headers['location']
    try:
        get_zone = CityZone.objects.get(id=location)
        today = datetime.datetime.now().date()
        get_sub = CategoryList.objects.get(id=sub)
        instance = SellingBulkProducts.objects.filter(zone=get_zone, product__category=get_sub,
                                                      inv_due_date__gte=today, inventory__gt=0)
        data = {}
        if instance:
            data = SellingBulkProductsSerializer(instance, many=True, context={'lang': language}).data
        return Response(data)
    except:
        return Response("No Stock in Area")


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_MixedMarketFilter(request):

    sub = request.query_params.get('section')
    language = request.headers['Accept-language']
    location = request.headers['location']
    try:
        get_zone = CityZone.objects.get(id=location)
        today = datetime.datetime.now().date()
        get_sub = CategoryProducts.objects.get(id=sub)
        instance = SellingMixedProducts.objects.filter(zone=get_zone, product=get_sub,
                                                       inv_due_date__gte=today, inventory__gt=0)

        data = {}
        if instance:
            data = SellingMixedProductsSerializer(instance, many=True).data
        return Response(data)
    except:
        return Response("No Stock in Area")


#########Trader

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiProductCateg(request):
    get_ur = UsersProfiles.objects.get(name=request.user)
    sub = request.query_params.get('section')
    language = request.headers['Accept-language']
    instance = CategoryProducts.objects.filter(category=sub, country=get_ur.country)
    data = {}
    if instance:
        data = CategoryProductsSerializer(instance, many=True, context={"lang": language}).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiSubmitoffer(request):
    get_farm = UsersProfiles.objects.get(name=request.user)
    today = datetime.datetime.now().date()
    cat_id = request.POST.get('id')
    quantity = request.POST.get('quantity')
    scale = request.POST.get('group')
    price = decimal.Decimal(request.POST.get('price'))
    get_date = int(request.POST.get('date'))
    cat = CategoryProducts.objects.get(id=cat_id)
    new_date = today + datetime.timedelta(get_date)
    new, create = Products.objects.get_or_create(trader=get_farm, product=cat)
    new.price = price
    new.symbl = get_farm.symbl
    new.inventory = quantity
    new.inv_due_date = new_date
    new.scale = scale
    new.status = 'NEW'
    new.save()
    return Response("done")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiBoxoffer(request):
    get_trade = UsersProfiles.objects.get(name=request.user)
    today = datetime.datetime.now().date()
    cat_id = request.POST.get('id')
    boxname = request.POST.get('boxname')
    quantity = request.POST.get('quantity')
    price = decimal.Decimal(request.POST.get('price'))
    get_date = int(request.POST.get('date'))
    cat = CategoryProducts.objects.get(id=cat_id)
    new_date = today + datetime.timedelta(get_date)
    create = ProductsBox.objects.create(trader=get_trade, product=cat, price=price,
                                        symbl=get_trade.symbl, inventory=quantity,
                                        inv_due_date=new_date,

                                        box_name=boxname)
    return Response(create.id)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiBulkoffer(request):
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
    get, create = ProductsBulk.objects.get_or_create(trader=get_trade, product=cat)
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
def apiMixoffer(request):
    get_trade = UsersProfiles.objects.get(name=request.user)
    today = datetime.datetime.now().date()
    cat_id = request.POST.get('id')
    weight = decimal.Decimal(request.POST.get('weight'))
    scale = request.POST.get('group')
    quantity = request.POST.get('quantity')
    mname = request.POST.get('name')
    description = request.POST.get('describe')
    price = decimal.Decimal(request.POST.get('price'))
    get_date = int(request.POST.get('date'))
    cat = CategoryProducts.objects.get(id=cat_id)
    new_date = today + datetime.timedelta(get_date)
    ProductsMixed.objects.create(trader=get_trade, product=cat, price=price, symbl=get_trade.symbl,
                                 description=description, mix_name=mname,
                                 inventory=quantity, inv_due_date=new_date, scale=scale, weight=weight,
                                 status='NEW')

    return JsonResponse('Done', safe=False)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiAllItems(request):
    language = request.headers['Accept-language']
    get_usr = UsersProfiles.objects.get(name=request.user)
    instance = CategoryProducts.objects.filter(category__in=[1, 3, 2], country=get_usr.country)
    data = {}
    if instance:
        data = CategoryProductsSerializer(instance, many=True,context={'lang':language}).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiBoxitem(request):
    cat_id = request.POST.get('id')
    scale = request.POST.get('group')
    quantity = decimal.Decimal(request.POST.get('quantity'))
    box = request.POST.get('box')
    get_box = ProductsBox.objects.get(id=box)
    get_cat = CategoryProducts.objects.get(id=cat_id)
    MixedBox.objects.create(box=get_box, items=get_cat, scale=scale, weight=quantity)
    return Response('done')


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiBoxDetails(request):
    sub = request.POST.get('box_id')
    instance = ProductsBox.objects.get(id=sub)
    data = {}
    if instance:
        data = BoxSerializer(instance).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiBoxRemoveitem(request):
    sub = request.POST.get('box_id')
    MixedBox.objects.get(id=sub).delete()
    return Response("done")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiBoxRemove(request):
    sub = request.POST.get('box_id')
    ProductsBox.objects.get(id=sub).delete()
    return Response("done")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiRemove(request):
    sub = request.POST.get('box_id')
    item = request.POST.get('item')
    if item == 'single':
        Products.objects.get(id=sub).delete()
        return Response("Item Removed")
    if item == 'mix':
        ProductsBox.objects.get(id=sub).delete()
        return Response("Item Removed")
    if item == 'bulk':
        ProductsBulk.objects.get(id=sub).delete()
        return Response("Item Removed")
    if item == 'salad':
        ProductsMixed.objects.get(id=sub).delete()
        return Response("Item Removed")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiBoxPublish(request):
    sub = request.POST.get('box_id')
    get_box = ProductsBox.objects.get(id=sub)
    get_box.status = 'NEW'
    get_box.save()
    return Response("done")


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiItemsSubmitedList(request):
    language = request.headers['Accept-language']
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = Products.objects.filter(trader=get_farm)
    data = {}
    if instance:
        data = SubmitedItemsFilterSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiBoxesSubmitedList(request):
    language = request.headers['Accept-language']
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = ProductsBox.objects.filter(trader=get_farm)
    data = {}
    if instance:
        data = SubmitedBoxesFilterSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiBulkSubmitedList(request):
    language = request.headers['Accept-language']
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = ProductsBulk.objects.filter(trader=get_farm)
    data = {}
    if instance:
        data = SubmitedBulkFilterSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiMixedSubmitedList(request):
    language = request.headers['Accept-language']
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = ProductsMixed.objects.filter(trader=get_farm)
    data = {}
    if instance:
        data = SubmitedMixedFilterSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)
