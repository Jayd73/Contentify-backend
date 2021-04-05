from django.db import models
from django.utils import timezone
from channel.models import Channel
from user_post.models import UserPost
from multimedia.models import Video, Audio

class Comment(models.Model):
    text = models.TextField(blank=True)
    posted_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default = 0)
    channel = models.ForeignKey(Channel, on_delete = models.CASCADE, null = True)
    video_ref = models.ForeignKey(Video, on_delete = models.CASCADE, null = True)
    audio_ref = models.ForeignKey(Audio, on_delete = models.CASCADE, null = True)
    userPost_ref = models.ForeignKey(UserPost, on_delete = models.CASCADE, null = True)