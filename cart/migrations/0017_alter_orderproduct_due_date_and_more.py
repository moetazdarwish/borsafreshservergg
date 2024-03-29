# Generated by Django 4.0 on 2022-06-25 23:47

import datetime
from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_alter_orderproduct_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 27), null=True),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(blank=True, choices=[('CREATED', 'CREATED'), ('CONFIRMED', 'CONFIRMED'), ('ACCEPT', 'ACCEPT'), ('REJECT', 'REJECT'), ('DELIVERY OUT', 'DELIVERY OUT'), ('DELIVERED', 'DELIVERED'), ('RESCHEDULE', 'RESCHEDULE'), ('REFUSED', 'REFUSED'), ('CANCELLED', 'CANCELLED')], default='CREATED', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='shipping',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
    ]
