from django.urls import path
from video_processing import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload_video, name='upload_video'),
    path('videos/', views.video_list, name='video_list'),
    path('search/<int:video_id>/', views.search_subtitles, name='search_subtitles'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
