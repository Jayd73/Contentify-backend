from django.contrib import admin
from user_post.models import UserPost
from channel.models import Channel

admin.site.register(UserPost)
admin.site.register(Channel)
