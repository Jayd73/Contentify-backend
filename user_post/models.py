from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from channel.models import Channel

def upload_to(instance, filename):
    return 'channel/userpostsimg/{filename}'.format(filename = filename)

class UserPost(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(_("UserPostImage"), upload_to = upload_to, null = True)
    slug = models.SlugField(max_length=250, unique=True, default="channel_name")
    published = models.DateTimeField(default=timezone.now)
    channel = models.ForeignKey(Channel, on_delete = models.CASCADE, null = True)

    class Meta:
        ordering = ('-published',)

    # def __str__(self):
    #     return self.published

