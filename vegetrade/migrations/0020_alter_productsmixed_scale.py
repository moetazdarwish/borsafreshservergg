# Generated by Django 4.0 on 2022-06-28 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetrade', '0019_rename_discription_productsmixed_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmixed',
            name='scale',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]