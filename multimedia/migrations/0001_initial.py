# Generated by Django 3.1.7 on 2021-04-05 17:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multimedia.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channel', '0010_auto_20210403_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='')),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
                ('thumbnail', models.ImageField(null=True, upload_to=multimedia.models.upload_video_thumbnail_to, verbose_name='Thumbnail')),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='channel.channel')),
            ],
            options={
                'ordering': ('-upload_date',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='')),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
                ('cover', models.ImageField(null=True, upload_to=multimedia.models.upload_audio_cover_to, verbose_name='AudioCover')),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='channel.channel')),
            ],
            options={
                'ordering': ('-upload_date',),
                'abstract': False,
            },
        ),
    ]
