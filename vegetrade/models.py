from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models
import datetime
from decimal import Decimal
# Create your models here.
from django.db.models import Min
from django.db.models.signals import pre_save, post_save, pre_delete

from countrymgt.models import CityZone
from profils.models import UsersProfiles, ProfilesZone
from vegetrade.filed import *


class CategoryList(models.Model):
    category_name = models.CharField(max_length=30, null=True, blank=True)
    approved = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f'{self.category_name} - {self.id}'


def product_path(instance, filename):
    return 'Products/{0}/{1}'.format(instance.name, filename)

class CountryTransLang(models.Model):
    box_name = models.CharField(max_length=50, null=True, blank=True)
    box_name_sc = models.CharField(max_length=50, null=True, blank=True)
    scale = models.CharField(max_length=50, null=True, blank=True)
    scale_sc = models.CharField(max_length=50, null=True, blank=True)
    retail = models.CharField(max_length=50, null=True, blank=True)
    retail_sc = models.CharField(max_length=50, null=True, blank=True)
    st_accept = models.CharField(max_length=50, null=True, blank=True)
    st_accept_sc = models.CharField(max_length=50, null=True, blank=True)
    st_confirmed = models.CharField(max_length=50, null=True, blank=True)
    st_confirmed_sc = models.CharField(max_length=50, null=True, blank=True)
    st_delivery = models.CharField(max_length=50, null=True, blank=True)
    st_delivery_sc = models.CharField(max_length=50, null=True, blank=True)
    st_delivered = models.CharField(max_length=50, null=True, blank=True)
    st_delivered_sc = models.CharField(max_length=50, null=True, blank=True)
    st_reschedule = models.CharField(max_length=50, null=True, blank=True)
    st_reschedule_sc = models.CharField(max_length=50, null=True, blank=True)
    st_refused = models.CharField(max_length=50, null=True, blank=True)
    st_refused_sc = models.CharField(max_length=50, null=True, blank=True)
    st_cancelled = models.CharField(max_length=50, null=True, blank=True)
    st_cancelled_sc = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, blank=True, null=True)

class CategoryProducts(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    name_sc = models.CharField(max_length=30, null=True, blank=True)
    category = models.ForeignKey(CategoryList, null=True, blank=True, on_delete=models.CASCADE)
    photo = models.FileField(blank=True, null=True, default="default.png", upload_to=product_path,
                             validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    lang = models.ForeignKey(CountryTransLang, null=True, blank=True, on_delete=models.CASCADE)
    packing_info = models.TextField(blank=True, null=True)
    quality_info = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    approved = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.id} '


def due_date():
    current = datetime.date.today()
    return current + datetime.timedelta(3)


class Products(models.Model):
    trader = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    symbl = models.CharField(max_length=5, null=True, blank=True)
    inventory = models.PositiveIntegerField(default=0, null=True, blank=True, )
    inv_due_date = models.DateField(blank=True, null=True, default=due_date())
    scale = models.CharField(max_length=5, null=True, blank=True)
    status = models.CharField(max_length=20, blank=True, null=True, choices=PRODUCTFIELD, default='NEW')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.trader} - {self.id} '

    class Meta:
        ordering = ['-create_date']

    @property
    def getdueday(self):
        days = self.inv_due_date - self.create_date.date()
        return days.days


def productPriceupdate(sender, instance, created, *args, **kwargs):
    if instance.status == 'NEW':
        get_zone = ProfilesZone.objects.filter(user=instance.trader)
        for i in get_zone:
            ProductZone.objects.create(product=instance, zone=i.zone)


post_save.connect(productPriceupdate, sender=Products)


def deleteProduct(sender, instance, *args, **kwargs):
    productzone = SellingProducts.objects.filter(supplier=instance)
    for i in productzone:
        i.inventory = 0
        i.save()


pre_delete.connect(deleteProduct, sender=Products)


