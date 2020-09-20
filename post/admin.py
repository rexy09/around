from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "author", "title", "price"]    
    list_display_links = ["pk","title"]
    
    
@admin.register(PostImage)
class PostImageModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "post", "file"]    
    list_display_links = ["pk","post"]


@admin.register(SponsoredPost)
class SponsoredPostModelAdmin(admin.ModelAdmin):
    list_display = ["pk","post", "sponsored", "plan"]
    list_display_links = ["pk","post"]