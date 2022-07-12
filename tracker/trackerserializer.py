from rest_framework import serializers

from cart.models import OrderProduct, Orders
from tracker.models import OrderTracking

class UserOrderTrackingSerializer(serializers.ModelSerializer):

    class Meta :
        model = Orders
        fields = ['id','transaction_id',]

class UserTrackingSerializer(serializers.ModelSerializer):
    create_date= serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta :
        model = OrderTracking
        fields = ['order','transaction_id','status','create_date']



class UserTrackSubOrderSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField( read_only=True)
    class Meta :
        model = OrderProduct
        fields = ['id','buy_price','symbl','quantity','product_data']

    def get_product_data(self,obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            return{
            "product_data":obj.product.name_sc,
            "photo_data":obj.product.photo.url,
        }
        return {
            "product_data":obj.product.name,
            "photo_data":obj.product.photo.url,
        }

