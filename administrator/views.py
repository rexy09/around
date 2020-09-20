from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators  import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from activity_log.models import ActivityLog
import datetime



# Create your views here.
# @login_required
# @user_passes_test(lambda u: u.is_superuser)
@staff_member_required 
def administratorView(request):
    context={}
    return render(request, 'admin/administrator.html', context)

@staff_member_required 
def userAccounts(request):
    User = get_user_model()
    users = User.objects.all()
    
    context = {
        'users':users,
    }
    return render(request, 'admin/user-accounts.html', context)

@staff_member_required 
def activityLogs(request):
    logs = ActivityLog.objects.all().order_by('-datetime')[:10]
    context = {
        'logs':logs,        
    }
    return render(request, 'admin/activity-logs.html', context)

@staff_member_required 
def delete_all_logs(request):
    # strftime("%b %d %Y %H:%M:%S")
    logs = ActivityLog.objects.exclude(datetime__icontains=datetime.date.today().strftime("%m"))
    # print(datetime.date.today().strftime("%m"))    
    for log in logs:
        log.delete()
        
    return redirect('administrator:logs')