# Generated by Django 4.0 on 2022-07-03 22:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admanager', '0003_advertesing_type_alter_advertesing_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertesing',
            name='due',
            field=models.DateField(blank=True, default=datetime.date(2022, 8, 3), null=True),
        ),
    ]
