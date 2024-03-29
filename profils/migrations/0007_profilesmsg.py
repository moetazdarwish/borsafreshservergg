# Generated by Django 4.0 on 2022-06-26 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0006_alter_tradertransdata_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilesMSG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(blank=True, null=True)),
                ('smal_msg', models.TextField(blank=True, null=True)),
                ('is_read', models.BooleanField(default=True, null=True)),
                ('is_admin', models.BooleanField(default=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
            ],
        ),
    ]
