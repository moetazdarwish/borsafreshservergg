# Generated by Django 4.0 on 2022-06-21 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countrymgt', '0007_cityzone_country_cityzone_customer_percent_and_more'),
        ('profils', '0002_tradertransdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilesZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='countrymgt.cityzone')),
            ],
        ),
    ]
