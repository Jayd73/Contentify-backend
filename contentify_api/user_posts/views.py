from rest_framework import generics
from user_post.models import UserPost
from .serializers import UserPostSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from channel.models import Channel
from .serializers import UserPostSerializer
from django.shortcuts import get_object_or_404

import random, string


class UserPostList(generics.ListCreateAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer

class SingleUserPostList(APIView):
    def get(self, request, pk ,format=None):
        user_channel = get_object_or_404(Channel, id = pk)
        serializer = UserPostSerializer(user_channel.userpost_set.all(), many = True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserPostDetail(generics.RetrieveAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer

class CreateUserPost(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        # print("Requested data: ", request.data)
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            #change id to request.user.channel.id
            parent_channel = get_object_or_404(Channel, id=request.user.channel.id)
            serializer.validated_data["channel"] = parent_channel
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserPost(generics.RetrieveDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.all()
    

