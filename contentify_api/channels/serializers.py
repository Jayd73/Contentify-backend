from rest_framework import serializers
from channel.models import Channel

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Channel
        depth = 1
