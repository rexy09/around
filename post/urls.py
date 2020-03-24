from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
    path('posts/', views.post_view, name='posts'),
    path('add_post/', views.add_post, name='add_post'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
