from rest_framework import serializers
from multimedia.models import Video, Audio


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Video
        depth = 2

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Audio
        depth = 2
        
