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
from rest_framework.authtoken import views as rest

urlpatterns = [

    path('api-token-auth/', rest.obtain_auth_token),
    ### general
    path('logintokenchck/', views.loginTokenChck, name="logintokenchck"),
### User
    path('create_auth/', views.create_auth, name="create_auth"),
    path('login_auth/', views.login_auth, name="login_auth"),

    path('api_Edit_profile/', views.api_EditProfile, name="api_Edit_profile"),
    path('api_profile/', views.api_Profile, name="api_profile"),

    ### Supplier
    path('create_Tradeauth/', views.create_Tradeauth, name="create_Tradeauth"),
    path('reg_tradeauth/', views.reg_Tradeauth, name="reg_tradeauth"),
    path('login_Traderauth/', views.login_Traderauth, name="login_Traderauth"),
    path('supplier_transfer_data/', views.supplierTransferData, name="supplier_transfer_data"),
    path('supplier_transfer_update/', views.supplierTransferUpdate, name="supplier_transfer_update"),


    ## farm
    path('reg_farmauth/', views.reg_farmauth, name="reg_farmauth"),
    path('login_FarmTrad/', views.login_FarmTrad, name="login_FarmTrad"),
    path('reg_farmapp/', views.reg_farmapp, name="reg_farmapp"),


]
