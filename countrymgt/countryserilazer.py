from rest_framework import serializers
from .models import *


class LocationSerializer(serializers.Serializer):
    key = serializers.CharField()
    zone = serializers.CharField()
    msg = serializers.CharField()


class AllCountriesSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_photo')

    class Meta:
        model = CountryManager
        fields = ['id', 'country','photo']
    def get_photo(self,obj):
        return {
            "photo":obj.file_upload.url
        }

class CitySerializer(serializers.ModelSerializer):
    photo = serializers.URLField(source='file_upload.url')
    country = serializers.URLField(source='country.file_upload.url',read_only=True)
    class Meta:
        model = CityManagement
        fields = ['id', 'city','photo','country']

    # def get_photo(self, obj):
    #     return {
    #         "photo": obj.file_upload.url
    #     }

class ZoneSerializer(serializers.ModelSerializer):
    photo = serializers.URLField(source='city.file_upload.url', read_only=True)
    class Meta:
        model = CityZone
        fields = ['id', 'zone','photo']