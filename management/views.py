from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
import datetime
# Create your views here.
from accountmgt.models import RevenueAccount, IncomeAccount, ExpensesAccount, CashOutAccount, RefundAccount, TAXAccount, \
    PaymentAccount
from admanager.models import Advertesing
from cart.models import Orders, OrderProduct
from countrymgt.models import CountryManager, CityManagement, CityZone, NewZone
from management.decorators import allowedUser
from notif.models import UserNotif, SupplierNotif
from profils.models import UsersProfiles, ProfilesZone, ProfilePhotos, ProfilesMSG, SupporterProfiles, TraderTransData
from support.models import TicketSupport, TicketFiles, TicketAnswers, FarmSupport
from tracker.models import OrderTracking, SubOrderTracking, SubOrderReview
from vegetrade.models import CategoryProducts, CategoryList, CountryTransLang

def login(request):
    if request.POST:
        usr = request.POST.get('email')
        pss = request.POST.get('password')
        user = authenticate(request, username=usr, password=pss)
        if user is not None:
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'admin':
                return redirect('main')
            if group == 'support':
                return redirect('order')
            else:
                return redirect('login')
    return render(request, 'dashboard/login.html')

@allowedUser(allowedGroups=['admin'])
def main(request):
    user_count = UsersProfiles.objects.all().count()
    order_count = Orders.objects.all().count()
    zone_count = CityZone.objects.all().count()
    acc_count = IncomeAccount.objects.all().count()

    context = {'user_count':user_count,'order_count':order_count,
               'acc_count':acc_count,'zone_count':zone_count}
    return render(request, 'dashboard/main.html',context)


def order(request):
    _order = Orders.objects.all()
    paginator = Paginator(_order, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"order": page_obj}
    return render(request, 'dashboard/order.html', context)


def orderDetails(request):
    get_id = request.GET.get('myid')
    _order = Orders.objects.get(id=get_id)
    sub_order = OrderProduct.objects.filter(order=_order)
    context = {"sub_order": sub_order, 'order': _order}
    return render(request, 'dashboard/orderdetails.html', context)


def orderFilter(request):
    get_id = request.POST.get('search')
    _order = Orders.objects.filter(transaction_id__contains=get_id)

    context = {"order": _order}
    return render(request, 'dashboard/orderfilter.html', context)


def orderUserDetails(request):
    get_id = request.GET.get('myid')
    _user = UsersProfiles.objects.get(id=get_id)
    sub_order = Orders.objects.filter(name=_user)
    paginator = Paginator(sub_order, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"order": page_obj, 'user': _user}
    return render(request, 'dashboard/userdetail.html', context)


def orderTraderDetails(request):
    if request.POST:
        post_id = request.POST.get('myid')
        _user = UsersProfiles.objects.get(id=post_id)
        post_title = request.POST.get('title')
        post_file = request.FILES.get('file')
        if post_file:
            ProfilePhotos.objects.create(title=post_title, name=_user, photo=post_file)
            return redirect('/management/orderTraderDetails/?myid={}'.format(post_id))
        else:
            return redirect('/management/orderTraderDetails/?myid={}'.format(post_id))
    else:
        get_id = request.GET.get('myid')
        _user = UsersProfiles.objects.get(id=get_id)
        zons = ProfilesZone.objects.filter(user=_user)
        fils = ProfilePhotos.objects.filter(name=_user)
        sub_order = OrderProduct.objects.filter(trader=_user)
        paginator = Paginator(sub_order, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"order": page_obj, 'user': _user, 'zons': zons, 'fils': fils}
        return render(request, 'dashboard/traderdetail.html', context)


def orderAction(request, pk):

    sub_order = Orders.objects.get(id=pk)
    if request.POST:
        get_act = request.POST.get('action')
        if get_act == 'note':
            value = request.POST.get('note')
            sub_order.note = value
            sub_order.save()
            return redirect('order')
        if get_act == 'stat':
            value = request.POST.get('stut')
            sub_order.status = value
            sub_order.save()
            return redirect('order')
    context = {"order": sub_order, }
    return render(request, 'dashboard/orderaction.html', context)


def subOrderAction(request, pk):
    sub_order = OrderProduct.objects.get(id=pk)
    if request.POST:
        get_act = request.POST.get('action')
        if get_act == 'stat':
            value = request.POST.get('stut')
            sub_order.status = value
            sub_order.save()
            return redirect('order')
    context = {"order": sub_order, }
    return render(request, 'dashboard/suborderaction.html', context)


