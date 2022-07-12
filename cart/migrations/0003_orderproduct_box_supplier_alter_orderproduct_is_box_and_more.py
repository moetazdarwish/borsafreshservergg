# Generated by Django 4.0 on 2022-06-18 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vegetrade', '0002_remove_products_box_approve_remove_products_is_box_and_more'),
        ('cart', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='box_supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vegetrade.productsbox'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='is_box',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='scale',
            field=models.CharField(blank=True, default='Mix', max_length=5, null=True),
        ),
    ]