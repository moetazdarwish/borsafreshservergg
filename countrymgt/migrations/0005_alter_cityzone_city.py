# Generated by Django 4.0 on 2022-06-20 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countrymgt', '0004_cityzone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityzone',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countrymgt.citymanagement'),
        ),
    ]
