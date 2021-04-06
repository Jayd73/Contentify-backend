from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from channel.models import Channel
from multimedia.models import Video, Audio
from ..serializers import VideoSerializer, AudioSerializer


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class SingleUserVideoList(APIView):
    def get(self, request, pk ,format=None):
        user_channel = get_object_or_404(Channel, id = pk)
        serializer = VideoSerializer(user_channel.video_set.all(), many = True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class VideoDetails(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class AddNewVideo(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        # print("Requested data: ", request.data)
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            #change id to request.user.channel.id
            parent_channel = get_object_or_404(Channel, id = 8) #request.user.channel.id
            serializer.validated_data["channel"] = parent_channel
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDetailsFromSlug(generics.RetrieveAPIView):
    serializer_class = VideoSerializer
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Video, slug=item)

# class AddToLikedVideos(generics.UpdateAPIView):
#     serializer_class = VideoSerializer
#     def put(self, request, pk = None, format = None):
#         liked_video = get_object_or_404(Video, id=pk)
#         user_channel = Channel.objects.get(id = request.user.channel.id)
#         user_channel.liked_videos.add(liked_video)
#         liked_video.likes += 1
#         liked_video.save()
#         user_channel.save()
#         return Response(VideoSerializer(liked_video).data)

class EditVideoDetails(generics.UpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

class DeleteVideo(generics.RetrieveDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
      

#=====================================  AUDIO ==============================================

