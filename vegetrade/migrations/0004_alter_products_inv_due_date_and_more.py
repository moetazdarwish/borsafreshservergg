# Generated by Django 4.0 on 2022-06-20 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetrade', '0003_alter_products_inv_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 24), null=True),
        ),
        migrations.AlterField(
            model_name='productsbox',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 24), null=True),
        ),
        migrations.AlterField(
            model_name='sellingproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 24), null=True),
        ),
    ]
