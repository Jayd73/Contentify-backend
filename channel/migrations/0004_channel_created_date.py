# Generated by Django 3.1.7 on 2021-03-30 06:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0003_auto_20210330_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
