# Generated by Django 4.0 on 2022-06-30 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0020_orderproduct_is_mix_orderproduct_mix_market_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_result',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='tran_ref',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='tran_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 1), null=True),
        ),
    ]
