# Generated by Django 4.0 on 2022-06-22 22:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmgt', '0004_alter_expensesaccount_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesaccount',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 30), null=True),
        ),
    ]
