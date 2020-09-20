from django.urls import path, include
from administrator import views

app_name='administrator'

urlpatterns = [
   path('', views.administratorView, name='admin'),
   path('user-accounts/', views.userAccounts, name='user-accounts'),
   path('activity-logs/', views.activityLogs, name='logs' ),
   path('del-activity-logs/', views.delete_all_logs, name='del-logs' ),
   

]