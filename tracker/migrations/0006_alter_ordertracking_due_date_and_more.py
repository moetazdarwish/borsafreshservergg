# Generated by Django 4.0 on 2022-06-28 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_alter_ordertracking_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertracking',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 29), null=True),
        ),
        migrations.AlterField(
            model_name='subordertracking',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 29), null=True),
        ),
    ]
