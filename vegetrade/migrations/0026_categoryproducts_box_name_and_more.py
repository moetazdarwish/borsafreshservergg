# Generated by Django 4.0 on 2022-06-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetrade', '0025_categoryproducts_name_sc'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryproducts',
            name='box_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='box_name_sc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='retail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='retail_sc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='scale',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='scale_sc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_accept',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_accept_sc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_cancelled',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_cancelled_sc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_confirmed',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_confirmed_sc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_delivered',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_delivered_sc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_delivery',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_delivery_sc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_refused',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_refused_sc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_reschedule',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='st_reschedule_sc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
