# Generated by Django 4.0 on 2022-06-18 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countrymgt', '0002_countrymanager_second_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countrymanager',
            name='shipping',
        ),
        migrations.RemoveField(
            model_name='countrymanager',
            name='shipping_flat',
        ),
    ]
