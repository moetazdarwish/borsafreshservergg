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
##### user
    path('api_farmmarketfilter/', views.api_FarmMarketFilter, name="api_farmmarketfilter"),
    path('api_bulkfarmfilter/', views.api_BulkFarmFilter, name="api_bulkfarmfilter"),

    # Farmer
    path('farmproductcateg/', views.farmProductCateg, name="farmproductcateg"),
    path('farmsubmitoffer/', views.farmSubmitoffer, name="farmsubmitoffer"),
    path('farmbulkoffer/', views.farmBulkoffer, name="farmbulkoffer"),
    path('farmremove/', views.farmRemove, name="farmremove"),
    path('farmitemssubmitedlist/', views.farmItemsSubmitedList, name="farmitemssubmitedlist"),
    path('farmbulksubmitedlist/', views.farmBulkSubmitedList, name="farmbulksubmitedlist"),

    # grower
    path('creategrow/', views.createGrow, name="creategrow"),
    path('farmgrowlist/', views.farmGrowList, name="farmgrowlist"),




]
