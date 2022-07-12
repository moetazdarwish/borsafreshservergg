from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from ipregistry import IpregistryClient
import json
import datetime
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
# Create your views here.


# from countrymgt.countryserilazer import CountryAppConstSerializer
######## User
from countrymgt.models import CountryManager, CityManagement, CityZone, NewZone
from profils.forms import CreateUser, LoginForm
from profils.models import UsersProfiles, TraderTransData, ProfilesZone, ProfilesMSG
from profils.profileserializer import USERPROFILESerializer, TraderTransDataSerializer, LogininSerializer, MSGSerializer


#### user
@api_view(['POST'])
def create_auth(request):
    country = request.POST.get('country')
    city = request.POST.get('city')
    email = request.POST.get('email')
    password = request.POST.get('password')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    address = request.POST.get('address')
    area = request.POST.get('area')
    phone = request.POST.get('phone')
    latitude = request.query_params.get('latitude')
    longitude = request.query_params.get('longitude')
    data = {
        'first_name': fname,
        'last_name': lname,
        'email': email,
        'username': email,
        'password1': password,
        'password2': password,
    }
    form = CreateUser(data)
    if form.is_valid():
        user = form.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        UsersProfiles.objects.create(name=user, phone=phone, address=address,
                                     area=area, country=country, city=city, lat=latitude, long=longitude)
        token = Token.objects.get(user=user)
        get_user = User.objects.get(username=email)
        name = get_user.get_full_name()
        data = {"key": token.key,
                "name": name}
        json_stuff = LogininSerializer(data).data
        return Response(json_stuff)
    else:
        return JsonResponse(form.errors)


@api_view(['POST'])
def login_auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        get_user = User.objects.get(username=user)
        token, create = Token.objects.get_or_create(user=get_user)
        name = get_user.get_full_name()
        key = token.key
        data = {"key": key,
                "name": name}
        json_stuff = LogininSerializer(data).data
        return Response(json_stuff)
    else:
        return Response('Wrong Password or Email')

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_EditProfile(request):
    get_profile = UsersProfiles.objects.get(name=request.user)
    address = request.POST.get('address')
    postal = request.POST.get('postal')
    area = request.POST.get('area')
    phone = request.POST.get('phone')
    get_profile.address = address
    get_profile.phone = phone
    get_profile.postal_code = postal
    get_profile.area = area
    get_profile.save()
    return Response("done")


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def api_Profile(request):
    get_profile = UsersProfiles.objects.get(name=request.user)
    profile_data = USERPROFILESerializer(get_profile).data
    return Response(profile_data)


####### Suppliers

@api_view(['POST'])
def create_Tradeauth(request):
    latitude = request.query_params.get('latitude')
    longitude = request.query_params.get('longitude')
    country = request.POST.get('country')
    city = request.POST.get('city')
    # currency = ipInfo.currency["code"]
    email = request.POST.get('email')
    password = request.POST.get('password')
    fname = request.POST.get('fname')
    tradename = request.POST.get('tradename')
    lname = request.POST.get('lname')
    address = request.POST.get('address')
    area = request.POST.get('area')
    phone = request.POST.get('phone')
    data = {
        'first_name': fname,
        'last_name': lname,
        'email': email,
        'username': email,
        'password1': password,
        'password2': password,
    }
    form = CreateUser(data)
    if form.is_valid():
        user = form.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        get_user = User.objects.get(username=email)
        get_prof = UsersProfiles.objects.create(name=get_user, phone=phone, address=address,
                                                 area=area, country=country, city=city,
                                                trader_name=tradename,
                                                is_trader=True, lat=latitude, long=longitude)
        token, create = Token.objects.get_or_create(user=get_user)
        name = get_user.get_full_name()
        key = token.key
        data = {"key": key,
                "name": name, }
        json_stuff = LogininSerializer(data).data
        try:
            get_zone = CityZone.objects.get(lat_greater__lte=latitude, lat_lower__gte=latitude, long_greater__lte=longitude,
                                            long_lower__gte=longitude)
            ProfilesZone.objects.create(user=get_prof, zone=get_zone)
            get_prof.symbl =get_zone.country.symbl
            get_prof.approve = True
            get_prof.save()
            return Response(json_stuff)
        except:
            NewZone.objects.create(lat=latitude, long=longitude,is_trader=True)
            ProfilesMSG.objects.create(user=get_prof,msg='Out of Coverage Area , Please Contact Support Team',
                                       smal_msg='Please Contact Support Team')
            return Response(json_stuff)
    else:
        return JsonResponse(form.errors)

@api_view(['POST'])
def reg_Tradeauth(request):
    data = json.loads(request.body)
    password = data['psw']
    fname = data['fname']
    lname = data['lname']
    tradename = data['tname']
    email = data['mail']
    address = data['addrs']
    phone = data['phone']
    city = data['city']
    instance = CityManagement.objects.filter(id=city)


    listArray = data['listArray']

    data = {
        'first_name': fname,
        'last_name': lname,
        'email': email,
        'username': email,
        'password1': password,
        'password2': password,
    }
    form = CreateUser(data)
    if form.is_valid():
        user = form.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        get_user = User.objects.get(username=email)
        get_prof = UsersProfiles.objects.create(name=get_user, phone=phone, address=address,
                                                  country=instance.country.country, city=instance.city,symbl=instance.country.symbl,
                                                trader_name=tradename,
                                                is_trader=True)

        if listArray :
            for i in listArray:
                get_zone = CityZone.objects.get(id=i)
                ProfilesZone.objects.create(user=get_prof, zone=get_zone)
        return Response("Thank you , Our Team Will Contact you ")
    else:
        return JsonResponse(form.errors)
