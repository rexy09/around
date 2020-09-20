from django.urls import path, include
from pages import views

app_name='pages'

urlpatterns = [
    path('<int:id>/profile/', views.profile_view, name='profile'),
    path('<int:user_id>/gallery/', views.gallery, name='gallery'),
    path('search/', views.search_view, name='search'),
    path('search/<str:query>/', views.search_category, name='search_cat'),
    path('orders/', views.orders_view, name='orders'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('getcoords/', views.get_coordinates, name='getcoords'),
    path('success/', views.successView, name='success'),
    path('help/', views.helpView, name='help'),
    path('terms&privacy/', views.termsView, name='terms'),


]