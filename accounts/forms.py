from django import forms
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import BusinessInfo, BusinessDetails, CoverImg, ProfileImg, Gallery
from django.core.files import File
from PIL import Image



User = get_user_model()

# User ragistration form
class SignUpForm(UserCreationForm):
    CHOICES = (
        ('', 'Account Type'),
        # (1, 'Normal'),
        (2, 'Business'),
    ) 
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'rounded-pill', 'placeholder':'Username'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'rounded-pill', 'placeholder':'Email'}))
    user_type = forms.ChoiceField(choices=CHOICES, label='', widget=forms.Select(attrs={'class':'rounded-pill', 'placeholder':'Account Type'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'rounded-pill', 'placeholder':'Password',}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'rounded-pill', 'placeholder':'Confirm password',}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
			'username',
			'email',
            'user_type',
			'password1',
			'password2',
		]


# User login form
class LoginForm(forms.Form):

	username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'rounded-pill', 'placeholder':'Username or email'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'rounded-pill', 'placeholder':'Password'}))
 
#  Business info form
class BusinessInfoForm(forms.ModelForm):
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
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'First name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Last name'}))
    gender = forms.ChoiceField(choices=GENDER_CHOISES,label='', widget=forms.RadioSelect(attrs={}))
    birthdate = forms.CharField(label='', widget=forms.DateInput(attrs={'type':'date'}))
    business_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Business name'}))
    business_type = forms.ChoiceField(choices=BUSINESS_CHOICES, label='', widget=forms.Select(attrs={'placeholder':'Business type'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'placeholder':'City'}))
    street = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Street eg. Sinza, Madukani'}))
    
    class Meta:
        model = BusinessInfo
        fields = [
            'first_name',
            'last_name',
            'gender',
            'birthdate',
            'business_name',
            'business_type',
            'country',
            'city',
            'street',
        ]
        
        widgets = {
		'country': CountrySelectWidget(attrs={}), 
		}


class BusinessDetailsForm(forms.ModelForm):
    # BCATEGORY_CHOICES = [
    #     ('','Select business category'),
    #     ('money agent','Money Agent'),
    #     ('fashion','Fashion'),
    #     ('restaurant','Restaurant'),
    #     ('mobile','Mobile & Accessories'),        
    # ]
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Describe your business here','rows':'4'}))
    # business_category = forms.ChoiceField(choices=BCATEGORY_CHOICES, label='', widget=forms.Select(attrs={'placeholder':'Choose your business cartegory'}))
    longitude = forms.DecimalField(label='longitude', widget=forms.TextInput(attrs={'placeholder':'Pin your location','id':'info1','type':'hidden'}))
    latitude = forms.DecimalField(label='latitude', widget=forms.TextInput(attrs={'placeholder':'Pin your location','id':'info2','type':'hidden'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter phone number'}))
    
    class Meta:
        model = BusinessDetails
        fields = [
            'description',
            # 'business_category',
            'longitude',
            'latitude',
            'email',
            'phone',
            
        ]
        
        
class CoverImgForm(forms.ModelForm):
    image = forms.ImageField(label='Add Image', widget=forms.FileInput(attrs={}))
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())
    
    class Meta:
        model = CoverImg
        fields = ['image', 'x', 'y', 'width', 'height', ]
    
class ProfileImgForm(forms.ModelForm):
    image = forms.ImageField(label='Add Image', widget=forms.FileInput(attrs={}))
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = ProfileImg
        fields = ['image', 'x', 'y', 'width', 'height', ]
   
    

class GalleryImgForm(forms.ModelForm):
    image = forms.FileField(label='Add Images', widget=forms.ClearableFileInput(attrs={'multiple': True,}))
    class Meta:
        model = Gallery
        fields = ['image', ]