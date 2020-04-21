from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('activation_success/', views.activation_success, name='activation_success'),
    path('email_sent', views.confirmation_email, name='email_sent'),
    #password reset confirm 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    # Business info
    path('business_info/', views.businessinfo, name='business_info'),
    path('business_details/', views.businessdetails_view, name='business_details'),
    path('cover/', views.cover_img, name='cover'),
    path('<int:id>/cover/', views.cover_img_delete, name='cover_delete'),
    path('profile_img/', views.profile_img, name='profileimg'),
    path('<int:id>/profile_img_delete/', views.profile_img_delete, name='profile_img_delete'),
    path('gallery/', views.gallery, name='gallery'),
    path('<int:id>/gallery/', views.gallery_delete, name='gallery_delete'),
    path('myprofile/', views.myprofile_view, name='myprofile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