class ProductZone(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                        blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    supplier_rev = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                       blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    our_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                     blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']


def zoneAcc(sender, instance, *args, **kwargs):
    instance.price = instance.product.price
    instance.selling_price = instance.product.price * instance.zone.customer_percent
    instance.supplier_rev = instance.product.price * instance.zone.trader_percent
    instance.our_profit = instance.selling_price - instance.supplier_rev


pre_save.connect(zoneAcc, sender=ProductZone)


def zonePrice(sender, instance, *args, **kwargs):
    today = datetime.datetime.now().date()
    obj = ProductZone.objects.filter(zone=instance.zone, product__product=instance.product.product,
                                     product__inv_due_date__gte=today,
                                     product__inventory__gt=0).aggregate(product__price=Min('price'))['product__price']
    obj_2 = ProductZone.objects.filter(zone=instance.zone, product__product=instance.product.product,
                                       product__inv_due_date__gte=today, price=obj,
                                       product__inventory__gt=0, ).first()
    get_product, create = SellingProducts.objects.get_or_create(product=instance.product.product, zone=instance.zone)
    if obj_2:
        get_product.supplier = obj_2.product
        get_product.selling_price = obj_2.selling_price
        get_product.supplier_rev = obj_2.supplier_rev
        get_product.our_profit = obj_2.our_profit
        get_product.symbl = obj_2.product.symbl
        get_product.inventory = obj_2.product.inventory
        get_product.inv_due_date = obj_2.product.inv_due_date
        get_product.save()
    else:
        get_product.delete()


post_save.connect(zonePrice, sender=ProductZone)


class SellingProducts(models.Model):
    product = models.ForeignKey(CategoryProducts, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)

    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                        blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    supplier_rev = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                       blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    our_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                     blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    zone = models.OneToOneField(CityZone, on_delete=models.SET_NULL, null=True, blank=True)
    symbl = models.CharField(max_length=5, null=True, blank=True)
    inventory = models.PositiveIntegerField(default=0, null=True, blank=True)
    inv_due_date = models.DateField(blank=True, null=True, default=due_date())
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.product.name} '

    class Meta:
        ordering = ['-create_date']


def zoneSellingPrice(sender, instance, *args, **kwargs):
    today = datetime.datetime.now().date()
    obj = ProductZone.objects.filter(zone=instance.zone, product__product=instance.product,
                                     product__inv_due_date__gte=today,
                                     product__inventory__gt=0).aggregate(product__price=Min('price'))['product__price']
    obj_2 = ProductZone.objects.filter(zone=instance.zone, product__product=instance.product,
                                       product__inv_due_date__gte=today, price=obj,
                                       product__inventory__gt=0, ).first()
    if obj_2:
        instance.supplier = obj_2.product
        instance.selling_price = obj_2.selling_price
        instance.supplier_rev = obj_2.supplier_rev
        instance.our_profit = obj_2.our_profit
        instance.symbl = obj_2.product.symbl
        instance.inventory = obj_2.product.inventory
        instance.inv_due_date = obj_2.product.inv_due_date
    else:
        instance.delete()


pre_save.connect(zoneSellingPrice, sender=SellingProducts)


# Mixed Box
class ProductsBox(models.Model):
    trader = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE, null=True, blank=True)
    box_name = models.CharField(max_length=25, null=True, blank=True, default='Mixed Items')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    symbl = models.CharField(max_length=5, null=True, blank=True)
    inventory = models.PositiveIntegerField(default=0, null=True, blank=True, )
    inv_due_date = models.DateField(blank=True, null=True, default=due_date())
    status = models.CharField(max_length=20, blank=True, null=True, choices=PRODUCTFIELD)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.trader} - {self.id} '

    class Meta:
        ordering = ['-create_date']

    @property
    def countItems(self):
        boxitems = self.mixedbox_set.all().count()

        return boxitems

    @property
    def getdueday(self):
        days = self.inv_due_date - self.create_date.date()
        return days.days


def productboxCount(sender, instance, *args, **kwargs):
    if instance.status == 'NEW':
        count = instance.countItems

        get_zone = ProfilesZone.objects.filter(user=instance.trader)
        for i in get_zone:
            selling_price = instance.price * i.zone.customer_percent
            supplier_rev = instance.price * i.zone.trader_percent
            our_profit = selling_price - supplier_rev
            SellingBoxProducts.objects.create(box=instance, product=instance.product, zone=i.zone,
                                              selling_price=selling_price,
                                              supplier_rev=supplier_rev, our_profit=our_profit, count=count,
                                              symbl=i.zone.country.symbl
                                              , inventory=instance.inventory,
                                              inv_due_date=instance.inv_due_date)


