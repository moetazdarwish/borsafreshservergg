from rest_framework import serializers
from .models import *


class OrderProductsSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField(read_only=True)
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['id', 'buy_price', 'symbl', 'quantity', 'product_data', 'total']

    def get_product_data(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            return {
                "product_data": obj.product.name_sc,
                "photo_data": obj.product.photo.url
            }
        return {
            "product_data": obj.product.name,
            "photo_data": obj.product.photo.url,
        }

    def get_total(self, obj):
        return {
            "total": obj.get_total,
        }


class OrderSerializer(serializers.ModelSerializer):
    ItemsCount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Orders
        fields = ['id', 'ItemsCount', 'symbl', 'note']

    def get_ItemsCount(self, obj):
        return {
            "ItemsCount": obj.get_cart_items,
            "ItemsSubtotal": obj.get_cart_sub_total,
            "Itemstotal": obj.get_cart_total,
            "ItemsTax": obj.get_cart_tax,
            "ItemsShipping": obj.get_shipping,
        }


class AllOrdersSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    delivery = serializers.SerializerMethodField('get_delivery')
    status = serializers.SerializerMethodField('get_status')

    class Meta:
        model = OrderProduct
        fields = ['id', 'transaction_id', 'quantity', 'status', 'items', 'delivery']

    def get_items(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            if obj.is_bulk:
                return {
                    "photo_data": obj.product.photo.url,
                    "name": obj.product.name_sc,
                    "box_name": obj.product.lang.box_name_sc,
                    "scale": obj.product.lang.scale_sc,
                }
            if obj.is_farm_bulk:
                return {
                    "photo_data": obj.product.photo.url,
                    "name": obj.product.name_sc,
                    "box_name": obj.product.lang.box_name_sc,
                    "scale": obj.product.lang.scale_sc,
                }
            if obj.is_box:
                return {
                    "photo_data": obj.product.photo.url,
                    "name": obj.product.name_sc,
                    "box_name": obj.box_name,
                    "scale": obj.product.lang.scale_sc,
                }
            return {
                "photo_data": obj.product.photo.url,
                "name": obj.product.name_sc,
                "box_name": obj.product.lang.retail_sc,
                "scale": obj.scale,
            }

        if obj.is_bulk:
            return {
                "photo_data": obj.product.photo.url,
                "name": obj.product.name,
                "box_name": obj.product.lang.box_name,
                "scale": obj.product.lang.scale,
            }
        if obj.is_farm_bulk:
            return {
                "photo_data": obj.product.photo.url,
                "name": obj.product.name,
                "box_name": obj.product.lang.box_name,
                "scale": obj.product.lang.scale,
            }
        if obj.is_box:
            return {
                "photo_data": obj.product.photo.url,
                "name": obj.product.name,
                "box_name": obj.box_name,
                "scale": obj.product.lang.scale,
            }
        return {
            "photo_data": obj.product.photo.url,
            "name": obj.product.name,
            "box_name": obj.product.lang.retail,
            "scale": obj.scale,
        }

    def get_delivery(self, obj):
        return {
            "adress": obj.order.name.address,
            "area": obj.order.name.area,
            "phone": obj.order.name.phone,
            "city": obj.order.name.city,
            "country": obj.order.name.country,
            "first_name": obj.order.name.name.first_name,
            "last_name": obj.order.name.name.last_name,
        }

    def get_status(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            if obj.status == 'ACCEPT':
                return {
                    "status": obj.product.lang.st_accept_sc
                }
            if obj.status == 'CONFIRMED':
                return {
                    "status": obj.product.lang.st_confirmed_sc
                }
            if obj.status == 'DELIVERY OUT':
                return {
                    "status": obj.product.lang.st_delivery_sc
                }
            if obj.status == 'DELIVERED':
                return {
                    "status": obj.product.lang.st_delivered_sc
                }
            if obj.status == 'RESCHEDULE':
                return {
                    "status": obj.product.lang.st_reschedule_sc
                }
            if obj.status == 'REFUSED':
                return {
                    "status": obj.product.lang.st_refused_sc
                }
            if obj.status == 'CANCELLED':
                return {
                    "status": obj.product.lang.st_cancelled_sc
                }

        if obj.status == 'ACCEPT':
            return {
                "status": obj.product.lang.st_accept
            }
        if obj.status == 'CONFIRMED':
            return {
                "status": obj.product.lang.st_confirmed
            }
        if obj.status == 'DELIVERY OUT':
            return {
                "status": obj.product.lang.st_delivery
            }
        if obj.status == 'DELIVERED':
            return {
                "status": obj.product.lang.st_delivered
            }
        if obj.status == 'RESCHEDULE':
            return {
                "status": obj.product.lang.st_reschedule
            }
        if obj.status == 'REFUSED':
            return {
                "status": obj.product.lang.st_refused
            }
        if obj.status == 'CANCELLED':
            return {
                "status": obj.product.lang.st_cancelled
            }
