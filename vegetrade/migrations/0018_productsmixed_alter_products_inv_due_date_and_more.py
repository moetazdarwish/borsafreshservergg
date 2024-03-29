# Generated by Django 4.0 on 2022-06-28 17:03

import datetime
from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0007_profilesmsg'),
        ('countrymgt', '0014_alter_countrymanager_file_upload'),
        ('vegetrade', '0017_alter_products_inv_due_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsMixed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('symbl', models.CharField(blank=True, max_length=5, null=True)),
                ('discription', models.CharField(blank=True, max_length=200, null=True)),
                ('inventory', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('inv_due_date', models.DateField(blank=True, default=datetime.date(2022, 7, 1), null=True)),
                ('scale', models.CharField(blank=True, choices=[('KG', 'KG'), ('BUNCH', 'BUNCH'), ('PIECE', 'PIECE')], max_length=5, null=True)),
                ('weight', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('status', models.CharField(blank=True, choices=[('NEW', 'NEW'), ('UPDATE', 'UPDATE')], max_length=20, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetrade.categoryproducts')),
                ('trader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
        migrations.AlterField(
            model_name='products',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 1), null=True),
        ),
        migrations.AlterField(
            model_name='productsbox',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 1), null=True),
        ),
        migrations.AlterField(
            model_name='productsbulk',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 1), null=True),
        ),
        migrations.AlterField(
            model_name='sellingboxproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 1), null=True),
        ),
        migrations.CreateModel(
            name='SellingMixedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('supplier_rev', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('our_profit', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetrade.categoryproducts')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vegetrade.productsmixed')),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='countrymgt.cityzone')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductMixedZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('supplier_rev', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('our_profit', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vegetrade.productsmixed')),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countrymgt.cityzone')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]
