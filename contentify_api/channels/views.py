from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


from channel.models import Channel
from django.contrib.auth.models import User
from .serializers import ChannelSerializer


class ChannelList(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class ChannelDetails(generics.RetrieveDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class ChannelDetailsFromCurrUser(APIView):
    def get(self, request, format = None):
        user_channel = None
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




    # def put(self, request, pk, format=None):
    #     print(request.data)
    #     obj = User.objects.get(pk=pk).channel
    #     serializer = ChannelSerializer(obj, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

