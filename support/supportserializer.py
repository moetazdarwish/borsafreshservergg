from rest_framework import serializers

from support.models import FAQSupport, FarmAdvice, FarmSupportAnswers, TicketAnswers, FarmMacth, FarmSupport, FarmFiles


# user
class FAQSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField('get_subject')
    answer = serializers.SerializerMethodField('get_answer')

    class Meta:
        model = FAQSupport
        fields = ['subject', 'answer']

    def get_subject(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            return obj.subject_sc
        return obj.subject

    def get_answer(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            return obj.answer_sc
        return obj.answer


# farmer
class AdvieceSerializer(serializers.ModelSerializer):
    grow = serializers.SerializerMethodField('get_grow')

    class Meta:
        model = FarmAdvice
        fields = ['id', 'subject', 'advice', 'grow']

    def get_grow(self, obj):
        user_id = self.context.get("lang")
        if user_id == 'ar':
            return {
                "product_data": obj.grow.product.name_sc,
                "photo_data": obj.grow.product.photo.url
            }
        return {
            "photo_data": obj.grow.product.photo.url,
            "product_data": obj.grow.product.name
        }


class SupportAnswerSerializer(serializers.ModelSerializer):
    case = serializers.SerializerMethodField('get_case')

    class Meta:
        model = FarmSupportAnswers
        fields = ['id', 'case', 'answer']

    def get_case(self, obj):
        return {
            "case": obj.case.subject
        }


# Supporter
class SupportMatchSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user')
    create_date = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = FarmMacth
        fields = ['id', 'user', 'create_date']

    def get_user(self, obj):
        return {
            "farm": obj.user.farm_name,
            "country": obj.user.country
        }


class SupportQuestSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = FarmSupport
        fields = ['id', 'subject', 'question', 'create_date']


class SupportPhotoSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField('get_files')

    class Meta:
        model = FarmFiles
        fields = ['id', 'files']

    def get_files(self, obj):
        return {
            "files": obj.files.url,
        }
