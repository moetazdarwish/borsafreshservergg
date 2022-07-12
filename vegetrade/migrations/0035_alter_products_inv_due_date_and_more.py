# Generated by Django 4.0 on 2022-07-08 01:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetrade', '0034_alter_products_inv_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 11), null=True),
        ),
        migrations.AlterField(
            model_name='productsbox',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 11), null=True),
        ),
        migrations.AlterField(
            model_name='productsbulk',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 11), null=True),
        ),
        migrations.AlterField(
            model_name='productsmixed',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 11), null=True),
        ),
        migrations.AlterField(
            model_name='sellingboxproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 11), null=True),
        ),
        migrations.AlterField(
            model_name='sellingbulkproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 11), null=True),
        ),
        migrations.AlterField(
            model_name='sellingmixedproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 11), null=True),
        ),
        migrations.AlterField(
            model_name='sellingproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 11), null=True),
        ),
    ]