def userList(request):
    _user = UsersProfiles.objects.all()
    paginator = Paginator(_user, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"user": page_obj}
    return render(request, 'dashboard/userlist.html', context)


def userAction(request, pk):
    _user = UsersProfiles.objects.get(id=pk)
    context = {"user": _user}
    return render(request, 'dashboard/useraction.html', context)


def userSubMSG(request, pk):
    _user = UsersProfiles.objects.get(id=pk)
    if request.POST:
        msg = request.POST.get('msg')
        smal_msg = request.POST.get('smal_msg')
        is_admin = request.POST.get('admin')
        if is_admin is None:
            is_admin = False
        ProfilesMSG.objects.create(user=_user, msg=msg, smal_msg=smal_msg, is_admin=is_admin)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {"user": _user}
    return render(request, 'dashboard/usermsg.html', context)


def userTrader(request):
    _user = UsersProfiles.objects.filter(is_trader=True)
    paginator = Paginator(_user, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"user": page_obj}
    return render(request, 'dashboard/usertrade.html', context)


def userTraderNew(request):
    _user = UsersProfiles.objects.filter(is_trader=True, approve=False)
    paginator = Paginator(_user, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"user": page_obj}
    return render(request, 'dashboard/usertrade.html', context)


def userTraderNewApprove(request, pk):
    _user = UsersProfiles.objects.get(id=pk)
    _user.approve = True
    _user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def userTraderNewDecline(request, pk):
    _user = UsersProfiles.objects.get(id=pk)
    _user.approve = False
    _user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def userFarmNew(request):
    _user = UsersProfiles.objects.filter(is_farm=True, approve=False)
    paginator = Paginator(_user, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"user": page_obj}
    return render(request, 'dashboard/usertrade.html', context)


def userFarms(request):
    _user = UsersProfiles.objects.filter(is_farm=True)
    paginator = Paginator(_user, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"user": page_obj}
    return render(request, 'dashboard/userlist.html', context)


def userFilter(request):
    get_id = request.POST.get('search')
    _user = UsersProfiles.objects.filter(name__email__contains=get_id)
    context = {"user": _user}
    return render(request, 'dashboard/userfilter.html', context)


def userNotifList(request, pk):
    _user = UsersProfiles.objects.get(id=pk)
    get_not = UserNotif.objects.filter(name=_user)
    context = {"notif": get_not}
    return render(request, 'dashboard/notifdetail.html', context)


def userNotifListChange(request, pk):
    get_not = UserNotif.objects.get(id=pk)
    get_not.read = not get_not.read
    get_not.save()
    return redirect('userNotifList', pk=get_not.name.id)


def tradeNotifList(request, pk):
    _user = UsersProfiles.objects.get(id=pk)
    get_not = SupplierNotif.objects.filter(trader=_user)
    context = {"notif": get_not}
    return render(request, 'dashboard/notifdetail.html', context)


def map(request):
    instance = CountryManager.objects.all()
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"country": page_obj}
    return render(request, 'dashboard/maps.html', context)


def mapCities(request, pk):
    country = CountryManager.objects.get(id=pk)
    instance = CityZone.objects.filter(country=country)
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"zones": page_obj}
    return render(request, 'dashboard/citiesdetail.html', context)


def mapCitiesFilter(request):
    city = request.POST.get('search')
    instance = CityZone.objects.filter(city__city__contains=city)

    context = {"zones": instance}
    return render(request, 'dashboard/citytable.html', context)


def mapZoneAction(request, pk):
    if request.POST:
        instance = CityZone.objects.get(id=pk)
        instance.lat_greater = request.POST.get('lat_greater')
        instance.lat_lower = request.POST.get('lat_lower')
        instance.long_greater = request.POST.get('long_greater')
        instance.long_lower = request.POST.get('long_lower')
        instance.trader_percent = request.POST.get('trader_percent')
        instance.farm_percent = request.POST.get('farm_percent')
        instance.customer_percent = request.POST.get('customer_percent')
        instance.duedate = request.POST.get('duedate')
        instance.shipping = request.POST.get('shipping')
        instance.save()
        return redirect('mapCities', instance.country.id)
    else:
        instance = CityZone.objects.get(id=pk)
        context = {"zones": instance}
        return render(request, 'dashboard/mapaction.html', context)


