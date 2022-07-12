# Generated by Django 4.0 on 2022-06-23 01:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vegetrade', '0013_alter_products_inventory_alter_productsbox_inventory_and_more'),
        ('cart', '0009_alter_orderproduct_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='bulk_market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vegetrade.productsbulk'),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='bulk_supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vegetrade.sellingbulkproducts'),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='is_bulk',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='weight',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
