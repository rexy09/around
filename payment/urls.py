from django.urls import path
from payment import views

app_name = 'payment'

urlpatterns = [
    path('pay/<int:post>/<int:plan>/', views.payment_view, name='pay'),
    path('checkout/', views.checkout, name='checkout'),    
]
