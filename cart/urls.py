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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as authViews
urlpatterns = [
######## user
    path('api_cart/', views.api_cart, name="api_cart"),
    path('api_cartTotal/', views.api_cartTotal, name="api_cartTotal"),

    path('cartactionproduct/', views.apiCartActionProduct, name="cartactionproduct"),
    path('apicartactionbox/', views.apiCartActionBox, name="apicartactionbox"),
    path('apicartactionfarm/', views.apiCartActionFarm, name="apicartactionfarm"),
    path('apiCartAddBulk/', views.apiCartAddBulk, name="apiCartAddBulk"),
    path('apifarmaddbulk/', views.apiFarmAddBulk, name="apifarmaddbulk"),
    path('apicartaddmix/', views.apiCartAddMix, name="apicartaddmix"),



    path('apicartaction/', views.apiCartAction, name="apicartaction"),
    path('apiaddnote/', views.apiAddNote, name="apiaddnote"),
    path('cancelorder/', views.cancelOrder, name="cancelorder"),
    path('makePayment/', views.makePayment, name="makePayment"),
    path('paymrespone/', views.paymrespone, name="paymrespone"),


    ####supplier
    path('apiorderslist/', views.apiOrdersList, name="apiorderslist"),
    path('apiconfirmprocess/', views.apiConfirmProcess, name="apiconfirmprocess"),
    path('apiordersprocessing/', views.apiOrdersProcessing, name="apiordersprocessing"),
    path('apiordersdeliverystats/', views.apiOrdersDeliveryStats, name="apiordersdeliverystats"),
    path('apiordersall/', views.apiOrdersAll, name="apiordersall"),

]
