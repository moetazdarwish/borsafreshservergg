from rest_framework import serializers
from .models import *


class NotifSerializer(serializers.ModelSerializer):
    class Meta :
        model = SupplierNotif
        fields = ['title','body']
