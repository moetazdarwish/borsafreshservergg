from django.db import models
import datetime
# Create your models here.
from django.db.models import Q
from django.db.models.signals import post_save, pre_save

from cart.models import Orders, OrderProduct
from profils.models import UsersProfiles
from tracker.trckfield import TRACKFIELD


def order_due_date():
    current = datetime.date.today()
    return current + datetime.timedelta(days=1)


class OrderTracking(models.Model):
    name = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_id = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, blank=True, null=True, choices=TRACKFIELD)
    due_date = models.DateField(blank=True, null=True, default=order_due_date())
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-create_date']


def orderTracking(sender, instance, *args, **kwargs):
    if instance.status == 'PAID':
        OrderTracking.objects.create(name=instance.name, order=instance, transaction_id=instance.transaction_id,
                                     status='ORDER RECEIVED')
post_save.connect(orderTracking, sender=Orders)


class SubOrderTracking(models.Model):
    trader = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True, blank=True)
    sub_order = models.ForeignKey(OrderProduct, on_delete=models.SET_NULL, null=True, blank=True)
    items = models.IntegerField(null=True, blank=True)
    transaction_id = models.IntegerField(null=True, blank=True)
    due_date = models.DateField(blank=True, null=True, default=order_due_date())
    status = models.CharField(max_length=50, blank=True, null=True, choices=TRACKFIELD)

    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # def __str__(self):
    #     return self.trader
    class Meta:
        ordering = ['-create_date']


def subOrderTracking(sender, instance, *args, **kwargs):
    if instance.status == 'CONFIRMED':
        SubOrderTracking.objects.create(trader=instance.trader, order=instance.order, sub_order=instance,
                                        items=instance.order.items
                                        , transaction_id=instance.transaction_id,
                                        status='ORDER RECEIVED')

    if instance.status == 'ACCEPT':
        SubOrderTracking.objects.create(trader=instance.trader, order=instance.order, sub_order=instance,
                                        items=instance.order.items
                                        , transaction_id=instance.transaction_id,
                                        status='PROCESSING')
        count = instance.order.items
        order_count = SubOrderTracking.objects.filter(order=instance.order, status='PROCESSING').count()
        percent = count / order_count
        if percent >= 0.5:
            OrderTracking.objects.get_or_create(name=instance.order.name, order=instance.order,
                                                transaction_id=instance.order.transaction_id,
                                                status='PROCESSING')
    if instance.status == 'REJECT':
        SubOrderTracking.objects.create(trader=instance.trader, order=instance.order, sub_order=instance,
                                        items=instance.order.items
                                        , transaction_id=instance.transaction_id,
                                        status='UNABLE TO DELIVER '+instance.product.name)
        OrderTracking.objects.create(name=instance.order.name, order=instance.order,
                                     transaction_id=instance.order.transaction_id,
                                     status='UNABLE TO DELIVER '+instance.product.name)

    if instance.status == 'DELIVERY OUT':
        SubOrderTracking.objects.create(trader=instance.trader, order=instance.order, sub_order=instance,
                                        items=instance.order.items
                                        , transaction_id=instance.transaction_id,
                                        status='DELIVERY OUT')
        count = instance.order.items
        order_count = SubOrderTracking.objects.filter(status__in=['DELIVERY OUT'],order=instance.order).count()
        percent = count / order_count
        if percent >= 0.5:
            OrderTracking.objects.create(name=instance.order.name, order=instance.order,
                                         transaction_id=instance.order.transaction_id,
                                         status='ITEMS DELIVERY OUT')
    if instance.status == 'DELIVERED':
        SubOrderTracking.objects.create(trader=instance.trader, order=instance.order, sub_order=instance,
                                        items=instance.order.items
                                        , transaction_id=instance.transaction_id,
                                        status='DELIVERED')
        OrderTracking.objects.create(name=instance.order.name, order=instance.order,
                                     transaction_id=instance.order.transaction_id,
                                     status=instance.product.name + ' DELIVERED')
        count = instance.order.items
        order_count = SubOrderTracking.objects.filter(status__in=['DELIVERED'], order=instance.order).count()
        percent = count / order_count
        if percent >= 0.9:
            get_ord = Orders.objects.get(id=instance.order.id,)
            get_ord.status='DELIVERED'
            get_ord.save()
    if instance.status == 'RESCHEDULE':
        SubOrderTracking.objects.create(trader=instance.trader, order=instance.order, sub_order=instance,
                                        items=instance.order.items
                                        , transaction_id=instance.transaction_id,
                                        status='RESCHEDULE')
        OrderTracking.objects.create(name=instance.order.name, order=instance.order,
                                     transaction_id=instance.order.transaction_id,
                                     status=instance.product.name + ' RESCHEDULE')
    if instance.status == 'REFUSED':
        SubOrderTracking.objects.create(trader=instance.trader, order=instance.order, sub_order=instance,
                                        items=instance.order.items
                                        , transaction_id=instance.transaction_id,
                                        status='REFUSED')
        OrderTracking.objects.create(name=instance.order.name, order=instance.order,
                                     transaction_id=instance.order.transaction_id,
                                     status=instance.product.name + ' REFUSED')
    if instance.status == 'CANCELLED':
        SubOrderTracking.objects.create(trader=instance.trader, order=instance.order, sub_order=instance,
                                        items=instance.order.items
                                        , transaction_id=instance.transaction_id,
                                        status='CANCELLED')
        OrderTracking.objects.create(name=instance.order.name, order=instance.order,
                                     transaction_id=instance.order.transaction_id,
                                     status='CANCELLED')

# REFUSED RESCHEDULE
post_save.connect(subOrderTracking, sender=OrderProduct)


class SubOrderReview(models.Model):
    name = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    sub_order = models.ForeignKey(OrderProduct, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True, blank=True)
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00,null=True, blank=True,)
    review = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-create_date']
def orderReviews(sender, instance, *args, **kwargs):
    instance.order = instance.sub_order.order
pre_save.connect(orderReviews, sender=SubOrderReview)
