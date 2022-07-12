from rest_framework import serializers
from .models import *


# user


class AdManagerSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField('get_logo')
    class Meta:
        model = Advertesing
        fields = ['id','name', 'phone','address','postal_code','area','city','country','lat','long','msg'
            ,'link','due','logo','type']

    def get_logo(self,obj):
        return{
            'logo':obj.logo.url
        }


