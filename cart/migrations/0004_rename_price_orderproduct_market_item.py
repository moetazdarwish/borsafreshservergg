# Generated by Django 4.0 on 2022-06-18 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_orderproduct_box_supplier_alter_orderproduct_is_box_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='price',
            new_name='market_item',
        ),
    ]