post_save.connect(productboxCount, sender=ProductsBox)


def productboxDelete(sender, instance, *args, **kwargs):
    MixedBox.objects.filter(box=instance).delete()
    SellingBoxProducts.objects.filter(box=instance).delete()


pre_delete.connect(productboxDelete, sender=ProductsBox)


class MixedBox(models.Model):
    box = models.ForeignKey(ProductsBox, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE, null=True, blank=True)
    scale = models.CharField(max_length=5, null=True, blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, null=True,
                                 blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.box.box_name} - {self.items} '

    class Meta:
        ordering = ['-create_date']


class SellingBoxProducts(models.Model):
    box = models.ForeignKey(ProductsBox, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                        blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    supplier_rev = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                       blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    our_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                     blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    count = models.PositiveIntegerField(null=True, blank=True, )
    symbl = models.CharField(max_length=5, null=True, blank=True)
    inventory = models.PositiveIntegerField(default=0, null=True, blank=True)
    inv_due_date = models.DateField(blank=True, null=True, default=due_date())
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.box.box_name} '

    class Meta:
        ordering = ['-create_date']


# Bulk product
class ProductsBulk(models.Model):
    trader = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    symbl = models.CharField(max_length=5, null=True, blank=True)
    inventory = models.PositiveIntegerField(default=0, null=True, blank=True, )
    inv_due_date = models.DateField(blank=True, null=True, default=due_date())
    scale = models.CharField(max_length=5, null=True, blank=True)
    weight = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20, blank=True, null=True, choices=PRODUCTFIELD)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.trader} - {self.id} '

    class Meta:
        ordering = ['-create_date']

    @property
    def get_itemPrice(self):
        item_p = self.price / self.weight
        return item_p


def bulkPriceUpdate(sender, instance, *args, **kwargs):
    if instance.status == 'NEW':
        get_zone = ProfilesZone.objects.filter(user=instance.trader)
        itemPrice = instance.get_itemPrice
        for i in get_zone:
            ProductBulkZone.objects.create(product=instance, zone=i.zone, item_price=itemPrice)

    if instance.status == 'UPDATE':
        ProcductZone = ProductBulkZone.objects.filter(product=instance)
        for i in ProcductZone:
            i.save()


post_save.connect(bulkPriceUpdate, sender=ProductsBulk)


def deleteBulkProduct(sender, instance, *args, **kwargs):
    productZone = SellingBulkProducts.objects.filter(product=instance)
    for i in productZone:
        i.inventory = 0
        i.save()


pre_delete.connect(deleteBulkProduct, sender=ProductsBulk)


class ProductBulkZone(models.Model):
    product = models.ForeignKey(ProductsBulk, on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.CASCADE, null=True, blank=True)
    item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                     blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                        blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    supplier_rev = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                       blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    our_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                     blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']


def zoneBulkAcc(sender, instance, *args, **kwargs):
    instance.price = instance.product.price
    instance.selling_price = instance.product.price * instance.zone.customer_percent
    instance.supplier_rev = instance.product.price * instance.zone.trader_percent
    instance.our_profit = instance.selling_price - instance.supplier_rev


pre_save.connect(zoneBulkAcc, sender=ProductBulkZone)


def zoneBulkPrice(sender, instance, *args, **kwargs):
    today = datetime.datetime.now().date()
    obj = ProductBulkZone.objects.filter(zone=instance.zone, product__product=instance.product.product,
                                         product__inv_due_date__gte=today,
                                         product__inventory__gt=0).aggregate(item_price=Min('item_price'))['item_price']
    obj_2 = ProductBulkZone.objects.filter(zone=instance.zone, product__product=instance.product.product,
                                           product__inv_due_date__gte=today, item_price=obj,
                                           product__inventory__gt=0, ).first()

    get_product, create = SellingBulkProducts.objects.get_or_create(product=instance.product.product,
                                                                    zone=instance.zone)
    if obj_2:
        get_product.supplier = obj_2.product
        get_product.selling_price = obj_2.selling_price
        get_product.supplier_rev = obj_2.supplier_rev
        get_product.our_profit = obj_2.our_profit
        get_product.symbl = obj_2.product.symbl
        get_product.inventory = obj_2.product.inventory
        get_product.inv_due_date = obj_2.product.inv_due_date
        get_product.save()
    else:
        get_product.delete()