def mapZoneList(request, pk):
    instance = ProfilesZone.objects.filter(zone__id=pk)
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"zones": page_obj}
    return render(request, 'dashboard/maplist.html', context)


def mapadd(request):
    if request.POST:
        country = request.POST.get('country')
        second_lang = request.POST.get('lang')
        tax_rate = request.POST.get('tax_rate')
        tax = request.POST.get('tax')
        if tax is None:
            tax = 'False'
        symbl = request.POST.get('symbl')
        file_upload = request.FILES.get('file')
        obj = CountryManager.objects.create(country=country, second_lang=second_lang, tax_rate=tax_rate,
                                            tax=tax, symbl=symbl, file_upload=file_upload)
        context = {"country": obj}
        return render(request, 'dashboard/mapzoneadd.html', context)
    else:
        return render(request, 'dashboard/mapadd.html')


def mapaddzone(request, pk):
    if request.POST:
        country = CountryManager.objects.get(id=pk)
        city = request.POST.get('city')
        zone = request.POST.get('zone')
        lat_greater = request.POST.get('lat_greater')
        lat_lower = request.POST.get('lat_lower')
        long_greater = request.POST.get('long_greater')
        long_lower = request.POST.get('long_lower')
        trader_percent = request.POST.get('trader_percent')
        farm_percent = request.POST.get('farm_percent')
        customer_percent = request.POST.get('customer_percent')
        duedate = request.POST.get('duedate')
        shipping = request.POST.get('shipping')
        obj_city = CityManagement.objects.create(country=country, city=city)
        CityZone.objects.create(country=country, city=obj_city, zone=zone, lat_greater=lat_greater,
                                lat_lower=lat_lower, long_greater=long_greater, long_lower=long_lower,
                                trader_percent=trader_percent, farm_percent=farm_percent,
                                customer_percent=customer_percent,
                                duedate=duedate, shipping=shipping)

        return redirect('mapaddzone', pk)
    else:
        country = CountryManager.objects.get(id=pk)
        obj = CityZone.objects.filter(country=country)
        context = {"zone": obj, 'country': country}
        return render(request, 'dashboard/mapzoneadded.html', context)


def mapaddzonedelete(request, pk):
    delet = CityZone.objects.get(id=pk)
    country = CountryManager.objects.get(id=delet.country.id)
    obj = CityZone.objects.filter(country=country)
    delet.delete()
    context = {"zone": obj, 'country': country}
    return render(request, 'dashboard/mapzoneadded.html', context)


def mapnewAreas(request, ):
    obj = NewZone.objects.filter()

    context = {"zone": obj, }
    return render(request, 'dashboard/mapsnewarea.html', context)


def ordersSubTracker(request, pk):
    get_ord = Orders.objects.get(id=pk)
    instance = SubOrderTracking.objects.filter(order=get_ord)
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"track": page_obj}
    return render(request, 'dashboard/tracker.html', context)


def ordersReview(request, pk):
    get_ord = Orders.objects.get(id=pk)
    instance = SubOrderReview.objects.filter(order=get_ord)

    context = {"track": instance}
    return render(request, 'dashboard/review.html', context)


def adsList(request):
    instance = Advertesing.objects.all()
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"ads": page_obj}
    return render(request, 'dashboard/ads.html', context)


def adsFilter(request):
    get_id = request.POST.get('search')
    instance = Advertesing.objects.filter(Q(country__contains=get_id) | Q(type__contains=get_id))

    context = {"ads": instance}
    return render(request, 'dashboard/adfilter.html', context)


def adsDetail(request, pk):
    instance = Advertesing.objects.get(id=pk)

    context = {"ads": instance}
    return render(request, 'dashboard/adsdetail.html', context)


def adsDetailadd(request):
    if request.POST:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        postal_code = request.POST.get('postal_code')
        city = request.POST.get('city')
        country = request.POST.get('country')
        area = request.POST.get('area')
        lat = request.POST.get('lat')
        long = request.POST.get('long')
        logo = request.FILES.get('file')
        msg = request.POST.get('msg')
        link = request.POST.get('link')
        type = request.POST.get('type')
        Advertesing.objects.create(name=name, phone=phone, email=email, address=address, postal_code=postal_code,
                                   city=city, country=country, area=area, lat=lat, long=long, logo=logo,
                                   msg=msg, link=link, type=type)
        return redirect('adsList')

    return render(request, 'dashboard/adsdetailadd.html')


