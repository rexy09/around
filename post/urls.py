from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
    path('posts/', views.all_post, name='posts'),
    path('<int:id>/all_posts/', views.all_posts, name='all_posts'),
    path('posts_all/', views.posts_all, name='posts_all'),
    path('add_post/', views.add_post, name='add_post'),
    path('<int:id>/post_view/', views.post_view, name='post_view'),    
    path('<int:id>/view_post/', views.view_post, name='view_post'),
    path('<int:id>/post/', views.edit_post, name='edit_post'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:id>/img/<int:pid>/delete/', views.delete_post_img, name='delete_post_img'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
