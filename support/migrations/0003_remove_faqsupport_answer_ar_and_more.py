# Generated by Django 4.0 on 2022-06-30 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_faqsupport_answer_sc_faqsupport_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqsupport',
            name='answer_ar',
        ),
        migrations.RemoveField(
            model_name='faqsupport',
            name='answer_en',
        ),
        migrations.RemoveField(
            model_name='faqsupport',
            name='subject_ar',
        ),
        migrations.RemoveField(
            model_name='faqsupport',
            name='subject_en',
        ),
    ]