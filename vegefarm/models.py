from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models
import datetime
from decimal import Decimal
# Create your models here.
from django.db.models import Min
from django.db.models.signals import pre_save, post_save, pre_delete

from countrymgt.models import CityManagement, CountryManager, CityZone
from profils.models import UsersProfiles, ProfilesZone
from vegetrade.filed import PRODUCTFIELD
from vegetrade.models import CategoryProducts


def due_date():
    current = datetime.date.today()
    return current + datetime.timedelta(30)

def farm_path(instance, filename):
    return '/Farms/{0}/{1}'.format(instance.name, filename)
class FarmProducts(models.Model):
    trader = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                blank=True, validators=[MinValueValidator(Decimal('0.00'))])

    symbl = models.CharField(max_length=5, null=True, blank=True)
    inventory = models.PositiveIntegerField(default=0, null=True, blank=True)
    inv_due_date = models.DateField(blank=True, null=True, default=due_date())
    scale = models.CharField(max_length=5, null=True, blank=True, )
    status = models.CharField(max_length=20, blank=True, null=True, choices=PRODUCTFIELD, default='NEW')
    hydro = models.BooleanField(default=True, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.trader} - {self.id} '

    class Meta:
        ordering = ['-create_date']

    @property
    def getdueday(self):
        days = self.inv_due_date - self.create_date.date()
        return days.days


def farmPriceupdate(sender, instance, created, *args, **kwargs):
    if instance.status == 'NEW':
        get_zone = ProfilesZone.objects.filter(user=instance.trader)
        for i in get_zone:
            FarmProductZone.objects.create(product=instance, zone=i.zone)


post_save.connect(farmPriceupdate, sender=FarmProducts)


def deleteFarmProduct(sender, instance, *args, **kwargs):
    productZone = FarmSellingProducts.objects.filter(product=instance)
    for i in productZone:
        i.inventory = 0
        i.save()


pre_delete.connect(deleteFarmProduct, sender=FarmProducts)


class FarmProductZone(models.Model):
    product = models.ForeignKey(FarmProducts, on_delete=models.SET_NULL, null=True, blank=True)
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


def farmzoneAcc(sender, instance, *args, **kwargs):
    instance.price = instance.product.price
    instance.selling_price = instance.product.price * instance.zone.customer_percent
    instance.supplier_rev = instance.product.price * instance.zone.farm_percent
    instance.our_profit = instance.selling_price - instance.supplier_rev


pre_save.connect(farmzoneAcc, sender=FarmProductZone)


