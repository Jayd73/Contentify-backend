
from django.urls import path
from .views import UserPostList, UserPostDetail

app_name = 'contentify_api'

urlpatterns = [
    path('<int:pk>/', UserPostDetail.as_view(), name='detailcreate'),
    path('', UserPostList.as_view(), name='listcreate'),
]