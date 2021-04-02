from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


def upload_to(instance, filename):
    return 'channel/avatar/{filename}'.format(filename = filename)

def upload_to_b(instance, filename):
    return 'channel/banner/{filename}'.format(filename = filename)

class Channel(models.Model):
    about = models.TextField(default="No description")
    followers = models.IntegerField(default = 0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    banner = models.ImageField(_("BannerImage"), upload_to = upload_to_b, default='channel/banner/defaultBanner.jpg')
    avatar = models.ImageField(_("Avatar"), upload_to = upload_to, default='channel/avatar/defaultAvatar.jpg')
    created_date = models.DateTimeField(default=now, editable=False)
    slug = models.SlugField(default = "channel_name",max_length = 250, null = False, blank = False)
    followedChannels = models.ManyToManyField("self", symmetrical=False, blank= True)

    def __str__(self):
        return self.user.username

