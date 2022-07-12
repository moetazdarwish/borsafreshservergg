
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0009_supporterprofiles_experience_supporterprofiles_fees'),
        ('notif', '0004_alter_suppliernotif_body_alter_suppliernotif_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmTradeNotif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('body', models.CharField(blank=True, max_length=50, null=True)),
                ('read', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('trader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
            ],
        ),
    ]
