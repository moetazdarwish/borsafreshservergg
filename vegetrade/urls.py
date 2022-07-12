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
#### user
    path('api_MarketFilter/', views.api_MarketFilter, name="api_MarketFilter"),
    path('api_BoxFilter/', views.api_BoxFilter, name="api_BoxFilter"),
    path('api_BoxContainFilter/', views.api_BoxContainFilter, name="api_BoxContainFilter"),
    path('api_BulkMarketFilter/', views.api_BulkMarketFilter, name="api_BulkMarketFilter"),
    path('api_mixedmarketfilter/', views.api_MixedMarketFilter, name="api_mixedmarketfilter"),

    #### supplier
    path('apiProductCateg/', views.apiProductCateg, name="apiProductCateg"),
    path('apiSubmitoffer/', views.apiSubmitoffer, name="apiSubmitoffer"),
    path('apiBoxoffer/', views.apiBoxoffer, name="apiBoxoffer"),
    path('apiAllItems/', views.apiAllItems, name="apiAllItems"),
    path('apiBoxitem/', views.apiBoxitem, name="apiBoxitem"),
    path('apiBoxDetails/', views.apiBoxDetails, name="apiBoxDetails"),
    path('apiBoxRemoveitem/', views.apiBoxRemoveitem, name="apiBoxRemoveitem"),
    path('apiBoxRemove/', views.apiBoxRemove, name="apiBoxRemove"),
    path('apiBoxPublish/', views.apiBoxPublish, name="apiBoxPublish"),
    path('apiItemsSubmitedList/', views.apiItemsSubmitedList, name="apiItemsSubmitedList"),
    path('apiBoxesSubmitedList/', views.apiBoxesSubmitedList, name="apiBoxesSubmitedList"),
    path('apibulkoffer/', views.apiBulkoffer, name="apibulkoffer"),
    path('apiremove/', views.apiRemove, name="apiremove"),
    path('apibulksubmitedlist/', views.apiBulkSubmitedList, name="apibulksubmitedlist"),
    path('apimixoffer/', views.apiMixoffer, name="apimixoffer"),
    path('apimixedsubmitedlist/', views.apiMixedSubmitedList, name="apimixedsubmitedlist"),

]
