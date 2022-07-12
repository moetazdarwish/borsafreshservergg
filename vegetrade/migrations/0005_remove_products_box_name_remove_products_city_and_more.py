# Generated by Django 4.0 on 2022-06-21 17:46

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countrymgt', '0007_cityzone_country_cityzone_customer_percent_and_more'),
        ('vegetrade', '0004_alter_products_inv_due_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='box_name',
        ),
        migrations.RemoveField(
            model_name='products',
            name='city',
        ),
        migrations.RemoveField(
            model_name='products',
            name='country',
        ),
        migrations.RemoveField(
            model_name='sellingproducts',
            name='box_name',
        ),
        migrations.RemoveField(
            model_name='sellingproducts',
            name='city',
        ),
        migrations.RemoveField(
            model_name='sellingproducts',
            name='country',
        ),
        migrations.RemoveField(
            model_name='sellingproducts',
            name='hydro',
        ),
        migrations.RemoveField(
            model_name='sellingproducts',
            name='inv_due_date',
        ),
        migrations.RemoveField(
            model_name='sellingproducts',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='sellingproducts',
            name='is_box',
        ),
        migrations.RemoveField(
            model_name='sellingproducts',
            name='price',
        ),
        migrations.RemoveField(
            model_name='sellingproducts',
            name='scale',
        ),
        migrations.RemoveField(
            model_name='sellingproducts',
            name='symbl',
        ),
        migrations.AddField(
            model_name='sellingproducts',
            name='zone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='countrymgt.cityzone'),
        ),
        migrations.AlterField(
            model_name='products',
            name='scale',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.CreateModel(
            name='ProductZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('supplier_rev', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('our_profit', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vegetrade.products')),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countrymgt.cityzone')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]