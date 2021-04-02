from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from channel.models import Channel
from .serializers import ChannelSerializer


class ChannelList(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class ChannelDetails(generics.RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class ChannelDetailsFromSlug(generics.RetrieveAPIView):
    serializer_class = ChannelSerializer
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Channel, slug=item)

class ChannelDetailsFromCurrUser(APIView):
    def get(self, request, format = None):
        serializer = ChannelSerializer(request.user.channel)   
        return Response(serializer.data)

class UserAvatarUpload(generics.UpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()

class ChannelBannerUpload(generics.UpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()

class ChannelAboutChange(generics.UpdateAPIView):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()

class AddChannelFollower(generics.UpdateAPIView):
    serializer_class = ChannelSerializer
    def put(self, request, pk = None, format = None):
        target_channel = get_object_or_404(Channel, id=pk)
        target_channel.followers += 1
        target_channel.save()
        request.user.channel.followedChannels.add(target_channel)
        return Response(ChannelSerializer(request.user.channel).data)

class RemoveAsChannelFollower(generics.UpdateAPIView):
    serializer_class = ChannelSerializer
    def put(self, request, pk = None, format = None):
        target_channel = get_object_or_404(Channel, id=pk)
        target_channel.followers -= 1
        target_channel.save()
        request.user.channel.followedChannels.remove(target_channel)
        return Response(ChannelSerializer(request.user.channel).data)

      


