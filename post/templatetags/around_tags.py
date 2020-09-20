from django import template
from django.template.defaultfilters import register
from post.models import *

# register = template.Library()

@register.filter(name='reminder')
def reminder(value):
    # return reminder value 
    return value % 4 

@register.inclusion_tag('posts.html')
def ads(value):    
    pass
    