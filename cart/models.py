from django.core.validators import MinValueValidator
from django.db import models, transaction
from decimal import Decimal
import datetime
from django.db.models.signals import pre_save, post_save

from vegefarm.models import FarmSellingProducts, FarmProducts, FarmProductsBulk, SellingFarmBulkProducts
from vegetrade.models import CategoryProducts, SellingProducts, Products, ProductsBox, SellingBoxProducts, \
    SellingBulkProducts, ProductsBulk, SellingMixedProducts, ProductsMixed
from .fields import STATUS, SUBSTATUS
from countrymgt.models import CityZone
from profils.models import UsersProfiles
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

class Orders(models.Model):
    name = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True,
                                    validators=[MinValueValidator(Decimal('0.00'))])
    tax_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True,
                                   validators=[MinValueValidator(Decimal('0.00'))])
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True,
                                     validators=[MinValueValidator(Decimal('0.00'))])
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True,
                                validators=[MinValueValidator(Decimal('0.00'))])
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True,
                                validators=[MinValueValidator(Decimal('0.00'))])
    symbl = models.CharField(max_length=5, null=True, blank=True)
    items = models.IntegerField(null=True, blank=True)
    coupon = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    transaction_id = models.IntegerField(null=True, blank=True, unique=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, null=True, blank=True)
    note = models.TextField(null=True, blank=True, default='No Note')
    payment_result = models.CharField(max_length=20, null=True, blank=True)
    tran_ref = models.CharField(max_length=50, null=True, blank=True)
    tran_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    status = models.CharField(max_length=20, blank=True, null=True, choices=STATUS, default='CREATED')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.transaction_id} '

    class Meta:
        ordering = ['-create_date']

    @property
    def get_shipping(self):
        return self.zone.shipping

    # @property
    # def get_cart_tax(self):
    #     orderitems = self.orderproduct_set.all()
    #     if self.zone.country.tax:
    #         total_tax = (sum([item.get_total for item in orderitems]) + self.get_shipping) * self.zone.country.tax
    #         TWOPLACES = Decimal(10) ** -2
    #         return Decimal(total_tax).quantize(TWOPLACES)
    #     else:
    #         total_tax = 0
    #         return total_tax

    @property
    def get_cart_total(self):
        orderitems = self.orderproduct_set.all()
        total = sum([item.get_total for item in orderitems]) + self.get_shipping


        return total

    @property
    def get_cart_sub_total(self):
        orderitems = self.orderproduct_set.all()
        sub_total = sum([item.get_total for item in orderitems])
        return sub_total

    @property
    def get_cart_items(self):
        orderitems = self.orderproduct_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_date(self):
        return self.modified.date()


def createTransaction_id(sender, instance, *args, **kwargs):
    if instance.transaction_id is None:
        transaction_id = datetime.datetime.now().timestamp()
        instance.transaction_id = transaction_id

    if instance.status == 'PAID':
        # instance.tax_amount = instance.get_cart_tax
        instance.total = instance.get_cart_total
        instance.sub_total = instance.get_cart_sub_total
        instance.items = instance.get_cart_items


pre_save.connect(createTransaction_id, sender=Orders)


def orderTransaction(sender, instance, *args, **kwargs):
    if instance.status == 'PAID':
        get_orderIt = OrderProduct.objects.select_for_update().filter(order=instance)
        with transaction.atomic():
            for i in get_orderIt:
                i.transaction_id = instance.transaction_id
                i.status = 'CONFIRMED'
                i.save()
        htmly = get_template('dashboard/email.html')
        d = {'order': instance, 'sub': get_orderIt}
        subject, from_email, to = 'BorsaFresh Invoice', settings.EMAIL_HOST_USER, instance.name.name.email
        text_content = 'This is an important message.'
        html_content = htmly.render(d)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    if instance.status == 'LOST':
        get_orderIt = OrderProduct.objects.filter(order=instance)
        for i in get_orderIt:
            i.status = 'CANCELLED'
            i.save()

    if instance.status == 'DELIVER':
        get_orderIt = OrderProduct.objects.filter(order=instance)
        for i in get_orderIt:
            i.status = 'DELIVERED'
            i.save()


post_save.connect(orderTransaction, sender=Orders)


def order_due_date():
    current = datetime.date.today()
    return current + datetime.timedelta(1)


class OrderProduct(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True, blank=True)
    trader = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(CategoryProducts, on_delete=models.SET_NULL, null=True, blank=True)
    farm_item = models.ForeignKey(FarmSellingProducts, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    farm_supplier = models.ForeignKey(FarmProducts, on_delete=models.SET_NULL, null=True, blank=True)
    box_supplier = models.ForeignKey(ProductsBox, on_delete=models.SET_NULL, null=True, blank=True)
    box_market = models.ForeignKey(SellingBoxProducts, on_delete=models.SET_NULL, null=True, blank=True)
    bulk_supplier = models.ForeignKey(ProductsBulk, on_delete=models.SET_NULL, null=True, blank=True)
    bulk_market = models.ForeignKey(SellingBulkProducts, on_delete=models.SET_NULL, null=True, blank=True)
    bulk_farm_supplier = models.ForeignKey(FarmProductsBulk, on_delete=models.SET_NULL, null=True, blank=True)
    bulk_farm = models.ForeignKey(SellingFarmBulkProducts, on_delete=models.SET_NULL, null=True, blank=True)
    mix_supplier = models.ForeignKey(ProductsMixed, on_delete=models.SET_NULL, null=True, blank=True)
    mix_market = models.ForeignKey(SellingMixedProducts, on_delete=models.SET_NULL, null=True, blank=True)

    symbl = models.CharField(max_length=5, null=True, blank=True)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True,
                                    validators=[MinValueValidator(Decimal('0.00'))])
    supplier_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True,
                                         validators=[MinValueValidator(Decimal('0.00'))])
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MinValueValidator(0)])
    weight = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MinValueValidator(0)])
    transaction_id = models.IntegerField(null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, null=True, blank=True)
    scale = models.CharField(max_length=5, null=True, blank=True, default='Mix')
    box_name = models.CharField(max_length=25, null=True, blank=True, default='Single')
    is_box = models.BooleanField(null=False, blank=True, default=False)
    is_bulk = models.BooleanField(null=False, blank=True, default=False)
    is_mix = models.BooleanField(null=False, blank=True, default=False)
    is_farm_bulk = models.BooleanField(null=False, blank=True, default=False)
    hydro = models.BooleanField(default=False, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True, default=order_due_date())
    status = models.CharField(max_length=50, blank=True, null=True, choices=SUBSTATUS, default='CREATED')
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.transaction_id} '

    class Meta:
        ordering = ['-create_date']

    @property
    def get_total(self):
        total = self.buy_price * self.quantity

        return total

    @property
    def get_suppier_total(self):

        total = self.supplier_price * self.quantity
        return total

    @property
    def get_profit_total(self):
        proft = self.buy_price - self.supplier_price
        total = proft * self.quantity
        return total

    @property
    def get_subshipping(self):
        return self.zone.shipping
    # @property
    # def get_sub_tax(self):
    #     if self.zone.country.tax:
    #         total_tax = self.get_total * self.zone.country.tax_rate
    #         TWOPLACES = Decimal(10) ** -2
    #         return Decimal(total_tax).quantize(TWOPLACES)
    #     else:
    #         total_tax = 0
    #         return total_tax
