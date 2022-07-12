from django.http import JsonResponse, HttpResponse
from rest_framework.authentication import TokenAuthentication
import json
import requests
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from profils.models import UsersProfiles, SupporterProfiles
from profils.profileserializer import SupporterSerializer
from support.models import FAQSupport, SupportContact, FarmMacth, FarmAdvice, FarmSupport, FarmFiles, FarmSupportAnswers
from support.supportserializer import FAQSerializer, AdvieceSerializer, SupportAnswerSerializer, SupportMatchSerializer, \
    SupportQuestSerializer, SupportPhotoSerializer

# user
from vegefarm.farmserializer import FarmGrowSerializer
from vegefarm.models import FarmGrow


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_FAQSupport(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    language = request.headers['Accept-language']
    section = request.query_params.get('section')
    faq = FAQSupport.objects.filter(faq_section=section, country=get_us.country)
    faq_data = FAQSerializer(faq, many=True, context={'lang': language}).data
    return Response(faq_data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_getSupport(request):
    try:
        get_us = UsersProfiles.objects.get(name=request.user)
        get_link = SupportContact.objects.get(country=get_us.country)
        return Response(get_link.contact_link)
    except:
        return Response("https://wa.me/+971586495751")


# farmer
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmSupporter(request):
    instance = SupporterProfiles.objects.all()
    data = {}
    if instance:
        data = SupporterSerializer(instance, many=True).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmMatch(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    get_id = request.POST.get('id')
    sup = SupporterProfiles.objects.get(id=get_id)
    FarmMacth.objects.create(supporter=sup, user=get_us)
    return JsonResponse('Done', safe=False)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmmakePayment(request):
    get_ur = UsersProfiles.objects.get(name=request.user)
    get_id = request.POST.get('id')
    sup = SupporterProfiles.objects.get(id=get_id)
    transaction_id = datetime.datetime.now().timestamp()
    FarmMacth.objects.create(supporter=sup, user=get_ur)

    country = get_ur.country
    url = 'https://secure-egypt.paytabs.com/payment/request'
    data = {"profile_id": "99273",
            "tran_type": "sale",
            "tran_class": "ecom",
            "cart_id": str(transaction_id),
            "cart_description": "Fresh Fruits and Vegetables",
            "cart_currency": 'USD',
            "cart_amount": float(sup.fees),
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
    print(x)

    return HttpResponse(x['redirect_url'])


# @api_view(['POST'])
# def paymrespone(request):
#     data = json.loads(request.body)
#     tran_ref = data['tran_ref']
#     tran_total = data['tran_total']
#     cart_id = data['cart_id']
#     payment_result = data['payment_result']['response_status']
#     order = Orders.objects.get(transaction_id=cart_id, status='CREATED')
#     if payment_result == 'A':
#         order.tran_ref = tran_ref
#         order.tran_total = tran_total
#         order.payment_result = payment_result
#         order.status = 'PAID'
#         order.save()
#     else:
#         order.tran_ref = tran_ref
#         order.tran_total = tran_total
#         order.payment_result = payment_result
#         order.status = 'FAIL'
#         order.save()
#
#     return HttpResponse(status=200)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_GetAdvice(request):
    gro = request.query_params.get('gro_id')
    get_gro = FarmGrow.objects.get(id=gro)
    language = request.headers['Accept-language']
    instance = FarmAdvice.objects.filter(grow=get_gro)
    data = {}
    if instance:
        data = AdvieceSerializer(SupporterSerializer, many=True, context={'lang': language}).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmTicketSupport(request):
    subj = request.POST.get('subj')
    quest = request.POST.get('quest')
    file = request.FILES.get('file')
    get_us = UsersProfiles.objects.get(name=request.user)
    try:
        instance = FarmMacth.objects.get(user=get_us, action='ACTIVE')

        sup_crt = FarmSupport.objects.create(user=get_us, supporter=instance.supporter, subject=subj, question=quest)
        FarmFiles.objects.create(case=sup_crt, files=file)

        return JsonResponse('Done', safe=False)
    except:
        return JsonResponse('No Mentor Subscription', safe=False)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def farmTicketAnswer(request):
    get_us = UsersProfiles.objects.get(name=request.user)
    instance = FarmSupportAnswers.objects.filter(user=get_us)
    data = {}
    if instance:
        data = SupportAnswerSerializer(instance, many=True, ).data
    return Response(data)


# Supporter
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def supporterMatchList(request):
    get_s = SupporterProfiles.objects.get(name=request.user)
    instance = FarmMacth.objects.filter(supporter=get_s, action='ACTIVE')
    data = {}
    if instance:
        data = SupportMatchSerializer(instance, many=True, ).data
    return Response(data)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def supporterGrowList(request):
    language = request.headers['Accept-language']
    section = request.query_params.get('section')
    get_s = FarmMacth.objects.get(id=section)
    instance = FarmGrow.objects.filter(trader=get_s.user)
    data = {}
    if instance:
        data = FarmGrowSerializer(instance, many=True,context={'lang': language} ).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def addGrowAdvice(request):
    get_s = SupporterProfiles.objects.get(name=request.user)
    gr_id = request.POST.get('id')
    subj = request.POST.get('subj')
    advice = request.POST.get('advice')

    get_gr = FarmGrow.objects.get(id=gr_id)
    FarmAdvice.objects.create(user=get_gr.trader,supporter=get_s,trader=get_s.user,subject=subj,advice=advice)

    return JsonResponse('Advice Added', safe=False)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def supporterFarmSupport(request):
    get_s = SupporterProfiles.objects.get(name=request.user)
    instance = FarmSupport.objects.filter(supporter=get_s)
    data = {}
    if instance:
        data = SupportQuestSerializer(instance, many=True).data
    return Response(data)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def supporterFarmSupportPhoto(request):
    section = request.query_params.get('section')
    get_s = FarmSupport.objects.get(id=section)
    instance = FarmFiles.objects.filter(case=get_s)
    data = {}
    if instance:
        data = SupportPhotoSerializer(instance, many=True).data
    return Response(data)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def supporterAnswerFarmSupport(request):
    get_s = SupporterProfiles.objects.get(name=request.user)
    gr_id = request.POST.get('id')
    answer = request.POST.get('answer')
    get_c = FarmSupport.objects.get(id=gr_id)
    get_c.status = 'CLOSED'
    get_c.save()
    FarmSupportAnswers.objects.create(supporter=get_s,user=get_c.user,case=get_c,
                                                 answer=answer,reply=True)

    return JsonResponse('Answer Added', safe=False)