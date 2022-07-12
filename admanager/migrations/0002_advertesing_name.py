

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertesing',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
