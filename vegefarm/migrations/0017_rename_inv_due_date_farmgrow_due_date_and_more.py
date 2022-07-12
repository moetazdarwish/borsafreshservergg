# Generated by Django 4.0 on 2022-07-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegefarm', '0016_alter_farmgrow_inv_due_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmgrow',
            old_name='inv_due_date',
            new_name='due_date',
        ),
        migrations.AddField(
            model_name='farmgrow',
            name='system',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
