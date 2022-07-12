from django.contrib.auth.models import User
from rest_framework import serializers

from vegefarm.models import FarmSellingProducts, SellingFarmBulkProducts, FarmProducts, FarmProductsBulk, FarmGrow


#  user
class SellingFarmProductsSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FarmSellingProducts
        fields = ['id', 'product', 'selling_price', 'inventory', 'product_data']

    def get_product_data(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            return {
                "product_data": obj.product.name_sc,
                "photo_data": obj.product.photo.url
            }
        return {
            "photo_data": obj.product.photo.url,
            "product_data": obj.product.name
        }


class SellingBulkFarmSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField('get_product_data')
    supplier = serializers.SerializerMethodField('get_supplier')

    class Meta:
        model = SellingFarmBulkProducts
        fields = ['id', 'selling_price', 'supplier', 'product_data']

    def get_product_data(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            return {
                "product_data": obj.product.name_sc,
                "photo_data": obj.product.photo.url
            }
        return {
            "photo_data": obj.product.photo.url,
            "product_data": obj.product.name
        }

    def get_supplier(self, obj):
        return {
            "symbl": obj.supplier.symbl,
            "scale": obj.supplier.scale,
            "weight": obj.supplier.weight,
        }


#  Farmer

class FarmSubmitedItemsSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = FarmProducts
        fields = ['id', 'price', 'inventory', 'scale', 'inv_due_date', 'items']

    def get_items(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            return {
                "photo_data": obj.product.photo.url,
                "name": obj.product.name_sc}
        return {
            "photo_data": obj.product.photo.url,
            "name": obj.product.name
        }


class FarmSubmitedBulkSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = FarmProductsBulk
        fields = ['id', 'price', 'inventory', 'scale', 'weight', 'inv_due_date', 'items']

    def get_items(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            return {
                "photo_data": obj.product.photo.url,
                "name": obj.product.name_sc}
        return {
            "photo_data": obj.product.photo.url,
            "name": obj.product.name
        }


# grower
class FarmGrowSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    create_date = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = FarmGrow
        fields = ['id', 'quantity', 'due_date', 'system', 'city','create_date', 'items']

    def get_items(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            return {
                "photo_data": obj.product.photo.url,
                "name": obj.product.name_sc}
        return {
            "photo_data": obj.product.photo.url,
            "name": obj.product.name
        }
