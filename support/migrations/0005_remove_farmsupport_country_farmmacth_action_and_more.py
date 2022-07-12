
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [

        ('vegefarm', '0016_alter_farmgrow_inv_due_date_and_more'),
        ('profils', '0009_supporterprofiles_experience_supporterprofiles_fees'),

        ('profils', '0009_supporterprofiles_experience_supporterprofiles_fees'),
        ('vegefarm', '0017_rename_inv_due_date_farmgrow_due_date_and_more'),

        ('support', '0004_farmsupport_supportcontact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmsupport',
            name='country',
        ),
        migrations.AddField(
            model_name='farmmacth',
            name='action',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'ACTIVE'), ('DEACTIVATE', 'DEACTIVATE')], default='ACTIVE', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='farmmacth',
            name='status',
            field=models.CharField(blank=True, choices=[('NEW', 'NEW'), ('APPROVED', 'APPROVED'), ('REJECT', 'REJECT')], default='NEW', max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='FarmAdvice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('advice', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('grow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vegefarm.farmgrow')),
                ('supporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.supporterprofiles')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profils.usersprofiles')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]
