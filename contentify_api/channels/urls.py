
from django.urls import path
from .views import (ChannelList, ChannelDetails, ChannelDetailsFromSlug, UserAvatarUpload, 
ChannelBannerUpload, ChannelDetailsFromCurrUser, ChannelAboutChange, AddChannelFollower, RemoveAsChannelFollower)

app_name = 'contentify_api'

urlpatterns = [
    path('', ChannelList.as_view(), name='listcreate'),
    path('<int:pk>/', ChannelDetails.as_view(), name='detailcreate'),
    path('upload/avatar/<int:pk>/', UserAvatarUpload.as_view(), name='uploadavatar'),
    path('upload/banner/<int:pk>/', ChannelBannerUpload.as_view(), name='uploadbanner'),
    path('changeabout/<int:pk>/', ChannelAboutChange.as_view(), name='aboutchange'),
    path('addfollower/<int:pk>/', AddChannelFollower.as_view(), name='addfollower'),
    path('removefollower/<int:pk>/', RemoveAsChannelFollower.as_view(), name='removefollower'),
    path('curruser/', ChannelDetailsFromCurrUser.as_view(), name='getcurruserchannel'),
    path('<str:pk>/', ChannelDetailsFromSlug.as_view(), name='detailcreateslug'),
]