# Generated by Django 4.0 on 2022-07-08 01:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0028_alter_orderproduct_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 9), null=True),
        ),
    ]
