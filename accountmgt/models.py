import datetime
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.db.models.signals import post_save, pre_save

from cart.models import Orders, OrderProduct
from countrymgt.models import CountryManager, CityManagement, CityZone
from profils.models import UsersProfiles
from vegetrade.models import Products


class ExpensesAccount(models.Model):
    order_product = models.ForeignKey(OrderProduct, models.CASCADE, null=True, blank=True)
    supplier = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    transaction_id = models.PositiveIntegerField(null=True, blank=True)
    symbl = models.CharField(max_length=5, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    expense = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    key = models.CharField(max_length=30, blank=True, null=True, )

    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-create_date']


def expensesAdjustment(sender, instance, **kwargs):
    instance.city = instance.zone.city.city
    instance.country = instance.zone.country.country


pre_save.connect(expensesAdjustment, sender=ExpensesAccount)


class CashOutAccount(models.Model):
    order_product = models.ForeignKey(OrderProduct, models.CASCADE, null=True, blank=True)
    supplier = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    transaction_id = models.PositiveIntegerField(null=True, blank=True)
    symbl = models.CharField(max_length=5, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    expense = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    key = models.CharField(max_length=30, blank=True, null=True, )
    due_date = models.DateField(blank=True, null=True, )
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-due_date']


def cashoutAdjustment(sender, instance,created, **kwargs):
    if created:
        instance.city = instance.zone.city.city
        instance.country = instance.zone.country.country
        current = datetime.date.today()
        n = instance.zone.duedate
        instance.due_date = current + datetime.timedelta(n)
        instance.save()
post_save.connect(cashoutAdjustment, sender=CashOutAccount)


class RevenueAccount(models.Model):
    order_product = models.ForeignKey(OrderProduct, models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    transaction_id = models.PositiveIntegerField(null=True, blank=True)
    symbl = models.CharField(max_length=5, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    key = models.CharField(max_length=30, blank=True, null=True, )
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-create_date']
def revenueAdjustment(sender, instance, **kwargs):
    instance.city = instance.zone.city.city
    instance.country = instance.zone.country.country


pre_save.connect(revenueAdjustment, sender=RevenueAccount)

class PaymentAccount(models.Model):
    user_trans = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    order_product = models.ManyToManyField(OrderProduct, blank=True)
    order = models.ManyToManyField(Orders, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    transaction_id = models.PositiveIntegerField(null=True, blank=True)
    transaction_ref = models.CharField(max_length=100, null=True, blank=True)
    symbl = models.CharField(max_length=5, null=True, blank=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    key = models.CharField(max_length=30, blank=True, null=True, )
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-create_date']


def paymentAdjustment(sender, instance, **kwargs):
    instance.city = instance.user_trans.city
    instance.country = instance.user_trans.country
    instance.symbl = instance.user_trans.symbl

pre_save.connect(paymentAdjustment, sender=PaymentAccount)




class IncomeAccount(models.Model):
    order = models.ForeignKey(Orders, models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    transaction_id = models.PositiveIntegerField(null=True, blank=True)
    symbl = models.CharField(max_length=5, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    key = models.CharField(max_length=30, blank=True, null=True, )
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-create_date']


def incomeAdjustment(sender, instance, **kwargs):
    instance.city = instance.zone.city.city
    instance.country = instance.zone.country.country


pre_save.connect(incomeAdjustment, sender=IncomeAccount)


class TAXAccount(models.Model):
    order = models.ForeignKey(Orders, models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    transaction_id = models.PositiveIntegerField(null=True, blank=True)
    symbl = models.CharField(max_length=5, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    key = models.CharField(max_length=30, blank=True, null=True, )
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


def taxAdjustment(sender, instance, **kwargs):
    instance.city = instance.zone.city.city
    instance.country = instance.zone.country.country


pre_save.connect(taxAdjustment, sender=TAXAccount)


class RefundAccount(models.Model):
    order = models.ForeignKey(Orders, models.CASCADE, null=True, blank=True)
    order_item = models.ForeignKey(OrderProduct, models.CASCADE, null=True, blank=True)
    user_trans = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    transaction_id = models.PositiveIntegerField(null=True, blank=True)
    symbl = models.CharField(max_length=5, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True, )
    expense = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    key = models.CharField(max_length=30, blank=True, null=True, )
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-create_date']


def refundjustment(sender, instance, **kwargs):
    instance.city = instance.zone.city.city
    instance.country = instance.zone.country.country
    current = datetime.date.today()
    n = instance.zone.duedate
    instance.due_date = current + datetime.timedelta(n)


pre_save.connect(refundjustment, sender=RefundAccount)


def expence_journal(sender, instance, created, *args, **kwargs, ):
    if instance.status == 'ACCEPT':
        ExpensesAccount.objects.create(title='Selling Expense', order_product=instance, zone=instance.zone
                                       , symbl=instance.symbl, supplier=instance.trader,
                                       transaction_id=instance.transaction_id, expense=instance.get_suppier_total,
                                       key='PENDING')
    if instance.status == 'REFUSED' or instance.status == 'CANCELLED':
        ExpensesAccount.objects.create(title='Lost Selling', order_product=instance, zone=instance.zone
                                       , symbl=instance.symbl, supplier=instance.trader,
                                       transaction_id=instance.transaction_id, expense=instance.get_suppier_total * -1,
                                       key='LOST')
        RefundAccount.objects.create(title='Refund Sub Expense', order=instance.order, order_item=instance,
                                     zone=instance.zone
                                     , symbl=instance.symbl, user_trans=instance.order.name,
                                     transaction_id=instance.transaction_id, expense=instance.get_suppier_total,
                                     key='PENDING')
        IncomeAccount.objects.create(title='Lost Sub Income', order=instance.order
                                     , zone=instance.zone, symbl=instance.symbl,
                                     transaction_id=instance.transaction_id, total=instance.get_total * -1, key='LOST')
    if instance.status == 'DELIVERED':
        RevenueAccount.objects.create(title='Selling Income', order_product=instance
                                      , zone=instance.zone, symbl=instance.symbl,
                                      transaction_id=instance.transaction_id, profit=instance.get_profit_total)
        CashOutAccount.objects.create(title='Selling Expense', order_product=instance, zone=instance.zone
                                      , symbl=instance.symbl, supplier=instance.trader,
                                      transaction_id=instance.transaction_id, expense=instance.get_suppier_total,
                                      key='WAITING')
        # CashOutAccount.objects.create(title='Tax Expense', order_product=instance, zone=instance.zone
        #                               , symbl=instance.symbl, supplier=instance.trader,
        #                               transaction_id=instance.transaction_id, expense=instance.get_sub_tax,
        #                               key='WAITING')


post_save.connect(expence_journal, sender=OrderProduct)


def revenue_journal(sender, instance, created, *args, **kwargs):
    if instance.status == 'PAID':
        IncomeAccount.objects.create(title='Selling Income', order=instance
                                     , zone=instance.zone, symbl=instance.symbl,
                                     transaction_id=instance.transaction_id, total=instance.total, key='GAIN')

        # TAXAccount.objects.create(title='Sales Tax', order=instance, zone=instance.zone, symbl=instance.symbl,
        #                           transaction_id=instance.transaction_id, sub_total=instance.sub_total,
        #                           tax_amount=instance.tax_amount, shipping=instance.shipping,
        #                           key='PENDING')
    if instance.status == 'LOST':
        # RefundAccount.objects.create(title='Refund Expense', order=instance, zone=instance.zone
        #                              , symbl=instance.symbl, user_trans=instance.name,
        #                              transaction_id=instance.transaction_id, expense=instance.total,
        #                              key='PENDING')
        IncomeAccount.objects.create(title='Lost Income', order=instance
                                     , zone=instance.zone, symbl=instance.symbl,
                                     transaction_id=instance.transaction_id, total=instance.total * -1, key='LOST')


post_save.connect(expence_journal, sender=Orders)
