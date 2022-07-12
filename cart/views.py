from django.db.models import Q
import requests
import json
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from cart.cartserializer import OrderProductsSerializer, OrderSerializer, AllOrdersSerializer
from cart.models import Orders, OrderProduct
from countrymgt.models import CityZone
from profils.models import UsersProfiles
from vegefarm.models import FarmSellingProducts, FarmProducts, SellingFarmBulkProducts, FarmProductsBulk
from vegetrade.models import SellingProducts, Products, ProductsBox, SellingBoxProducts, SellingBulkProducts, \
    ProductsBulk, SellingMixedProducts, ProductsMixed
import datetime


# Create your views here.


######## user


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_cart(request):
    language = request.headers['Accept-language']
    get_us = UsersProfiles.objects.get(name=request.user)
    try:
        order = Orders.objects.get(name=get_us, status='CREATED')
        instance = order.orderproduct_set.all()
        data = OrderProductsSerializer(instance, many=True, context={'lang': language}).data
        return Response(data)
    except:
        return Response('No item Purchased')


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_cartTotal(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    try:
        order = Orders.objects.get(name=get_us, status='CREATED')

        order_data = OrderSerializer(order).data
        return Response(order_data)
    except:
        return Response('No item Purchased')


@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def apiCartActionProduct(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    productID = request.POST.get('item_id')
    action = request.POST.get('action')
    location = request.headers['location']
    get_zone = CityZone.objects.get(id=location)
    if action == 'add':
        get_product = SellingProducts.objects.get(id=productID)
        order, created = Orders.objects.get_or_create(name=get_us, symbl=get_zone.country.symbl, status='CREATED')
        orderitem, ordercreated = OrderProduct.objects.get_or_create(order=order, trader=get_product.supplier.trader,
                                                                     symbl=get_zone.country.symbl,
                                                                     product=get_product.product,
                                                                     supplier=get_product.supplier,
                                                                     buy_price=get_product.selling_price,
                                                                     scale=get_product.supplier.scale,
                                                                     supplier_price=get_product.supplier_rev,
                                                                     zone=get_zone)
        if get_product.inventory == 0:
            return JsonResponse('Stock Finish', safe=False)
        else:
            orderitem.quantity = (orderitem.quantity + 1)
            get_product.inventory = get_product.inventory - 1
            orderitem.save()
            get_product.save()
            return JsonResponse('Item Add', safe=False)


@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def apiCartActionFarm(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    productID = request.POST.get('item_id')
    get_product = FarmSellingProducts.objects.get(id=productID)
    location = request.headers['location']
    get_zone = CityZone.objects.get(id=location)
    order, created = Orders.objects.get_or_create(name=get_us, status='CREATED', symbl=get_zone.country.symbl,
                                                  zone=get_zone)
    orderitem, ordercreated = OrderProduct.objects.get_or_create(order=order, trader=get_product.supplier.trader,
                                                                 symbl=get_zone.country.symbl,
                                                                 product=get_product.product,
                                                                 supplier=get_product.supplier,
                                                                 buy_price=get_product.selling_price,
                                                                 scale=get_product.supplier.scale, hydro=True,
                                                                 supplier_price=get_product.supplier_rev,
                                                                 farm_item=get_product, zone=get_zone)

    if get_product.inventory == 0:
        return JsonResponse('Stock Finish', safe=False)
    else:
        orderitem.quantity = (orderitem.quantity + 1)
        get_product.inventory = get_product.inventory - 1
        orderitem.save()
        get_product.save()
        return JsonResponse('Item Add', safe=False)


@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def apiCartActionBox(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    productID = request.POST.get('item_id')
    action = request.POST.get('action')
    location = request.headers['location']
    get_zone = CityZone.objects.get(id=location)
    get_product = SellingBoxProducts.objects.get(id=productID)
    if action == 'add':
        order, created = Orders.objects.get_or_create(name=get_us, status='CREATED', symbl=get_zone.country.symbl,
                                                      zone=get_zone)
        orderitem, ordercreated = OrderProduct.objects.get_or_create(order=order, trader=get_product.box.trader,
                                                                     symbl=get_zone.country.symbl,
                                                                     product=get_product.product,
                                                                     box_supplier=get_product.box,
                                                                     buy_price=get_product.selling_price,
                                                                     box_name=get_product.box.box_name, zone=get_zone,
                                                                     is_box=True,
                                                                     supplier_price=get_product.supplier_rev,
                                                                     box_market=get_product)
        if get_product.inventory == 0:
            return JsonResponse('Stock Finish', safe=False)
        else:
            orderitem.quantity = (orderitem.quantity + 1)
            get_product.inventory = get_product.inventory - 1
            orderitem.save()
            get_product.save()
            return JsonResponse('Item Add', safe=False)


@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def apiCartAddBulk(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    productID = request.POST.get('item_id')
    action = request.POST.get('action')
    location = request.headers['location']
    get_zone = CityZone.objects.get(id=location)
    if action == 'add':
        get_product = SellingBulkProducts.objects.get(id=productID)
        order, created = Orders.objects.get_or_create(name=get_us, symbl=get_zone.country.symbl, status='CREATED')
        orderitem, ordercreated = OrderProduct.objects.get_or_create(order=order, trader=get_product.supplier.trader,
                                                                     symbl=get_zone.country.symbl,
                                                                     product=get_product.product,
                                                                     bulk_supplier=get_product.supplier,
                                                                     buy_price=get_product.selling_price,
                                                                     scale=get_product.supplier.scale,
                                                                     weight=get_product.supplier.weight, is_bulk=True,
                                                                     supplier_price=get_product.supplier_rev,
                                                                     zone=get_zone, bulk_market=get_product)
        if get_product.inventory == 0:
            return JsonResponse('Stock Finish', safe=False)
        else:
            orderitem.quantity = (orderitem.quantity + 1)
            get_product.inventory = get_product.inventory - 1
            orderitem.save()
            get_product.save()
            return JsonResponse('Item Add', safe=False)


@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def apiCartAddMix(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    productID = request.POST.get('item_id')
    action = request.POST.get('action')
    location = request.headers['location']
    get_zone = CityZone.objects.get(id=location)
    if action == 'add':
        get_product = SellingMixedProducts.objects.get(id=productID)
        order, created = Orders.objects.get_or_create(name=get_us, symbl=get_zone.country.symbl, status='CREATED')
        orderitem, ordercreated = OrderProduct.objects.get_or_create(order=order, trader=get_product.supplier.trader,
                                                                     symbl=get_zone.country.symbl,
                                                                     product=get_product.product,
                                                                     mix_supplier=get_product.supplier,
                                                                     buy_price=get_product.selling_price,
                                                                     scale=get_product.supplier.scale,
                                                                     weight=get_product.supplier.weight, is_mix=True,
                                                                     supplier_price=get_product.supplier_rev,
                                                                     zone=get_zone, mix_market=get_product)
        if get_product.inventory == 0:
            return JsonResponse('Stock Finish', safe=False)
        else:
            orderitem.quantity = (orderitem.quantity + 1)
            get_product.inventory = get_product.inventory - 1
            orderitem.save()
            get_product.save()
            return JsonResponse('Item Add', safe=False)


@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def apiFarmAddBulk(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    productID = request.POST.get('item_id')
    location = request.headers['location']
    get_zone = CityZone.objects.get(id=location)

    get_product = SellingFarmBulkProducts.objects.get(id=productID)
    order, created = Orders.objects.get_or_create(name=get_us, symbl=get_zone.country.symbl, status='CREATED')
    orderitem, ordercreated = OrderProduct.objects.get_or_create(order=order, trader=get_product.supplier.trader,
                                                                 symbl=get_zone.country.symbl,
                                                                 product=get_product.product,
                                                                 bulk_farm_supplier=get_product.supplier,
                                                                 buy_price=get_product.selling_price,
                                                                 scale=get_product.supplier.scale,
                                                                 weight=get_product.supplier.weight, is_farm_bulk=True,
                                                                 supplier_price=get_product.supplier_rev, zone=get_zone,
                                                                 bulk_farm=get_product)
    if get_product.inventory == 0:
        return JsonResponse('Stock Finish', safe=False)
    else:
        orderitem.quantity = (orderitem.quantity + 1)
        get_product.inventory = get_product.inventory - 1
        orderitem.save()
        get_product.save()
        return JsonResponse('Item Add', safe=False)


@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def apiCartAction(request):
    productID = request.POST.get('item_id')
    action = request.POST.get('action')
    if action == 'add':
        get_OrderProduct = OrderProduct.objects.get(id=productID)
        if get_OrderProduct.is_box:
            get_product = SellingBoxProducts.objects.get(orderproduct=get_OrderProduct)
            if get_product.inventory == 0:
                return JsonResponse('Stock Finish', safe=False)
            else:
                get_OrderProduct.quantity = (get_OrderProduct.quantity + 1)
                get_product.inventory = get_product.inventory - 1
                get_OrderProduct.save()
                get_product.save()
                return JsonResponse('Item Add', safe=False)
        elif get_OrderProduct.is_bulk:
            get_product = SellingBulkProducts.objects.get(orderproduct=get_OrderProduct)
            if get_product.inventory == 0:
                return JsonResponse('Stock Finish', safe=False)
            else:
                get_OrderProduct.quantity = (get_OrderProduct.quantity + 1)
                get_product.inventory = get_product.inventory - 1
                get_OrderProduct.save()
                get_product.save()
                return JsonResponse('Item Add', safe=False)
        elif get_OrderProduct.is_mix:
            get_product = SellingMixedProducts.objects.get(orderproduct=get_OrderProduct)
            if get_product.inventory == 0:
                return JsonResponse('Stock Finish', safe=False)
            else:
                get_OrderProduct.quantity = (get_OrderProduct.quantity + 1)
                get_product.inventory = get_product.inventory - 1
                get_OrderProduct.save()
                get_product.save()
                return JsonResponse('Item Add', safe=False)
        elif get_OrderProduct.is_farm_bulk:
            get_product = FarmProductsBulk.objects.get(orderproduct=get_OrderProduct)
            if get_product.inventory == 0:
                return JsonResponse('Stock Finish', safe=False)
            else:
                get_OrderProduct.quantity = (get_OrderProduct.quantity + 1)
                get_product.inventory = get_product.inventory - 1
                get_product.status = 'UPDATE'
                get_OrderProduct.save()
                get_product.save()
                return JsonResponse('Item Add', safe=False)
        elif get_OrderProduct.hydro:
            get_product = FarmProducts.objects.get(orderproduct=get_OrderProduct)
            if get_product.inventory == 0:
                return JsonResponse('Stock Finish', safe=False)
            else:
                get_OrderProduct.quantity = (get_OrderProduct.quantity + 1)
                get_OrderProduct.price = get_product
                get_product.inventory = get_product.inventory - 1
                get_product.status = 'UPDATE'
                get_OrderProduct.save()
                get_product.save()
                return JsonResponse('Item Add', safe=False)
        else:
            get_product = SellingProducts.objects.get(orderproduct=get_OrderProduct)
            if get_product.inventory == 0:
                return JsonResponse('Stock Finish', safe=False)
            else:
                get_OrderProduct.quantity = (get_OrderProduct.quantity + 1)
                get_product.inventory = get_product.inventory - 1
                get_OrderProduct.save()
                get_product.save()
                return JsonResponse('Item Add', safe=False)
    elif action == 'remove':
        orderitem = OrderProduct.objects.get(id=productID)
        if orderitem.is_box:
            orderitem.quantity = (orderitem.quantity - 1)
            get_sup = SellingBoxProducts.objects.get(orderproduct=orderitem)
            get_sup.inventory = get_sup.inventory + 1
            orderitem.save()
            get_sup.save()
            if orderitem.quantity <= 0:
                orderitem.delete()
            return JsonResponse('Item Removed', safe=False)
        elif orderitem.is_bulk:
            get_product = SellingBulkProducts.objects.get(orderproduct=orderitem)
            orderitem.quantity = (orderitem.quantity - 1)
            get_product.inventory = get_product.inventory + 1
            orderitem.save()
            get_product.save()
            if orderitem.quantity <= 0:
                orderitem.delete()
            return JsonResponse('Item Removed', safe=False)
        elif orderitem.is_mix:
            get_product = SellingMixedProducts.objects.get(orderproduct=orderitem)
            orderitem.quantity = (orderitem.quantity - 1)
            get_product.inventory = get_product.inventory + 1
            orderitem.save()
            get_product.save()
            if orderitem.quantity <= 0:
                orderitem.delete()
            return JsonResponse('Item Removed', safe=False)
        elif orderitem.is_farm_bulk:
            get_product = SellingFarmBulkProducts.objects.get(orderproduct=orderitem)
            if get_product.inventory == 0:
                return JsonResponse('Stock Finish', safe=False)
            else:
                orderitem.quantity = (orderitem.quantity - 1)
                get_product.inventory = get_product.inventory + 1
                orderitem.save()
                get_product.save()
                return JsonResponse('Item Removed', safe=False)
        elif orderitem.hydro:
            orderitem.quantity = (orderitem.quantity - 1)
            get_product = FarmSellingProducts.objects.get(orderproduct=orderitem)
            get_product.inventory = get_product.inventory + 1
            orderitem.save()
            get_product.save()
            if orderitem.quantity <= 0:
                orderitem.delete()
            return JsonResponse('Item Removed', safe=False)
        else:
            orderitem.quantity = (orderitem.quantity - 1)
            get_product = SellingProducts.objects.get(orderproduct=orderitem)
            get_product.inventory = get_product.inventory + 1
            orderitem.save()
            get_product.save()
            if orderitem.quantity <= 0:
                orderitem.delete()
            return JsonResponse('Item Removed', safe=False)


@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def apiAddNote(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    note = request.POST.get('new_note')
    created = Orders.objects.get(name=get_us, status='CREATED')
    created.note = note
    created.save()
    return Response('Note Added ')


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def cancelOrder(request):
    get_id = request.POST.get('order_id')
    get_order = Orders.objects.get(id=get_id)
    get_order.status = 'CANCELLED'
    get_order.save()
    return JsonResponse('Order Cancelled', safe=False)


####### supplier

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiOrdersList(request):
    language = request.headers['Accept-language']
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = OrderProduct.objects.filter(trader=get_farm, status='CONFIRMED')
    data = {}
    if instance:
        data = AllOrdersSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiConfirmProcess(request):
    get_id = request.POST.get('id')
    status = request.POST.get('status')
    get_order = OrderProduct.objects.get(id=get_id)
    get_order.status = status
    get_order.save()
    return Response("Order " + status)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiOrdersProcessing(request):
    language = request.headers['Accept-language']
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = OrderProduct.objects.filter(trader=get_farm, status__in=['ACCEPT', 'RESCHEDULE'])
    data = {}
    if instance:
        data = AllOrdersSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiOrdersDeliveryStats(request):
    language = request.headers['Accept-language']
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = OrderProduct.objects.filter(trader=get_farm, status='DELIVERY OUT')
    data = {}
    if instance:
        data = AllOrdersSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiOrdersAll(request):
    language = request.headers['Accept-language']
    get_farm = UsersProfiles.objects.get(name=request.user)
    instance = OrderProduct.objects.filter(~Q(status='CREATED'), trader=get_farm, )
    data = {}
    if instance:
        data = AllOrdersSerializer(instance, many=True, context={'lang': language}).data
    return Response(data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def makePayment(request):
    get_ur = UsersProfiles.objects.get(name=request.user)
    order = Orders.objects.get(name=get_ur, status='CREATED')
    country = get_ur.country
    url = 'https://secure-egypt.paytabs.com/payment/request'
    data = {"profile_id": "99273",
            "tran_type": "sale",
            "tran_class": "ecom",
            "cart_id": str(order.transaction_id),
            "cart_description": "Fresh Fruits and Vegetables",
            "cart_currency": order.symbl,
            "cart_amount": float(order.get_cart_total),
            "hide_shipping": True,
            "callback": "https://f0dd-102-44-160-143.ngrok.io/cart/paymrespone/",
            "return": "/success",
            "customer_details": {
                "name": get_ur.name.get_full_name(),
                "email": get_ur.name.email,
                "street1": get_ur.address,
                "city": get_ur.city,
                "state": country[:2],
                "country": country[:2]
                # "ip": "91.74.146.168"
            }}
    r = requests.post(url, headers={
        "authorization": 'SBJNGGRN6J-JDNRH9H9BW-WZT6NGLDHZ',
        "content-type": 'application/json'
    }, data=json.dumps(data),
                      )
    x = r.json()
    return HttpResponse(x['redirect_url'])


@api_view(['POST'])
def paymrespone(request):
    data = json.loads(request.body)
    tran_ref = data['tran_ref']
    tran_total = data['tran_total']
    cart_id = data['cart_id']
    payment_result = data['payment_result']['response_status']
    order = Orders.objects.get(transaction_id=cart_id, status='CREATED')
    if payment_result == 'A':
        order.tran_ref = tran_ref
        order.tran_total = tran_total
        order.payment_result = payment_result
        order.status = 'PAID'
        order.save()
    else:
        order.tran_ref = tran_ref
        order.tran_total = tran_total
        order.payment_result = payment_result
        order.status = 'FAIL'
        order.save()

    return HttpResponse(status=200)

