# Generated by Django 4.0 on 2022-06-24 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertracking',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 25), null=True),
        ),
        migrations.AlterField(
            model_name='ordertracking',
            name='status',
            field=models.CharField(blank=True, choices=[('ORDER RECEIVED', 'ORDER RECEIVED'), ('PROCESSING', 'PROCESSING'), ('DELIVERY OUT', 'DELIVERY OUT'), ('DELIVERED', 'DELIVERED'), ('UNABLE TO DELIVER ONE ITEM', 'UNABLE TO DELIVER ONE ITEM'), ('CANCELLED', 'CANCELLED'), ('ITEMS DELIVERY OUT', 'ITEMS DELIVERY OUT')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='suborderreview',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='subordertracking',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 25), null=True),
        ),
        migrations.AlterField(
            model_name='subordertracking',
            name='status',
            field=models.CharField(blank=True, choices=[('ORDER RECEIVED', 'ORDER RECEIVED'), ('PROCESSING', 'PROCESSING'), ('DELIVERY OUT', 'DELIVERY OUT'), ('DELIVERED', 'DELIVERED'), ('UNABLE TO DELIVER ONE ITEM', 'UNABLE TO DELIVER ONE ITEM'), ('CANCELLED', 'CANCELLED'), ('ITEMS DELIVERY OUT', 'ITEMS DELIVERY OUT')], max_length=50, null=True),
        ),
    ]
