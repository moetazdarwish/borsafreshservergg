# Generated by Django 4.0 on 2022-06-24 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegefarm', '0006_farmproductsbulk_alter_farmproducts_inventory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 27), null=True),
        ),
        migrations.AlterField(
            model_name='farmproductsbulk',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 27), null=True),
        ),
    ]
