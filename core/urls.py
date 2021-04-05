from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', include('contentify_api.users.urls', namespace='users')),
    path('admin/', admin.site.urls),
    #path('', include('user_posts.urls', namespace = 'user_posts')),
    path('api/channel/', include('contentify_api.channels.urls', namespace = 'channels')),
    path('api/userpost/', include('contentify_api.user_posts.urls', namespace = 'user_posts')),
    path('api/video/', include('contentify_api.multimedia.video.urls', namespace = 'videos')),
    path('api/audio/', include('contentify_api.multimedia.audio.urls', namespace = 'audios')),
    path('api/comment/', include('contentify_api.comment.urls', namespace = 'comments')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

