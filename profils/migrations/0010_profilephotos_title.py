# Generated by Django 4.0 on 2022-07-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0009_supporterprofiles_experience_supporterprofiles_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilephotos',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]