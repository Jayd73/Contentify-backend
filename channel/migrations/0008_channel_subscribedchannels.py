# Generated by Django 3.1.7 on 2021-04-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0007_channel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='subscribedChannels',
            field=models.ManyToManyField(blank=True, null=True, to='channel.Channel'),
        ),
    ]
