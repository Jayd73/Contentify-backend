from django.contrib import admin
from user_post.models import UserPost
from channel.models import Channel
from multimedia.models import Video, Audio
from comment.models import Comment

admin.site.register(UserPost)
admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Comment)




