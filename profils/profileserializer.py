from rest_framework import serializers
from .models import *


# user

class USERPROFILESerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField( read_only=True)
    class Meta:
        model = UsersProfiles
        fields = ['phone', 'address','postal_code','area','city']

    def get_city(self,obj):
        return {
            "city":obj.city,
            "country":obj.country
        }


class TraderTransDataSerializer(serializers.ModelSerializer):

    class Meta :
        model = TraderTransData
        fields = ['current']


class LogininSerializer(serializers.Serializer):
    key = serializers.CharField()
    name = serializers.CharField()

class MSGSerializer(serializers.Serializer):
    auth = serializers.CharField()
    msg = serializers.CharField()
    escape = serializers.CharField()

# Supporter

class SupporterSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')
    class Meta:
        model = SupporterProfiles
        fields = ['name','phone','city','country','fees','experience']

    def get_name(self,obj):
        return {
            "name":obj.name.get_full_name(),
        }

