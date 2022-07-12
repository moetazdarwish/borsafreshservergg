# Generated by Django 4.0 on 2022-06-18 17:24

import datetime
from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import vegetrade.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countrymgt', '0001_initial'),
        ('profils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=30, null=True)),
                ('approved', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('photo', models.FileField(blank=True, default='default.png', null=True, upload_to=vegetrade.models.product_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])])),
                ('packing_info', models.TextField(blank=True, null=True)),
                ('quality_info', models.TextField(blank=True, null=True)),
                ('approved', models.BooleanField(blank=True, default=False, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetrade.categorylist')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('supplier_rev', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('our_profit', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('symbl', models.CharField(blank=True, max_length=5, null=True)),
                ('inventory', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('inv_due_date', models.DateField(blank=True, default=datetime.date(2022, 6, 21), null=True)),
                ('scale', models.CharField(blank=True, default='Mix', max_length=5, null=True)),
                ('box_name', models.CharField(blank=True, default='Single', max_length=25, null=True)),
                ('is_box', models.BooleanField(blank=True, default=False)),
                ('box_approve', models.BooleanField(blank=True, default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countrymgt.citymanagement')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countrymgt.countrymanager')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetrade.categoryproducts')),
                ('trader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='SellingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('supplier_rev', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('our_profit', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('symbl', models.CharField(blank=True, max_length=5, null=True)),
                ('inventory', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('inv_due_date', models.DateField(blank=True, default=datetime.date(2022, 6, 21), null=True)),
                ('scale', models.CharField(blank=True, default='Mix', max_length=5, null=True)),
                ('box_name', models.CharField(blank=True, default='Single', max_length=25, null=True)),
                ('is_box', models.BooleanField(blank=True, default=False, null=True)),
                ('hydro', models.BooleanField(blank=True, default=False, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countrymgt.citymanagement')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countrymgt.countrymanager')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vegetrade.categoryproducts')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetrade.products')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductsBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('supplier_rev', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('our_profit', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('symbl', models.CharField(blank=True, max_length=5, null=True)),
                ('inventory', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('inv_due_date', models.DateField(blank=True, default=datetime.date(2022, 6, 21), null=True)),
                ('count', models.PositiveIntegerField(blank=True, null=True)),
                ('box_name', models.CharField(blank=True, default='Mixed Items', max_length=25, null=True)),
                ('box_approve', models.BooleanField(blank=True, default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countrymgt.citymanagement')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countrymgt.countrymanager')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetrade.categoryproducts')),
                ('trader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='MixedBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale', models.CharField(blank=True, max_length=5, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('box', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetrade.productsbox')),
                ('items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetrade.categoryproducts')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]
