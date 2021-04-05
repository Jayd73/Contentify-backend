
from django.urls import path
from .views import *

app_name = 'contentify_api'

urlpatterns = [
    path('', VideoList.as_view(), name='videolistcreate'),
    path('<int:pk>/', VideoDetails.as_view(), name='videodetailcreate'),
    path('create/', AddNewVideo.as_view(), name='addnewvideo'),
    path('delete/<int:pk>/', DeleteVideo.as_view(), name='deletevideo'),
    path('edit/<int:pk>/', EditVideoDetails.as_view(), name='editvidepo'),
    # path('addlike/<int:pk>/', AddToLikedVideos.as_view(), name='addlikevideo'),
    path('channel/<int:pk>/', SingleUserVideoList.as_view(), name='singleuservideolist'),
    path('<str:pk>/', VideoDetailsFromSlug.as_view(), name='detailcreateslugvideo'),
]