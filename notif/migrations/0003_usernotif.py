# Generated by Django 4.0 on 2022-06-19 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0002_tradertransdata'),
        ('notif', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='New Order', max_length=50, null=True)),
                ('body', models.CharField(blank=True, default='New Order', max_length=50, null=True)),
                ('read', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
            ],
        ),
    ]
