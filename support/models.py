from django.core.validators import FileExtensionValidator
from django.db import models

from cart.models import Orders
from profils.models import UsersProfiles, SupporterProfiles
from vegefarm.models import FarmGrow
from .fields import FAQFEILD, TIKETDEP, SUPPORTACTION, STATACTION, TIKETSTS


# Create your models here.
def support_path(instance, filename):
    return 'Support/{0}/{1}'.format(instance.ticket.subject, filename)


def farm_support_path(instance, filename):
    return 'FarmSupport/{0}/{1}'.format(instance, filename)


class FAQSupport(models.Model):
    subject = models.CharField(max_length=100, null=True, blank=True)
    subject_sc = models.CharField(max_length=100, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    answer_sc = models.TextField(null=True, blank=True)
    faq_section = models.CharField(max_length=100, null=True, blank=True, choices=FAQFEILD, )
    country = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.faq_section

    class Meta:
        ordering = ['-create_date']


class SupportContact(models.Model):
    contact = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    contact_link = models.CharField(max_length=50, blank=True, null=True)


class TicketSupport(models.Model):
    user = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    dep = models.CharField(max_length=100, null=True, blank=True, choices=TIKETDEP, )
    status = models.CharField(max_length=100,default='OPEN', null=True, blank=True, choices=TIKETSTS, )
    country = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.dep

    class Meta:
        ordering = ['-create_date']


class TicketFiles(models.Model):
    ticket = models.ForeignKey(TicketSupport, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    files = models.FileField(blank=True, null=True, upload_to=support_path,
                             validators=[FileExtensionValidator(['png', 'jpeg', 'jpg', 'pdf'])])


class TicketAnswers(models.Model):
    user = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    ticket = models.ForeignKey(TicketSupport, on_delete=models.SET_NULL, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    dep = models.CharField(max_length=100, null=True, blank=True, choices=TIKETDEP, )
    country = models.CharField(max_length=50, blank=True, null=True)
    reply = models.BooleanField(null=True, default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dep

    class Meta:
        ordering = ['-create_date']


class FarmMacth(models.Model):
    supporter = models.ForeignKey(SupporterProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True, choices=SUPPORTACTION, default='NEW')
    action = models.CharField(max_length=100, null=True, blank=True, choices=STATACTION, default='ACTIVE')
    create_date = models.DateTimeField(auto_now_add=True)


class FarmSupport(models.Model):
    user = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    supporter = models.ForeignKey(SupporterProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, default='OPEN', null=True, blank=True, choices=TIKETSTS, )
    create_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.subject

    class Meta:
        ordering = ['-create_date']


class FarmSupportAnswers(models.Model):
    supporter = models.ForeignKey(SupporterProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    case = models.ForeignKey(FarmSupport, on_delete=models.SET_NULL, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    reply = models.BooleanField(null=True, default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer

    class Meta:
        ordering = ['-create_date']


class FarmFiles(models.Model):
    case = models.ForeignKey(FarmSupport, on_delete=models.CASCADE, null=True, blank=True)
    case_ans = models.ForeignKey(FarmSupportAnswers, on_delete=models.CASCADE, null=True, blank=True)
    files = models.FileField(blank=True, null=True, upload_to=farm_support_path,
                             validators=[FileExtensionValidator(['png', 'jpeg', 'jpg', 'pdf'])])


class FarmAdvice(models.Model):
    user = models.ForeignKey(UsersProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    supporter = models.ForeignKey(SupporterProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    grow = models.ForeignKey(FarmGrow, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    advice = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['-create_date']
