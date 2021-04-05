
from django.urls import path
from .views import UserPostList, UserPostDetail, CreateUserPost, DeleteUserPost, SingleUserPostList

app_name = 'contentify_api'

urlpatterns = [
    path('<int:pk>/', UserPostDetail.as_view(), name='detailcreate'),
    path('create/', CreateUserPost.as_view(), name='createuserpost'),
    path('', UserPostList.as_view(), name='listcreate'),
    path('delete/<int:pk>/', DeleteUserPost.as_view(), name='deleteuserpost'),
    path('channel/<int:pk>/', SingleUserPostList.as_view(), name='singleuserpostlist'),
]