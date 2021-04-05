from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from channel.models import Channel
from user_post.models import UserPost
from multimedia.models import Video, Audio
from comment.models import Comment
from .serializers import CommentSerializer

class CommentListForVideo(APIView):
    def get(self, request, pk ,format=None):
        video = get_object_or_404(Video, id = pk)
        serializer = CommentSerializer(video.comment_set.all(), many = True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class CommentListForAudio(APIView):
    def get(self, request, pk ,format=None):
        audio = get_object_or_404(Audio, id = pk)
        serializer = CommentSerializer(audio.comment_set.all(), many = True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class CommentListForPosts(APIView):
    def get(self, request, pk ,format=None):
        userPost = get_object_or_404(UserPost, id = pk)
        serializer = CommentSerializer(userPost.comment_set.all(), many = True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateCommentForVideo(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk, format=None):
        # print("Requested data: ", request.data)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            #change id to request.user.channel.id
            parent_channel = get_object_or_404(Channel, id = request.user.channel.id) #request.user.channel.id
            target =  get_object_or_404(Video, id = pk)
            serializer.validated_data["channel"] = parent_channel
            serializer.validated_data["video_ref"] = target
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCommentForAudio(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk, format=None):
        # print("Requested data: ", request.data)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            #change id to request.user.channel.id
            parent_channel = get_object_or_404(Channel, id = request.user.channel.id) #request.user.channel.id
            target =  get_object_or_404(Audio, id = pk)
            serializer.validated_data["channel"] = parent_channel
            serializer.validated_data["audio_ref"] = target
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCommentForPost(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk, format=None):
        # print("Requested data: ", request.data)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            #change id to request.user.channel.id
            parent_channel = get_object_or_404(Channel, id = request.user.channel.id) #request.user.channel.id
            target =  get_object_or_404(UserPost, id = pk)
            serializer.validated_data["channel"] = parent_channel
            serializer.validated_data["userPost_ref"] = target
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddLike(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    def put(self, request, pk = None, format = None):
        comment = Comment.objects.get(id = pk)
        comment.likes += 1
        comment.save()
        return Response(CommentSerializer(comment).data)

class RemoveLike(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    def put(self, request, pk = None, format = None):
        comment = Comment.objects.get(id = pk)
        comment.likes -= 1
        comment.save()
        return Response(CommentSerializer(comment).data)

class DeleteComment(generics.RetrieveDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
      

#=====================================  AUDIO ==============================================

