from django.core.validators import MinValueValidator, FileExtensionValidator
from django.db import models
from decimal import Decimal
# Create your models here.
from django.db.models.signals import post_save, pre_save
def country_path(instance, filename):
    return f'Country/{instance.country}/{filename}'

class CountryManager(models.Model):
    country = models.CharField(max_length=50, blank=True, null=True)
    second_lang = models.CharField(max_length=50, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True,
                                   validators=[MinValueValidator(Decimal('0.00'))])
    tax = models.BooleanField(default=False, blank=True, null=True)
    symbl = models.CharField(max_length=5, null=True, blank=True)
    file_upload = models.FileField(blank=True, null=True,
                             default="farm_default.jpg", upload_to=country_path,
                             )
    approved = models.BooleanField(default=False, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country
    @property
    def get_countrycities(self):
        return  self.citymanagement_set.all().count()

    @property
    def get_countryzones(self):
        return self.cityzone_set.all().count()
def city_path(instance, filename):
    county = instance.country.country
    city = instance.city
    return f'Country/{county}/{city}/{filename}'
class CityManagement(models.Model):
    country = models.ForeignKey(CountryManager, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    trader_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    farm_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    custommer_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    shipping_flat = models.BooleanField(default=True, blank=True, null=True)
    file_upload = models.FileField(blank=True, null=True,
                                   default="farm_default.jpg", upload_to=city_path,
                                   validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    approved = models.BooleanField(default=False, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city
    @property
    def get_cityzones(self):
        return self.cityzone_set.all().count()


class CityZone(models.Model):
    country = models.ForeignKey(CountryManager, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(CityManagement, on_delete=models.CASCADE, null=True, blank=True)
    zone = models.CharField(max_length=50, null=True, blank=True)
    lat_greater = models.DecimalField(max_digits=50, decimal_places=8, default=0.00, null=True, blank=True)
    lat_lower = models.DecimalField(max_digits=50, decimal_places=8, default=0.00, null=True, blank=True)
    long_greater = models.DecimalField(max_digits=50, decimal_places=8, default=0.00, null=True, blank=True)
    long_lower = models.DecimalField(max_digits=50, decimal_places=8, default=0.00, null=True, blank=True)
    trader_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    farm_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    customer_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    duedate = models.PositiveIntegerField( default=7, null=True, blank=True)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    def __str__(self):
        return f'{self.city.city} {self.zone} '

    @property
    def get_trdcont(self):
        return self.profileszone_set.all().count

class NewZone(models.Model):
    lat = models.DecimalField(max_digits=50, decimal_places=8, default=0.00, null=True, blank=True)
    long = models.DecimalField(max_digits=50, decimal_places=8, default=0.00, null=True, blank=True)
    is_trader = models.BooleanField(default=False,null=True)

