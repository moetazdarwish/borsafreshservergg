# Generated by Django 4.0 on 2022-06-21 20:40

import datetime
from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countrymgt', '0007_cityzone_country_cityzone_customer_percent_and_more'),
        ('vegetrade', '0007_remove_productsbox_city_remove_productsbox_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsbox',
            name='count',
        ),
        migrations.RemoveField(
            model_name='productsbox',
            name='our_profit',
        ),
        migrations.RemoveField(
            model_name='productsbox',
            name='selling_price',
        ),
        migrations.RemoveField(
            model_name='productsbox',
            name='supplier_rev',
        ),
        migrations.RemoveField(
            model_name='productsbox',
            name='zone',
        ),
        migrations.AddField(
            model_name='productsbox',
            name='status',
            field=models.CharField(blank=True, choices=[('NEW', 'NEW'), ('UPDATE', 'UPDATE')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='SellingBoxProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('supplier_rev', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('our_profit', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('count', models.PositiveIntegerField(blank=True, null=True)),
                ('symbl', models.CharField(blank=True, max_length=5, null=True)),
                ('inventory', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('inv_due_date', models.DateField(blank=True, default=datetime.date(2022, 6, 24), null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('box', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vegetrade.productsbox')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetrade.categoryproducts')),
                ('zone', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='countrymgt.cityzone')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]
