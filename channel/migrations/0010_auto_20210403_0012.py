# Generated by Django 3.1.7 on 2021-04-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0009_auto_20210402_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='followedChannels',
            field=models.ManyToManyField(blank=True, to='channel.Channel'),
        ),
    ]
