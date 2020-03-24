from django import forms
from .models import *
from PIL import Image




class PostForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'title'}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Describe your product here', 'rows':'4'}))
    
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'price'
        ]


class PostImgForm(forms.ModelForm):
    file = forms.FileField( widget=forms.FileInput(attrs={'multiple':'', }))
    class Meta:
        model = PostImage
        fields = ['file', ]