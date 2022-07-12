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

urlpatterns = [
    # User
    path('api_FAQSupport/', views.api_FAQSupport, name="api_FAQSupport"),
    path('api_getSupport/', views.api_getSupport, name="api_getSupport"),
    # Farm
    path('farmsupporter/', views.farmSupporter, name="farmsupporter"),
    path('farmmatch/', views.farmMatch, name="farmmatch"),
    path('api_GetAdvice/', views.api_GetAdvice, name="api_GetAdvice"),
    path('farmmakePayment/', views.farmmakePayment, name="farmmakePayment"),
    path('farmticketsupport/', views.farmTicketSupport, name="farmticketsupport"),
    path('farmTicketAnswer/', views.farmTicketAnswer, name="farmTicketAnswer"),
    # supporter
    path('supportermatchlist/', views.supporterMatchList, name="supportermatchlist"),
    path('supportergrowlist/', views.supporterGrowList, name="supportergrowlist"),
    path('addGrowAdvice/', views.addGrowAdvice, name="addGrowAdvice"),
    path('supporterFarmSupport/', views.supporterFarmSupport, name="supporterFarmSupport"),
    path('supporterFarmSupportPhoto/', views.supporterFarmSupportPhoto, name="supporterFarmSupportPhoto"),
    path('supporterAnswerFarmSupport/', views.supporterAnswerFarmSupport, name="supporterAnswerFarmSupport"),


]
# growernotif