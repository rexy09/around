from django.contrib.gis.db import models
from django.conf import settings 

# Create your models here.



from django.utils import timezone
import math

# {{ post.timestamp | timesince }}

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author', on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add= True)
    date_updated = models.DateTimeField(auto_now= True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)



    def __str__(self):
        return self.title


    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.date_created

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


# <h1>Published {{ postobj.whenpublished }}</h1>

class PostImage(models.Model):
    # post = models.ForeignKey(Post, related_name='post_img', on_delete=models.CASCADE)
    file = models.ImageField(upload_to='post_img/')
    # position = models.PositiveSmallIntegerField(default=0)
    date_updated= models.DateTimeField(auto_now= True)



