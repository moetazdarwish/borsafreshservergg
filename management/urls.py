"""ilearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
import datetime
today = str('55452155545998884221221445654dfgfgfdgf32326')
urlpatterns = [
    path('', views.login, name="login"),

    path('main/', views.main, name="main"),
    # order
    path('order/', views.order, name="order"),
    path('orderFilter/', views.orderFilter, name="orderFilter"),
    path('orderDetails/', views.orderDetails, name="orderDetails"),
    path('orderUserDetails/', views.orderUserDetails, name="orderUserDetails"),
    path('orderTraderDetails/', views.orderTraderDetails, name="orderTraderDetails"),
    path('orderAction/<pk>', views.orderAction, name="orderAction"),
    path('subOrderAction/<pk>', views.subOrderAction, name="subOrderAction"),
    # users
    path('userList/', views.userList, name="userList"),
    path('userTrader/', views.userTrader, name="userTrader"),
    path('userTraderNew/', views.userTraderNew, name="userTraderNew"),
    path('userFarmNew/', views.userFarmNew, name="userFarmNew"),
    path('userFarms/', views.userFarms, name="userFarms"),
    path('userFilter/', views.userFilter, name="userFilter"),
    path('userNotifList/<pk>', views.userNotifList, name="userNotifList"),
    path('userNotifListChange/<pk>', views.userNotifListChange, name="userNotifListChange"),
    path('tradeNotifList/<pk>', views.tradeNotifList, name="tradeNotifList"),
    path('userAction/<pk>', views.userAction, name="userAction"),
    path('userSubMSG/<pk>', views.userSubMSG, name="userSubMSG"),
    path('userTraderNewApprove/<pk>', views.userTraderNewApprove, name="userTraderNewApprove"),
    path('userTraderNewDecline/<pk>', views.userTraderNewDecline, name="userTraderNewDecline"),
    # map
    path('map/', views.map, name="map"),
    path('mapCities/<pk>', views.mapCities, name="mapCities"),
    path('mapZoneAction/<pk>', views.mapZoneAction, name="mapZoneAction"),
    path('mapZoneList/<pk>', views.mapZoneList, name="mapZoneList"),
    path('mapCitiesFilter/', views.mapCitiesFilter, name="mapCitiesFilter"),
    path('mapadd/', views.mapadd, name="mapadd"),
    path('mapaddzone/<pk>', views.mapaddzone, name="mapaddzone"),
    path('mapaddzonedelete/<pk>', views.mapaddzonedelete, name="mapaddzonedelete"),
    path('mapnewAreas/', views.mapnewAreas, name="mapnewAreas"),
    # tracking

    path('ordersSubTracker/<pk>', views.ordersSubTracker, name="ordersSubTracker"),
    path('ordersReview/<pk>', views.ordersReview, name="ordersReview"),
    # ads
    path('adsList/', views.adsList, name="adsList"),
    path('adsDetail/<pk>', views.adsDetail, name="adsDetail"),
    path('adsDetailadd/', views.adsDetailadd, name="adsDetailadd"),
    path('adsFilter/', views.adsFilter, name="adsFilter"),
    # product
    path('productCatg/', views.productCatg, name="productCatg"),
    path('productCatgFilter/', views.productCatgFilter, name="productCatgFilter"),
    path('productCatgAdd/', views.productCatgAdd, name="productCatgAdd"),
    path('productCatgDetail/<pk>', views.productCatgDetail, name="productCatgDetail"),
    # support
    path('supportTiket/', views.supportTiket, name="supportTiket"),
    path('supportTiketAction/<pk>', views.supportTiketAction, name="supportTiketAction"),
    path('supportTiketAddFile/<pk>', views.supportTiketAddFile, name="supportTiketAddFile"),
    path('supportTiketAnswer/<pk>', views.supportTiketAnswer, name="supportTiketAnswer"),
    path('supportTiketCreate/<pk>', views.supportTiketCreate, name="supportTiketCreate"),
    path('supportTiketSubCreate/<pk>', views.supportTiketSubCreate, name="supportTiketSubCreate"),
    path('supportTiketUserCreate/<pk>', views.supportTiketUserCreate, name="supportTiketUserCreate"),
    # Farms
    path('supportFarmsList/', views.supportFarmsList, name="supportFarmsList"),
    path('getSupporterData/<pk>', views.getSupporterData, name="getSupporterData"),
    # account
    path('getIncomeAccunt/', views.getIncomeAccunt, name="getIncomeAccunt"),
    path('getExpenceAccunt/', views.getExpenceAccunt, name="getExpenceAccunt"),
    path('getCashOAccunt/', views.getCashOAccunt, name="getCashOAccunt"),
    path('getRefundOAccunt/', views.getRefundOAccunt, name="getRefundOAccunt"),
    path('getTaxAccunt/', views.getTaxAccunt, name="getTaxAccunt"),
    path('getRevAccunt/', views.getRevAccunt, name="getRevAccunt"),
    path('getCashOTraderAccunt/<pk>/', views.getCashOTraderAccunt, name="getCashOTraderAccunt"),
    path('getCashOTraderallAccunt/<pk>/', views.getCashOTraderallAccunt, name="getCashOTraderallAccunt"),
    path('makeRefundAccunt/<pk>/', views.makeRefundAccunt, name="makeRefundAccunt"),


]
