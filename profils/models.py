from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models
from decimal import Decimal
# Create your models here.
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from countrymgt.models import CityManagement, CountryManager, CityZone


def trader_path(instance, filename):
    return 'Profile/{0}/{1}'.format(instance.name, filename)


def supporter_path(instance, filename):
    return 'Team/{0}/{1}'.format(instance.name, filename)


class UsersProfiles(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True, default='No Address')
    postal_code = models.CharField(max_length=50, null=True, blank=True, default='No Postal Code')
    symbl = models.CharField(max_length=50, blank=True, null=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True, default='No Area')
    lat = models.DecimalField(max_digits=50, decimal_places=8, default=0.00, null=True, blank=True)
    long = models.DecimalField(max_digits=50, decimal_places=8, default=0.00, null=True, blank=True)
    terms = models.BooleanField(default=True, null=True, blank=True)
    trader_name = models.CharField(max_length=150, null=True, blank=True)
    is_trader = models.BooleanField(default=False, null=True, blank=True)
    farm_name = models.CharField(max_length=150, null=True, blank=True)
    is_farm = models.BooleanField(default=False, null=True, blank=True)
    approve = models.BooleanField(default=False, null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.trader_name = self.name.last_name + ' Trader'
            self.farm_name = self.name.last_name + ' Farm'
        super(UsersProfiles, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name.first_name} {self.name.last_name}'


class ProfilePhotos(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.ForeignKey(UsersProfiles, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.FileField(blank=True, null=True,
                             default="farm_default.jpg", upload_to=trader_path,
                             validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])


class ProfilesZone(models.Model):
    user = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey(CityZone, on_delete=models.SET_NULL, null=True, blank=True)


class ProfilesMSG(models.Model):
    user = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    msg = models.TextField(null=True, blank=True)
    smal_msg = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=True, null=True)
    is_admin = models.BooleanField(default=True, null=True)


def Tokencreatoruser(sender, instance, created, *args, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)


post_save.connect(Tokencreatoruser, sender=User)


class TraderTransData(models.Model):
    benfec = models.OneToOneField(UsersProfiles, on_delete=models.CASCADE, null=True, blank=True)
    current = models.TextField(null=True, blank=True, default='No Account Data')
    new = models.TextField(null=True, blank=True)
    change = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)


def supplierBankAccount(sender, instance, created, *args, **kwargs):
    if instance.is_trader:
        TraderTransData.objects.get_or_create(benfec=instance)
    if instance.is_farm:
        TraderTransData.objects.get_or_create(benfec=instance)


post_save.connect(supplierBankAccount, sender=UsersProfiles)


class SupporterProfiles(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True, default='No Address')
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(blank=True, null=True, upload_to=supporter_path,
                            validators=[FileExtensionValidator(['png', 'jpeg', 'jpg', 'pdf'])])
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True,
                                     blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    terms = models.BooleanField(default=True, null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
