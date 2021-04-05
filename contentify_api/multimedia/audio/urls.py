
from django.urls import path
from .views import *

app_name = 'contentify_api'

urlpatterns = [
    path('', AudioList.as_view(), name='audiolistcreate'),
    path('<int:pk>/', AudioDetails.as_view(), name='audiodetailcreate'),
    path('create/', AddNewAudio.as_view(), name='addnewaudio'),
    path('delete/<int:pk>/', DeleteAudio.as_view(), name='deleteaudio'),
    path('edit/<int:pk>/', EditAudioDetails.as_view(), name='editvidepo'),
    # path('addlike/<int:pk>/', AddToLikedAudios.as_view(), name='addlikeaudio'),
    path('channel/<int:pk>/', SingleUserAudioList.as_view(), name='singleuseraudiolist'),
    path('<str:pk>/', AudioDetailsFromSlug.as_view(), name='detailcreateslugaudio'),
]