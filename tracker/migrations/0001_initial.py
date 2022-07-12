# Generated by Django 4.0 on 2022-06-23 17:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profils', '0005_usersprofiles_lat_usersprofiles_long'),
        ('cart', '0013_orderproduct_bulk_farm_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubOrderTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.IntegerField(blank=True, null=True)),
                ('transaction_id', models.IntegerField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, default=datetime.date(2022, 6, 24), null=True)),
                ('status', models.CharField(blank=True, choices=[('ORDER RECEIVED', 'ORDER RECEIVED'), ('PROCESSING', 'PROCESSING'), ('DELIVERY OUT', 'DELIVERY OUT'), ('DELIVERED', 'DELIVERED'), ('UNABLE TO DELIVER ONE ITEM', 'UNABLE TO DELIVER ONE ITEM'), ('CANCELLED', 'CANCELLED')], max_length=50, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.orders')),
                ('sub_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.orderproduct')),
                ('trader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='SubOrderReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(blank=True, default=0, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
                ('sub_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.orderproduct')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='OrderTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('ORDER RECEIVED', 'ORDER RECEIVED'), ('PROCESSING', 'PROCESSING'), ('DELIVERY OUT', 'DELIVERY OUT'), ('DELIVERED', 'DELIVERED'), ('UNABLE TO DELIVER ONE ITEM', 'UNABLE TO DELIVER ONE ITEM'), ('CANCELLED', 'CANCELLED')], max_length=50, null=True)),
                ('due_date', models.DateField(blank=True, default=datetime.date(2022, 6, 24), null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.orders')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]