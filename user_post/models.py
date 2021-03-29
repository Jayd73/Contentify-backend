from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserPost(models.Model):
    content = models.TextField()
    #slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_posts')

    class Meta:
        ordering = ('-published',)

    # def __str__(self):
    #     return self.published

