
from django.urls import path
from .views import ChannelList, ChannelDetails, UserAvatarUpload, ChannelBannerUpload, ChannelDetailsFromCurrUser

app_name = 'contentify_api'

urlpatterns = [
    path('<int:pk>/', ChannelDetails.as_view(), name='detailcreate'),
    path('', ChannelList.as_view(), name='listcreate'),
    path('upload/avatar/<int:pk>', UserAvatarUpload.as_view(), name='uploadavatar'),
    path('upload/banner/<int:pk>', ChannelBannerUpload.as_view(), name='uploadbanner'),
    path('curruser/', ChannelDetailsFromCurrUser.as_view(), name='getcurruserchannel')
]