post_save.connect(zoneBulkPrice, sender=ProductBulkZone)


class SellingBulkProducts(models.Model):
    supplier = models.ForeignKey(ProductsBulk, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                        blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    supplier_rev = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                       blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    our_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                     blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    symbl = models.CharField(max_length=5, null=True, blank=True)
    inventory = models.PositiveIntegerField(default=0, null=True, blank=True)
    inv_due_date = models.DateField(blank=True, null=True, default=due_date())
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.product.name} '

    class Meta:
        ordering = ['-create_date']


def zoneSellingBulkPrice(sender, instance, *args, **kwargs):
    today = datetime.datetime.now().date()
    obj = ProductBulkZone.objects.filter(zone=instance.zone, product__product=instance.product,
                                         product__inv_due_date__gte=today,
                                         product__inventory__gt=0).aggregate(item_price=Min('item_price'))['item_price']
    obj_2 = ProductBulkZone.objects.filter(zone=instance.zone, product__product=instance.product,
                                           product__inv_due_date__gte=today, item_price=obj,
                                           product__inventory__gt=0, ).first()
    if obj_2:
        instance.supplier = obj_2.product
        instance.selling_price = obj_2.selling_price
        instance.supplier_rev = obj_2.supplier_rev
        instance.our_profit = obj_2.our_profit
        instance.symbl = obj_2.product.symbl
        instance.inventory = obj_2.product.inventory
        instance.inv_due_date = obj_2.product.inv_due_date
        instance.save()
    else:
        instance.delete()


pre_save.connect(zoneSellingBulkPrice, sender=SellingBulkProducts)


# Mixed Salad
class ProductsMixed(models.Model):
    trader = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    symbl = models.CharField(max_length=5, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    inventory = models.PositiveIntegerField(default=0, null=True, blank=True)
    inv_due_date = models.DateField(blank=True, null=True, default=due_date())
    scale = models.CharField(max_length=5, null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                 blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    mix_name = models.CharField(max_length=20, blank=True, null=True, )
    status = models.CharField(max_length=20, blank=True, null=True, choices=PRODUCTFIELD)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.trader} - {self.id} '

    class Meta:
        ordering = ['-create_date']


def MixedPriceUpdate(sender, instance, *args, **kwargs):
    if instance.status == 'NEW':
        get_zone = ProfilesZone.objects.filter(user=instance.trader)
        for i in get_zone:
            selling_price = instance.price * i.zone.customer_percent
            supplier_rev = instance.price * i.zone.trader_percent
            our_profit = selling_price - supplier_rev
            SellingMixedProducts.objects.create(supplier=instance, product=instance.product,
                                                zone=i.zone, selling_price=selling_price,
                                                supplier_rev=supplier_rev, our_profit=our_profit,
                                                symbl=instance.symbl, inventory=instance.inventory,
                                                inv_due_date=instance.inv_due_date)


post_save.connect(MixedPriceUpdate, sender=ProductsMixed)


def deleteMixedProduct(sender, instance, *args, **kwargs):
    SellingMixedProducts.objects.filter(supplier=instance).delete()
pre_delete.connect(deleteMixedProduct, sender=ProductsMixed)


class SellingMixedProducts(models.Model):
    supplier = models.ForeignKey(ProductsMixed, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                        blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    supplier_rev = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                       blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    our_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                     blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    symbl = models.CharField(max_length=5, null=True, blank=True)
    inventory = models.PositiveIntegerField(default=0, null=True, blank=True)
    inv_due_date = models.DateField(blank=True, null=True, default=due_date())
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.product.name} '

    class Meta:
        ordering = ['-create_date']
