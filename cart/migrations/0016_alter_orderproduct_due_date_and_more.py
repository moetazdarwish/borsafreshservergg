# Generated by Django 4.0 on 2022-06-25 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0015_alter_orderproduct_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 26), null=True),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(blank=True, choices=[('CREATED', 'CREATED'), ('CONFIRMED', 'CONFIRMED'), ('ACCEPT', 'ACCEPT'), ('REJECT', 'REJECT'), ('DELIVERY OUT', 'DELIVERY OUT'), ('DELIVERED', 'DELIVERED'), ('RESCHEDULE', 'RESCHEDULE'), ('REFUSED', 'REFUSED')], default='CREATED', max_length=50, null=True),
        ),
    ]