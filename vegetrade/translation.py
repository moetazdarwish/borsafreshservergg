from .models import *
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

# @register(CategoryProducts)
# class FooTR(TranslationOptions):
#     fields = (
#         'name',
#     )