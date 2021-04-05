
from django.urls import path
from .views import *

app_name = 'contentify_api'

urlpatterns = [
    path('create/video/<int:pk>/', CreateCommentForVideo.as_view(), name='cmntforvideo'),
    path('create/audio/<int:pk>/', CreateCommentForAudio.as_view(), name='cmntforaudio'),
    path('create/userpost/<int:pk>/', CreateCommentForPost.as_view(), name='cmntforuserpost'),

    path('video/<int:pk>/', CommentListForVideo.as_view(), name='cmntlistforvideo'),
    path('audio/<int:pk>/', CommentListForAudio.as_view(), name='cmntlistforaudio'),
    path('userpost/<int:pk>/', CommentListForPosts.as_view(), name='cmntlistforuserpost'),

    path('like/<int:pk>/', AddLike.as_view(), name='cmntaddlike'),
    path('removelike/<int:pk>/', RemoveLike.as_view(), name='cmntremovelike'),

    path('delete/<int:pk>/', DeleteComment.as_view(), name='deletecmnt'),
]