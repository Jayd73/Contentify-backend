from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from channel.models import Channel
from multimedia.models import Audio
from ..serializers import AudioSerializer

class AudioList(generics.ListCreateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

class SingleUserAudioList(APIView):
    def get(self, request, pk ,format=None):
        user_channel = get_object_or_404(Channel, id = pk)
        serializer = AudioSerializer(user_channel.audio_set.all(), many = True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class AudioDetails(generics.RetrieveAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

class AddNewAudio(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        # print("Requested data: ", request.data)
        serializer = AudioSerializer(data=request.data)
        if serializer.is_valid():
            #change id to request.user.channel.id
            parent_channel = get_object_or_404(Channel, id = request.user.channel.id) #request.user.channel.id
            serializer.validated_data["channel"] = parent_channel
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AudioDetailsFromSlug(generics.RetrieveAPIView):
    serializer_class = AudioSerializer
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Audio, slug=item)

# class AddToLikedAudio(generics.UpdateAPIView):
#     serializer_class = AudioSerializer
#     def put(self, request, pk = None, format = None):
#         liked_audio = get_object_or_404(Audio, id=pk)
#         user_channel = Channel.objects.get(id = request.user.channel.id)
#         user_channel.liked_videos.add(liked_audio)
#         liked_audio.likes += 1
#         liked_audio.save()
#         user_channel.save()
#         return Response(AudioSerializer(liked_audio).data)

class EditAudioDetails(generics.UpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = AudioSerializer
    queryset = Audio.objects.all()

class DeleteAudio(generics.RetrieveDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = AudioSerializer
    queryset = Audio.objects.all()
      


