# Generated by Django 4.0 on 2022-06-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqsupport',
            name='answer_sc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faqsupport',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='faqsupport',
            name='subject_sc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]