# product
def productCatg(request):
    instance = CategoryProducts.objects.all()
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"product": page_obj}
    return render(request, 'dashboard/productlist.html', context)


def productCatgDetail(request, pk):
    instance = CategoryProducts.objects.get(id=pk)
    context = {"product": instance}
    return render(request, 'dashboard/productlistdetail.html', context)


def productCatgAdd(request):
    cat = CategoryList.objects.all()
    cont_tr = CountryTransLang.objects.all()
    if request.POST:
        name = request.POST.get('pro')
        name_sc = request.POST.get('tran')
        category = request.POST.get('cat')
        get_cat = CategoryList.objects.get(id=category)
        photo = request.FILES.get('file')
        lang = request.POST.get('trancotry')
        get_lang = CountryTransLang.objects.get(id=lang)
        country = request.POST.get('contry')
        CategoryProducts.objects.create(name=name, name_sc=name_sc, category=get_cat, photo=photo, lang=get_lang,
                                        country=country)
        return redirect('productCatg')
    context = {"cat": cat, 'cont_tr': cont_tr}
    return render(request, 'dashboard/addproduct.html', context)


def productCatgFilter(request):
    get_id = request.POST.get('search')
    instance = CategoryProducts.objects.filter(
        Q(country__contains=get_id) | Q(name__contains=get_id))
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"product": page_obj}
    return render(request, 'dashboard/productlistfilter.html', context)


# support

def supportTiket(request):
    instance = TicketSupport.objects.all()
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"support": page_obj}
    return render(request, 'dashboard/supportlist.html', context)


def supportTiketAction(request, pk):
    instance = TicketSupport.objects.get(id=pk)
    old = TicketSupport.objects.filter(user=instance.user)
    file = TicketFiles.objects.filter(ticket=instance)
    answers = TicketAnswers.objects.filter(ticket=instance)

    context = {"support": instance, 'fils': file, 'answers': answers, 'old': old}
    return render(request, 'dashboard/tickectanswer.html', context)


def supportTiketAddFile(request, pk):
    instance = TicketSupport.objects.get(id=pk)
    file = request.FILES.get('file')
    title = request.POST.get('title')
    TicketFiles.objects.create(ticket=instance, title=title, files=file)
    files = TicketFiles.objects.filter(ticket=instance)
    context = {"fils": files, }
    return render(request, 'dashboard/supportfileupload.html', context)


def supportTiketAnswer(request, pk):
    instance = TicketSupport.objects.get(id=pk)
    answer = request.POST.get('ansr')
    option = request.POST.get('option')
    dpart = request.POST.get('dpart')
    instance.status = option
    instance.dep = dpart
    instance.save()
    TicketAnswers.objects.create(user=instance.user, ticket=instance, answer=answer, dep=dpart, )
    answers = TicketAnswers.objects.filter(ticket=instance)
    context = {"answers": answers, 'support': instance}
    return render(request, 'dashboard/ticktanswerupdate.html', context)


#

def supportTiketCreate(request, pk):
    instance = Orders.objects.get(id=pk)
    support, create = TicketSupport.objects.get_or_create(user=instance.name, order=instance,
                                                          country=instance.name.country, status='OPEN')
    context = {"question": instance, 'support': support}
    return render(request, 'dashboard/ticketcreate.html', context)


def supportTiketUserCreate(request, pk):
    instance = UsersProfiles.objects.get(id=pk)
    support, create = TicketSupport.objects.get_or_create(user=instance, country=instance.country, status='OPEN')
    context = {"name": instance, 'support': support}
    return render(request, 'dashboard/ticketcreate.html', context)


def supportTiketSubCreate(request, pk):
    support = TicketSupport.objects.get(id=pk)
    support.subject = request.POST.get('subject')
    support.question = request.POST.get('qstn')
    support.dep = request.POST.get('dpart')
    support.save()
    context = {'support': support}
    return render(request, 'dashboard/ticktsubconfirm.html', context)


# suport farm
def supportFarmsList(request):
    instance = FarmSupport.objects.all()
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"support": page_obj}
    return render(request, 'dashboard/supportlistfarm.html', context)


