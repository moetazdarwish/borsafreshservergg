# Generated by Django 4.0 on 2022-06-27 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetrade', '0016_alter_products_inv_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 30), null=True),
        ),
        migrations.AlterField(
            model_name='productsbox',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 30), null=True),
        ),
        migrations.AlterField(
            model_name='productsbulk',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 30), null=True),
        ),
        migrations.AlterField(
            model_name='sellingboxproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 30), null=True),
        ),
    ]
