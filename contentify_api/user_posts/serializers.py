from rest_framework import serializers
from user_post.models import UserPost


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UserPost
