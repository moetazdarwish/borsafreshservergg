from rest_framework import serializers
from .models import *


class ExpenseAccountSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)
    key = serializers.SerializerMethodField('get_key')

    class Meta:
        model = ExpensesAccount
        fields = ('id', 'transaction_id', 'expense', 'create_date', 'due_date', 'key')

    def get_key(self, obj):
        user_id = self.context.get("lang")
        # if user_id == 'ar':
        #     if obj.key == 'PENDING':
        #         return {
        #             "key": "في انتظار تاكيد التوصيل"
        #         }
        #     if obj.key == 'LOST':
        #         return {
        #             "key": "بيع مفقوده"
        #         }
        if obj.key == 'PENDING':
            return {
                "key": "Waiting Delivery"
            }
        if obj.key == 'LOST':
            return {
                "key": "Lost Sale"
            }


class CashOutAccountSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)
    key = serializers.SerializerMethodField('get_key')

    class Meta:
        model = CashOutAccount
        fields = ('id', 'transaction_id', 'expense', 'create_date', 'due_date', 'key')

    def get_key(self, obj):
        user_id = self.context.get("lang")
        # if user_id == 'ar':
        #     if obj.key == 'WAITING':
        #         return {
        #             "key": "جاري تحضير المبلغ"
        #         }
        #     if obj.key == 'TRANSFERRED':
        #         return {
        #             "key": "تم التحويل"
        #         }
        if obj.key == 'WAITING':
            return {
                "key": "Preparing Payment"
            }
        if obj.key == 'TRANSFERRED':
            return {
                "key": "Amount Transferred"
            }
