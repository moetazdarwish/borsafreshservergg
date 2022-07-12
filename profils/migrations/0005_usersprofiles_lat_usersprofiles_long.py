# Generated by Django 4.0 on 2022-06-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0004_usersprofiles_zone_alter_usersprofiles_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersprofiles',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=8, default=0.0, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='usersprofiles',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=8, default=0.0, max_digits=50, null=True),
        ),
    ]