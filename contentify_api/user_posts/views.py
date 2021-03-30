from rest_framework import generics
from user_post.models import UserPost
from .serializers import UserPostSerializer


class UserPostList(generics.ListCreateAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer


class UserPostDetail(generics.RetrieveDestroyAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer

