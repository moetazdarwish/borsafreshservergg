# Generated by Django 4.0 on 2022-06-20 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegefarm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 24), null=True),
        ),
        migrations.AlterField(
            model_name='farmsellingproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 24), null=True),
        ),
    ]