@api_view(['POST'])
def login_Traderauth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        get_user = User.objects.get(username=user)
        get_tradr = UsersProfiles.objects.get(name=get_user)
        if get_tradr.approve:
            token, create = Token.objects.get_or_create(user=get_user)
            name = get_user.get_full_name()
            key = token.key
            try:
                ProfilesZone.objects.create(user=get_tradr)
                data = {"key": key,
                                "name": get_tradr.trader_name,}
                json_stuff = LogininSerializer(data).data
                return Response(json_stuff)
            except:
                pass
        else:
            return Response('Trader Account Not Approved')
    else:
        return Response('Wrong Password or Email')

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def loginTokenChck(request):

    get_tradr = UsersProfiles.objects.get(name=request.user)
    try:
        get_msg = ProfilesMSG.objects.get(user=get_tradr,is_read=True)
        if get_msg.is_admin :
            data = {"auth": "false",
                    "msg": get_msg.msg,
                    "escape": get_msg.msg.smal_msg}
            resp = MSGSerializer(data).data

            return Response(resp)
        else:
            get_msg.is_read=False
            get_msg.save()
            data = {"auth": "false",
                    "msg": get_msg.msg,
                    "escape": get_msg.smal_msg}
            resp = MSGSerializer(data).data
            return Response(resp)
    except:
        data = {"auth": "true",
                "msg": "true",
                "escape": "true"}
        resp = MSGSerializer(data).data
        return Response(resp)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def supplierTransferData(request):
    get_u = UsersProfiles.objects.get(name=request.user)

    instance, create = TraderTransData.objects.get_or_create(benfec=get_u)
    data = {}
    if instance:
        data = TraderTransDataSerializer(instance, many=False).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def supplierTransferUpdate(request):
    get_u = UsersProfiles.objects.get(name=request.user)
    get_data = request.POST.get('data')
    instance, create = TraderTransData.objects.get_or_create(benfec=get_u)
    instance.new = get_data
    instance.change = True
    instance.save()

    return Response("done")


# reg_farmauth


@api_view(['POST'])
def reg_farmauth(request):
    data = json.loads(request.body)
    password = data['psw']
    fname = data['fname']
    lname = data['lname']
    tradename = data['tname']
    email = data['mail']
    address = data['addrs']
    phone = data['phone']
    city = data['city']
    listArray = data['listArray']
    instance = CityManagement.objects.filter(id=city)
    data = {
        'first_name': fname,
        'last_name': lname,
        'email': email,
        'username': email,
        'password1': password,
        'password2': password,
    }
    form = CreateUser(data)
    if form.is_valid():
        user = form.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        get_user = User.objects.get(username=email)
        get_prof = UsersProfiles.objects.create(name=get_user, phone=phone, address=address,
                                                  country=instance.country.country, city=instance.city,symbl=instance.country.symbl,
                                                trader_name=tradename,
                                                is_farm=True)

        if listArray :
            for i in listArray:
                get_zone = CityZone.objects.get(id=i)
                ProfilesZone.objects.create(user=get_prof, zone=get_zone)
        return Response("Thank you , Our Team Will Contact you ")
    else:
        return JsonResponse(form.errors)

# reg_farmauth app


@api_view(['POST'])
def reg_farmapp(request):
    data = json.loads(request.body)
    password = data['psw']
    fname = data['fname']
    lname = data['lname']
    tradename = data['tname']
    email = data['mail']
    address = data['addrs']
    phone = data['phone']
    city = data['city']
    instance = CityManagement.objects.filter(id=city)
    data = {
        'first_name': fname,
        'last_name': lname,
        'email': email,
        'username': email,
        'password1': password,
        'password2': password,
    }
    form = CreateUser(data)
    if form.is_valid():
        user = form.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        get_user = User.objects.get(username=email)
        UsersProfiles.objects.create(name=get_user, phone=phone, address=address,
                                                  country=instance.country.country, city=instance.city,symbl=instance.country.symbl,
                                                trader_name=tradename,
                                                is_farm=True)
        return Response("Thank you , Our Team Will Contact you ")
    else:
        return JsonResponse(form.errors)

@api_view(['POST'])
def login_FarmTrad(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        get_user = User.objects.get(username=user)
        get_tradr = UsersProfiles.objects.get(name=get_user)
        if get_tradr.approve:
            token, create = Token.objects.get_or_create(user=get_user)
            key = token.key
            try:

                data = {"key": key,
                                "name": get_tradr.trader_name,}
                json_stuff = LogininSerializer(data).data
                return Response(json_stuff)
            except:
                pass
        else:
            return Response('Farm Account Not Approved')
    else:
        return Response('Wrong Password or Email')

