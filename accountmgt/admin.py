from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(AccountJournal)
admin.site.register(ExpensesAccount)
admin.site.register(RevenueAccount)
admin.site.register(IncomeAccount)
admin.site.register(TAXAccount)
admin.site.register(CashOutAccount)
admin.site.register(RefundAccount)
admin.site.register(PaymentAccount)
