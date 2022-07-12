from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(OrderTracking)
admin.site.register(SubOrderTracking)
admin.site.register(SubOrderReview)
