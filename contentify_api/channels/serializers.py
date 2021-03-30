from rest_framework import serializers
from user_post.models import UserPost
from channel.models import Channel


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UserPost

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Channel