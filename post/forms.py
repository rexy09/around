from django import forms
from .models import *
from PIL import Image




class PostForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder':'Title'}))
    content = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder':'Describe your post here.', 'rows':'4'}))
    price = forms.FloatField(label='Price in TSh', widget=forms.NumberInput(attrs={}))
    
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'phone',
            'price',
            'image',
        ]


class PostImgForm(forms.ModelForm):
    file = forms.FileField(label='Add Images', widget=forms.ClearableFileInput(attrs={'multiple': True,}))
    class Meta:
        model = PostImage
        fields = ['file', ]


class SponsoredPostForm(forms.ModelForm):
    PLANS = [
        ('','Select plan'),
        (7,'7 Days'),
        (30,'30 Days'),
        (60,'3 Months' ),
        (120,'6 Months'),
        (366,'1 Year'),
    ]
    plan = forms.IntegerField(label='', required=True, widget=forms.Select(choices=PLANS))
    class Meta:
        model = SponsoredPost
        fields = '__all__'
        exclude = ['post','sponsored']        