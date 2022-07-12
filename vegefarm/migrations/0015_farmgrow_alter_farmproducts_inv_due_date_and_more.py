# Generated by Django 4.0 on 2022-06-30 22:20

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import vegefarm.models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetrade', '0028_alter_products_inv_due_date_and_more'),
        ('profils', '0007_profilesmsg'),
        ('vegefarm', '0014_farmproductsbulk_hydro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmGrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('inv_due_date', models.DateField(blank=True, default=datetime.date(2022, 7, 31), null=True)),
                ('status', models.CharField(blank=True, default='NEW', max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetrade.categoryproducts')),
                ('trader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
        migrations.AlterField(
            model_name='farmproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 31), null=True),
        ),
        migrations.AlterField(
            model_name='farmproductsbulk',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 31), null=True),
        ),
        migrations.AlterField(
            model_name='farmsellingproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 31), null=True),
        ),
        migrations.AlterField(
            model_name='sellingfarmbulkproducts',
            name='inv_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 7, 31), null=True),
        ),
        migrations.CreateModel(
            name='FarmPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank=True, default='farm_default.jpg', null=True, upload_to=vegefarm.models.farm_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])])),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegefarm.farmgrow')),
            ],
        ),
    ]