# Generated by Django 4.0 on 2022-06-27 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0017_alter_orderproduct_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 28), null=True),
        ),
    ]
