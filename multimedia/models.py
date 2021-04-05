from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from channel.models import Channel


def upload_video_thumbnail_to(instance, filename):
    return 'channel/videos/thumnbnails/{filename}'.format(filename = filename)

def upload_audio_cover_to(instance, filename):
    return 'channel/audios/covers/{filename}'.format(filename = filename)

def upload_video_to(instance, filename):
    return 'channel/videos/video_files/{filename}'.format(filename = filename)

def upload_audio_to(instance, filename):
    return 'channel/audios/audio_files/{filename}'.format(filename = filename)

class Multimedia(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    upload_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(max_length=250, unique=True, null = True)
    channel = models.ForeignKey(Channel, on_delete = models.CASCADE, null = True)

    class Meta:
        abstract = True
        ordering = ('-upload_date',)

    
class Video(Multimedia):
    thumbnail = models.ImageField(_("Thumbnail"), upload_to = upload_video_thumbnail_to, null = True)
    file = models.FileField(upload_to = upload_video_to, null = True)

    def __str__(self):
        return self.title

    
class Audio(Multimedia):
    cover = models.ImageField(_("AudioCover"), upload_to = upload_audio_cover_to, null = True)
    file = models.FileField(upload_to = upload_audio_to, null = True)

    def __str__(self):
        return self.title
