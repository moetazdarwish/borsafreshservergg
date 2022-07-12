from django.db.models import Q
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from cart.models import Orders, OrderProduct
from profils.models import UsersProfiles
from tracker.models import OrderTracking, SubOrderReview
from tracker.trackerserializer import UserTrackingSerializer, UserTrackSubOrderSerializer, UserOrderTrackingSerializer


# User

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def userOrderTracking(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    get_track = Orders.objects.filter(name=get_us,status='PAID')
    data = {}
    if get_track:
        data = UserOrderTrackingSerializer(get_track, many=True).data
    return Response(data)
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def userTracking(request):
    order_id = request.POST.get('order_id')
    get_us = Orders.objects.get(id=order_id)
    get_track = OrderTracking.objects.filter(order=get_us)
    data = {}
    if get_track:
        data = UserTrackingSerializer(get_track, many=True).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def userSubOrderTracking(request):
    language = request.headers['Accept-language']
    order_id = request.POST.get('order_id')
    get_order = Orders.objects.get(id=order_id)
    instance = OrderProduct.objects.filter(order=get_order)
    data = {}
    if instance:
        data = UserTrackSubOrderSerializer(instance, many=True,context={"lang": language}).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def userSubOrderReview(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    order_id = request.POST.get('order_id')
    rate = request.POST.get('rate')
    review = request.POST.get('review')
    print(rate)
    if rate :
        get_order = OrderProduct.objects.get(id=order_id)
        get, create = SubOrderReview.objects.get_or_create(name=get_us, sub_order=get_order, )
        get.rate = rate
        get.save()
        return JsonResponse('Thank you For Your Review', safe=False)
    else:
        print(review)
        get_order = OrderProduct.objects.get(id=order_id)
        get , create = SubOrderReview.objects.get_or_create(name=get_us, sub_order=get_order,)
        get.review = review
        get.save()
        return JsonResponse('Thank you For Your Review', safe=False)