def getSupporterData(request, pk):
    _user = SupporterProfiles.objects.get(id=pk)

    context = {'user': _user}
    return render(request, 'dashboard/userdetail.html', context)


# Account

def getIncomeAccunt(request):
    instance = IncomeAccount.objects.all()
    count = IncomeAccount.objects.all().aggregate(product__price=Sum('total'))['product__price']
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"account": page_obj, 'count': float(count)}
    return render(request, 'dashboard/accinc.html', context)


def getExpenceAccunt(request):
    instance = ExpensesAccount.objects.filter(key='PENDING')
    count = instance.aggregate(product__expense=Sum('expense'))['product__expense']
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"account": page_obj, 'count': float(count)}
    return render(request, 'dashboard/expenceacc.html', context)


def getCashOAccunt(request):
    instance = CashOutAccount.objects.filter(key='WAITING')
    count = instance.aggregate(product__expense=Sum('expense'))['product__expense']
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"account": page_obj, 'count': float(count)}
    return render(request, 'dashboard/cashotacc.html', context)


def getCashOTraderAccunt(request, pk):
    today = datetime.datetime.now().date()
    get_us = UsersProfiles.objects.get(id=pk)
    bank = TraderTransData.objects.get(benfec=get_us)
    instance = CashOutAccount.objects.filter(supplier=get_us,key='WAITING',due_date__lte=today )
    if instance :
        count = instance.aggregate(product__expense=Sum('expense'))['product__expense']
        if request.POST:
            tranID = request.POST.get('trasid')
            tranREF = request.POST.get('trasref')
            obj = PaymentAccount.objects.create(user_trans=get_us,transaction_id=tranID,transaction_ref=tranREF,
                                          amount=count,)
            for i in instance:
                i.key = 'TRANSFERRED'
                obj.order_product.add(i.order_product)
                i.save()
                obj.save()
            return redirect('getCashOTraderAccunt' ,pk)
        context = {"account": instance, 'count': float(count), 'user': get_us, 'bank': bank}
        return render(request, 'dashboard/cashpayment.html', context)
    context = { 'user': get_us, 'bank': bank}
    return render(request, 'dashboard/cashpayment.html', context)
def getCashOTraderallAccunt(request, pk):

    get_us = UsersProfiles.objects.get(id=pk)
    bank = TraderTransData.objects.get(benfec=get_us)
    instance = CashOutAccount.objects.filter(supplier=get_us,)
    count = instance.aggregate(product__expense=Sum('expense'))['product__expense']
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"account": page_obj, 'count': float(count), 'user': get_us, 'bank': bank}
    return render(request, 'dashboard/cashpayment.html', context)

def getRefundOAccunt(request):
    instance = RefundAccount.objects.all()
    count = instance.aggregate(product__expense=Sum('expense'))['product__expense']
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"account": page_obj, 'count': float(count)}
    return render(request, 'dashboard/refundacc.html', context)

def makeRefundAccunt(request,pk):
    get_us = UsersProfiles.objects.get(id=pk)
    instance = RefundAccount.objects.filter(user_trans=get_us)
    if instance:
        count = instance.aggregate(product__expense=Sum('expense'))['product__expense']
        if request.POST:
            tranID = request.POST.get('trasid')
            tranREF = request.POST.get('trasref')
            obj = PaymentAccount.objects.create(user_trans=get_us, transaction_id=tranID, transaction_ref=tranREF,
                                                amount=count, )
            for i in instance:
                i.key = 'TRANSFERRED'
                obj.order_product.add(i.order_item)
                i.save()
                obj.save()
            return redirect('makeRefundAccunt', pk)
        context = {"account": instance, 'count': float(count),'user':get_us}
        return render(request, 'dashboard/refundaccuser.html', context)
    context = {'user': get_us,}
    return render(request, 'dashboard/refundaccuser.html', context)

def getTaxAccunt(request):
    instance = TAXAccount.objects.all()
    count = instance.aggregate(product__expense=Sum('expense'))['product__expense']
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"account": page_obj, 'count': float(count)}
    return render(request, 'dashboard/taxacc.html', context)


def getRevAccunt(request):
    instance = RevenueAccount.objects.all()
    count = instance.aggregate(product__expense=Sum('profit'))['product__expense']
    paginator = Paginator(instance, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"account": page_obj, 'count': float(count)}
    return render(request, 'dashboard/revenueacc.html', context)