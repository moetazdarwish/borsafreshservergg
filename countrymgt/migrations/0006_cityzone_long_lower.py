# Generated by Django 4.0 on 2022-06-20 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countrymgt', '0005_alter_cityzone_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityzone',
            name='long_lower',
            field=models.DecimalField(blank=True, decimal_places=8, default=0.0, max_digits=50, null=True),
        ),
    ]