from django.contrib.auth.models import AbstractUser
from django.conf import settings  # settings.AUTH_USER_MODEL
from django_countries.fields import CountryField
# from django.contrib.gis.db.models import PointField
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import GEOSGeometry

from activity_log.models import UserMixin

# Only for LAST_ACTIVITY = True
# class User(AbstractUser, UserMixin):
#     pass


# Create your models here.

class User(AbstractUser, UserMixin):
    USER_TYPE_CHOICES = (
        (0,'Null'),
        (1,'Normal'),
        (2,'Business'),
    )
    email = models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, unique=True, blank=False, null=False)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=0)
    
    

class BusinessInfo(models.Model):
    GENDER_CHOISES = [
        ('male','Male'),
        ('female','Female'),
    ]
    BUSINESS_CHOICES = [
        ('', 'Business type'),
        ('fashion', 'Fashion'),
        ('mobile & accessories','Mobile & Accessories'),
        ('restaurant', 'Restaurant'),
        ('money agent', 'Money Agent'),
        ('other', 'Other'),    
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='user_info',  on_delete = models.CASCADE, primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOISES)
    birthdate = models.DateField()
    business_name = models.CharField(max_length=50)
    business_type = models.CharField(max_length=50,choices=BUSINESS_CHOICES)    
    country = CountryField(blank_label='Select country')
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
 
 
class BusinessDetails(models.Model):
    # BUSINESS_CHOICES = [
    #     ('', 'Business type'),
    #     ('fashion', 'Fashion'),
    #     ('mobile & accessories','Mobile & Accessories'),
    #     ('restaurant', 'Restaurant'),
    #     ('money agent', 'Money Agent'),
    #     ('other', 'Other'),    
    # ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, primary_key=True, unique=True)
    description = models.TextField(null=True, blank=True)
    # business_category = models.CharField(max_length=100, null=True, blank=True, choices=BUSINESS_CHOICES)
    longitude = models.DecimalField(max_digits=19, decimal_places=16, null=True, blank=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=16, null=True, blank=True)
    location = models.PointField(srid=4326, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class CoverImg(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, primary_key=True, unique=True)
    image = models.ImageField(upload_to='cover_image/')
    uploaded_at = models.DateTimeField(auto_now=True)
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name = 'coverimg'
        verbose_name_plural = 'coverimgs'


class ProfileImg(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, primary_key=True, unique=True)
    image = models.ImageField(upload_to='profile_image/')
    uploaded_at = models.DateTimeField(auto_now=True)
    
   
class Gallery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='gallery_image/')
    date_updated = models.DateTimeField(auto_now=True)
    
"""  
class Follow(models.Model):
    follower_id = models.IntegerField()
    followed_id = models.IntegerField()
    date_updated = models.DateTimeField(auto_now=True) 
"""