from django.urls import path, include
from pages import views

app_name='pages'

urlpatterns = [
    path('<int:id>/profile/', views.profile_view, name='profile'),
    path('<int:id>/<int:user_id>/product_view/', views.product_view, name='product_view'),
    path('<int:user_id>/products_all/', views.products_all, name='products_all'),
    path('<int:user_id>/gallery/', views.gallery, name='gallery'),
    path('search/', views.search_view, name='search'),
    path('search/<str:query>/', views.search_category, name='search_cat'),
    path('orders/', views.orders_view, name='orders'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('getcoords/', views.get_coordinates, name='getcoords'),

]