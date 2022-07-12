from django.db import models

# Create your models here.
from django.db.models.signals import post_save

from accountmgt.models import ExpensesAccount, CashOutAccount, RefundAccount
from profils.models import UsersProfiles
from tracker.models import OrderTracking, SubOrderTracking


class SupplierNotif(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    body = models.CharField(max_length=50, blank=True, null=True)
    trader = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    read = models.BooleanField(default=False, )
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-create_date']

def supplierSupplierNotif(sender, instance, created, *args, **kwargs):
    if created:
        SupplierNotif.objects.create(trader=instance.trader, title=instance.transaction_id, body=instance.status, )


post_save.connect(supplierSupplierNotif, sender=SubOrderTracking)


def expencesNotif(sender, instance, created, *args, **kwargs):
    if created:
        if instance.key == 'PENDING':
            SupplierNotif.objects.create(trader=instance.supplier,
                                         title=instance.transaction_id, body="Waiting Delivery")
        if instance.key == 'LOST':
            SupplierNotif.objects.create(trader=instance.supplier,
                                         title=instance.transaction_id, body="Lost Sale")


post_save.connect(expencesNotif, sender=ExpensesAccount)

def cashoutNotif(sender, instance, created, *args, **kwargs):
    if created:
        if instance.key == 'WAITING':
            SupplierNotif.objects.create(trader=instance.supplier,
                                         title=instance.transaction_id, body="Preparing to transfer money")
        if instance.key == 'TRANSFERRED':
            SupplierNotif.objects.create(trader=instance.supplier,
                                         title=instance.transaction_id, body="Amount Transferred " + instance.expense)


post_save.connect(cashoutNotif, sender=CashOutAccount)


class UserNotif(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, )
    body = models.CharField(max_length=50, blank=True, null=True, )
    name = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    read = models.BooleanField(default=False, )
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-create_date']

def orderUserNotif(sender, instance, created, *args, **kwargs):
    if created:
        UserNotif.objects.create(name=instance.name, title=instance.transaction_id, body=instance.status, )


post_save.connect(orderUserNotif, sender=OrderTracking)

def refundNotif(sender, instance, created, *args, **kwargs):
    if created:
        if instance.key == 'PENDING':
            UserNotif.objects.create(name=instance.user_trans,
                                         title=instance.transaction_id, body="Preparing to Refund")
        if instance.key == 'TRANSFERRED':
            UserNotif.objects.create(name=instance.user_trans,
                                         title=instance.transaction_id, body="Amount Transferred" +instance.expense)


post_save.connect(refundNotif, sender=RefundAccount)


class FarmTradeNotif(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    body = models.CharField(max_length=50, blank=True, null=True)
    trader = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    read = models.BooleanField(default=False, )
    create_date = models.DateTimeField(auto_now_add=True)


class SupporterNotif(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    body = models.CharField(max_length=50, blank=True, null=True)
    trader = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    read = models.BooleanField(default=False, )
    create_date = models.DateTimeField(auto_now_add=True)