def farmzonePrice(sender, instance, *args, **kwargs):
    today = datetime.datetime.now().date()
    obj = FarmProductZone.objects.filter(zone=instance.zone, product__product=instance.product.product,
                                         product__inv_due_date__gte=today,
                                         product__inventory__gt=0).aggregate(product__price=Min('price'))[
        'product__price']
    obj_2 = FarmProductZone.objects.filter(zone=instance.zone, product__product=instance.product.product,
                                           product__inv_due_date__gte=today, price=obj,
                                           product__inventory__gt=0, ).first()
    get_product, create = FarmSellingProducts.objects.get_or_create(product=instance.product.product,
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


post_save.connect(farmzonePrice, sender=FarmProductZone)


class FarmSellingProducts(models.Model):
    product = models.ForeignKey(CategoryProducts, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(FarmProducts, on_delete=models.CASCADE, blank=True, null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                        blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    supplier_rev = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                       blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    our_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                     blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    zone = models.OneToOneField(CityZone, on_delete=models.SET_NULL, null=True, blank=True)
    hydro = models.BooleanField(default=True, blank=True, null=True)
    symbl = models.CharField(max_length=5, null=True, blank=True)
    inventory = models.PositiveIntegerField(default=0, null=True, blank=True)
    inv_due_date = models.DateField(blank=True, null=True, default=due_date())
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.city.city} - {self.product.name} '

    class Meta:
        ordering = ['-create_date']


def farmSellingzonePrice(sender, instance, *args, **kwargs):
    today = datetime.datetime.now().date()
    obj = FarmProductZone.objects.filter(zone=instance.zone, product__product=instance.product,
                                         product__inv_due_date__gte=today,
                                         product__inventory__gt=0).aggregate(product__price=Min('price'))[
        'product__price']
    obj_2 = FarmProductZone.objects.filter(zone=instance.zone, product__product=instance.product,
                                           product__inv_due_date__gte=today, price=obj,
                                           product__inventory__gt=0).first()
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


pre_save.connect(farmSellingzonePrice, sender=FarmSellingProducts)


class FarmProductsBulk(models.Model):
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
    hydro = models.BooleanField(default=True, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.trader} - {self.id} '

    class Meta:
        ordering = ['-create_date']

    @property
    def get_itemFarmPrice(self):
        item_p = self.price / self.weight
        return item_p


def bulkPriceUpdate(sender, instance, created, *args, **kwargs):
    if instance.status == 'NEW':
        get_zone = ProfilesZone.objects.filter(user=instance.trader)
        itemPrice = instance.get_itemFarmPrice
        for i in get_zone:
            ProductFarmBulkZone.objects.create(product=instance, zone=i.zone, item_price=itemPrice)


post_save.connect(bulkPriceUpdate, sender=FarmProductsBulk)


def deleteProduct(sender, instance, *args, **kwargs):
    productZone = SellingFarmBulkProducts.objects.filter(product=instance)
    for i in productZone:
        i.inventory = 0
        i.save()


pre_delete.connect(deleteProduct, sender=FarmProductsBulk)


class ProductFarmBulkZone(models.Model):
    product = models.ForeignKey(FarmProductsBulk, on_delete=models.SET_NULL, null=True, blank=True)
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


def zoneFarmBulkAcc(sender, instance, *args, **kwargs):
    instance.price = instance.product.price
    instance.selling_price = instance.product.price * instance.zone.customer_percent
    instance.supplier_rev = instance.product.price * instance.zone.farm_percent
    instance.our_profit = instance.selling_price - instance.supplier_rev


pre_save.connect(zoneFarmBulkAcc, sender=ProductFarmBulkZone)


def zoneFarmBulkPrice(sender, instance, *args, **kwargs):
    today = datetime.datetime.now().date()
    obj = ProductFarmBulkZone.objects.filter(zone=instance.zone, product__product=instance.product.product,
                                             product__inv_due_date__gte=today,
                                             product__inventory__gt=0).aggregate(item_price=Min('item_price'))[
        'item_price']
    obj_2 = ProductFarmBulkZone.objects.filter(zone=instance.zone, product__product=instance.product.product,
                                               product__inv_due_date__gte=today, item_price=obj,
                                               product__inventory__gt=0, ).first()

    get_product, create = SellingFarmBulkProducts.objects.get_or_create(product=instance.product.product,
                                                                        zone=instance.zone)
    if obj_2:
        get_product.supplier = obj_2.product
        get_product.selling_price = obj_2.selling_price
        get_product.supplier_rev = obj_2.supplier_rev
        get_product.our_profit = obj_2.our_profit
        get_product.save()
    else:
        get_product.delete()


post_save.connect(zoneFarmBulkPrice, sender=ProductFarmBulkZone)


class SellingFarmBulkProducts(models.Model):
    supplier = models.ForeignKey(FarmProductsBulk, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                        blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    supplier_rev = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                       blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    our_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                     blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    hydro = models.BooleanField(default=True, blank=True, null=True)
    symbl = models.CharField(max_length=5, null=True, blank=True)
    inventory = models.PositiveIntegerField(default=0, null=True, blank=True)
    inv_due_date = models.DateField(blank=True, null=True, default=due_date())
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.product.name} '

    class Meta:
        ordering = ['-create_date']


def sellingFarmBulkPrice(sender, instance, *args, **kwargs):
    today = datetime.datetime.now().date()
    obj = ProductFarmBulkZone.objects.filter(zone=instance.zone, product__product=instance.product,
                                             product__inv_due_date__gte=today,
                                             product__inventory__gt=0).aggregate(item_price=Min('item_price'))[
        'item_price']
    obj_2 = ProductFarmBulkZone.objects.filter(zone=instance.zone, product__product=instance.product,
                                               product__inv_due_date__gte=today, item_price=obj,
                                               product__inventory__gt=0, ).first()
    if obj_2:
        instance.supplier = obj_2.product
        instance.selling_price = obj_2.selling_price
        instance.supplier_rev = obj_2.supplier_rev
        instance.our_profit = obj_2.our_profit
        instance.save()
    else:
        instance.delete()


pre_save.connect(sellingFarmBulkPrice, sender=SellingFarmBulkProducts)


class FarmGrow(models.Model):
    trader = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    due_date = models.DateField(blank=True, null=True, default=due_date())
    status = models.CharField(max_length=20, blank=True, null=True, default='NEW')
    city = models.CharField(max_length=50, blank=True, null=True)
    system = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.trader} - {self.id} '

    class Meta:
        ordering = ['-create_date']


class FarmPhotos(models.Model):
    name = models.ForeignKey(FarmGrow, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.FileField(blank=True, null=True,
                             default="farm_default.jpg", upload_to=farm_path,
                             validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])
