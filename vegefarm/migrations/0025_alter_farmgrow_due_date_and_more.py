# Generated by Django 4.0 on 2022-07-08 23:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegefarm', '0024_alter_farmgrow_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmgrow',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 8, 8), null=True),
        ),
        migrations.AlterField(
            model_name='farmproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 8, 8), null=True),
        ),
        migrations.AlterField(
            model_name='farmproductsbulk',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 8, 8), null=True),
        ),
        migrations.AlterField(
            model_name='farmsellingproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 8, 8), null=True),
        ),
        migrations.AlterField(
            model_name='sellingfarmbulkproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 8, 8), null=True),
        ),
    ]
