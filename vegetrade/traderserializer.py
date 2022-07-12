from django.contrib.auth.models import User
from rest_framework import serializers

from .models import SellingProducts, CategoryProducts, Products, MixedBox, ProductsBox, SellingBoxProducts, \
    SellingBulkProducts, ProductsBulk, ProductsMixed, SellingMixedProducts


### Global
class CategoryProductsSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CategoryProducts
        fields = ['name', 'photo', 'id']

    def get_photo(self, obj):
        return {
            "photo_data": obj.photo.url
        }

    def get_name(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            return obj.name_sc
        return obj.name


### User
class SellingProductsSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField('get_product_data')
    supplier = serializers.SerializerMethodField('get_supplier')

    class Meta:
        model = SellingProducts
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
            "inventory": obj.supplier.inventory,
        }


class MixedProductsSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MixedBox
        fields = ['id', 'scale', 'weight', 'items', ]

    def get_items(self, obj):
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


class UserBoxSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField('get_product_data')
    box = serializers.SerializerMethodField('get_box')

    class Meta:
        model = SellingBoxProducts
        fields = ['id', 'selling_price', 'symbl', 'count', 'box', 'product_data']

    def get_product_data(self, obj):
        return {
            "photo_data": obj.product.photo.url
        }

    def get_box(self, obj):
        return {
            "box_name": obj.box.box_name
        }


class SellingBulkProductsSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField('get_product_data')
    supplier = serializers.SerializerMethodField('get_supplier')

    class Meta:
        model = SellingBulkProducts
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


class SellingMixedProductsSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField('get_product_data')
    supplier = serializers.SerializerMethodField('get_supplier')

    class Meta:
        model = SellingMixedProducts
        fields = ['id', 'selling_price', 'supplier', 'product_data']

    def get_product_data(self, obj):
        return {
            "photo_data": obj.product.photo.url,
        }

    def get_supplier(self, obj):
        return {
            "symbl": obj.supplier.symbl,
            "scale": obj.supplier.scale,
            "weight": obj.supplier.weight,
            "description": obj.supplier.description,
            "mix_name": obj.supplier.mix_name,
        }


###Supplier

class itemsSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MixedBox
        fields = ['id', 'scale', 'weight', 'data', ]

    def get_data(self, obj):
        return {
            "photo_data": obj.items.photo.url,
            "name": obj.items.name
        }


class BoxSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    def get_items(self, obj):
        get_box = MixedBox.objects.filter(box=obj)
        serializer = itemsSerializer(instance=get_box, many=True)
        return serializer.data

    class Meta:
        model = ProductsBox
        fields = ['id', 'box_name', 'price', 'inventory', 'inv_due_date', 'items']


class SubmitedItemsFilterSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Products
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


class SubmitedBoxesFilterSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = ProductsBox
        fields = ['id', 'price', 'inventory', 'inv_due_date', 'items', 'box_name']

    def get_items(self, obj):
        return {
            "photo_data": obj.product.photo.url,
        }


class SubmitedBulkFilterSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = ProductsBulk
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


class SubmitedMixedFilterSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = ProductsMixed
        fields = ['id', 'price', 'inventory', 'scale','mix_name', 'description', 'weight', 'inv_due_date', 'items']

    def get_items(self, obj):
        return {
            "photo_data": obj.product.photo.url,
        }
