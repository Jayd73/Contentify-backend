# Generated by Django 3.1.7 on 2021-04-05 18:25

from django.db import migrations, models
import multimedia.models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.FileField(null=True, upload_to=multimedia.models.upload_audio_to),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(null=True, upload_to=multimedia.models.upload_video_to),
        ),
    ]
