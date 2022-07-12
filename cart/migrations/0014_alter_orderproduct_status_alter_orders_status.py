# Generated by Django 4.0 on 2022-06-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_orderproduct_bulk_farm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(blank=True, choices=[('CREATED', 'CREATED'), ('PAID', 'PAID'), ('ACCEPT', 'ACCEPT'), ('REJECT', 'REJECT'), ('COLLECTION POINT', 'COLLECTION POINT'), ('RECEIVED', 'RECEIVED'), ('PROCESSING', 'PROCESSING'), ('ITEMS DELIVERY OUT', 'ITEMS DELIVERY OUT'), ('COLLECTION POINT', 'COLLECTION POINT'), ('READY TO DELIVERY', 'READY TO DELIVERY'), ('SHIPPED', 'SHIPPED'), ('CANCELLED', 'CANCELLED'), ('REFUND', 'REFUND'), ('REJECT', 'REJECT'), ('RETURN', 'RETURN'), ('ASSIGNED', 'ASSIGNED'), ('DELIVERY OUT', 'DELIVERY OUT'), ('DELIVERED', 'DELIVERED'), ('UNABLE TO DELIVERY', 'UNABLE TO DELIVERY'), ('PICK UP', 'PICK UP'), ('CONFIRMED', 'CONFIRMED'), ('COLLECTED', 'COLLECTED'), ('RECEIVED', 'RECEIVED'), ('TRANSFERED', 'TRANSFERED'), ('FIXED', 'FIXED'), ('RATE', 'RATE'), ('CPC', 'CPC'), ('DATE', 'DATE'), ('SPONSOR', 'SPONSOR'), ('ADPAID', 'ADPAID'), ('PENDING', 'PENDING'), ('UNEARNED REVENUE', 'UNEARNED REVENUE'), ('OFFER', 'OFFER'), ('EXECUTED', 'EXECUTED'), ('MARKET', 'MARKET'), ('OFFER REMOVED', 'OFFER REMOVED'), ('LOST SELL', 'LOST SELL')], default='CREATED', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(blank=True, choices=[('CREATED', 'CREATED'), ('PAID', 'PAID'), ('ACCEPT', 'ACCEPT'), ('REJECT', 'REJECT'), ('COLLECTION POINT', 'COLLECTION POINT'), ('RECEIVED', 'RECEIVED'), ('PROCESSING', 'PROCESSING'), ('ITEMS DELIVERY OUT', 'ITEMS DELIVERY OUT'), ('COLLECTION POINT', 'COLLECTION POINT'), ('READY TO DELIVERY', 'READY TO DELIVERY'), ('SHIPPED', 'SHIPPED'), ('CANCELLED', 'CANCELLED'), ('REFUND', 'REFUND'), ('REJECT', 'REJECT'), ('RETURN', 'RETURN'), ('ASSIGNED', 'ASSIGNED'), ('DELIVERY OUT', 'DELIVERY OUT'), ('DELIVERED', 'DELIVERED'), ('UNABLE TO DELIVERY', 'UNABLE TO DELIVERY'), ('PICK UP', 'PICK UP'), ('CONFIRMED', 'CONFIRMED'), ('COLLECTED', 'COLLECTED'), ('RECEIVED', 'RECEIVED'), ('TRANSFERED', 'TRANSFERED'), ('FIXED', 'FIXED'), ('RATE', 'RATE'), ('CPC', 'CPC'), ('DATE', 'DATE'), ('SPONSOR', 'SPONSOR'), ('ADPAID', 'ADPAID'), ('PENDING', 'PENDING'), ('UNEARNED REVENUE', 'UNEARNED REVENUE'), ('OFFER', 'OFFER'), ('EXECUTED', 'EXECUTED'), ('MARKET', 'MARKET'), ('OFFER REMOVED', 'OFFER REMOVED'), ('LOST SELL', 'LOST SELL')], default='CREATED', max_length=20, null=True),
        ),
    ]