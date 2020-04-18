from django.contrib import admin
from .models import User, BusinessInfo, BusinessDetails, CoverImg, ProfileImg, Gallery

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('username','email','user_type','is_staff','is_active')


admin.site.register(User, UserAdmin)
# business info
admin.site.register(BusinessInfo)
admin.site.register(BusinessDetails)
admin.site.register(CoverImg)
admin.site.register(ProfileImg)
admin.site.register(Gallery)