from django.core.validators import FileExtensionValidator
from django.db import models
import datetime
# Create your models here.
from profils.models import UsersProfiles

def ads_path(instance, filename):
    return 'Ads/{0}/{1}'.format(instance.name, filename)
def due_date():
    current = datetime.date.today()
    return current + datetime.timedelta(30)
class Advertesing (models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True, default='No Address')
    postal_code = models.CharField(max_length=50, null=True, blank=True, default='No Postal Code')
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True, default='No Area')
    lat = models.DecimalField(max_digits=50, decimal_places=8, default=0.00, null=True, blank=True)
    long = models.DecimalField(max_digits=50, decimal_places=8, default=0.00, null=True, blank=True)
    logo = models.FileField(blank=True, null=True, upload_to=ads_path,
                             validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    msg = models.TextField(null=True)
    link = models.CharField(max_length=100,null=True,blank=True)
    due = models.DateField(blank=True, null=True, default=due_date())
    type = models.CharField(max_length=50, blank=True, null=True)
    terms = models.BooleanField(default=True, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_adcount(self):
        return self.adcounter_set.all().count()

class AdCounter(models.Model):
    user = models.ForeignKey(UsersProfiles,on_delete=models.SET_NULL,null=True,blank=True)
    ad = models.ForeignKey(Advertesing,on_delete=models.SET_NULL,null=True,blank=True)
    count = models.PositiveIntegerField(default=1)
    create_date = models.DateTimeField(auto_now_add=True)
