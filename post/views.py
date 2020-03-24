from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.files import File
from PIL import Image
from io import BytesIO
import os

# Create your views here.
from datetime import datetime, timedelta


def post_view(request):
#     date_from = datetime.datetime.now() - datetime.timedelta(days=1)
# created_documents = CreatedDocumentDetails.objects.filter(
#      user=user, created_document_timestamp__gte=date_from).count()

    context = {
        
    }
    return render(request, 'posts.html', context)

def add_post(request):
       
    if request.method == 'POST':
        form = PostForm(request.POST)
        form_img = PostImgForm(request.POST, request.FILES)
        if form_img.is_valid():
            # post = form.save(commit=False)
            # post.author = request.user
            # post.save()
            
            post_img = form_img.save(commit=False)
            image = form_img.cleaned_data.get('file')
            print(image)
            
            img = Image.open(image)
            rgb_im = img.convert('RGB')
            im_io = BytesIO() 
            rgb_im.save(im_io, 'JPEG', quality=85,)
            newimage = File(im_io, name=image.name)
            post_img.file = newimage
            post_img.save()
            return redirect('accounts:myprofile')
    else:
        form = PostForm()
        form_img = PostImgForm()


    context = {
        # 'form':form,
        'form_img':form_img,
        
    }
    return render(request, 'add_post.html', context)
    


'''
def delete_old_foos():
    # Query all the foos in our database
    foos = Foo.objects.all()

    # Iterate through them
    for foo in foos:

        # If the expiration date is bigger than now delete it
        if foo.expiration_date < timezone.now():
            foo.delete()
            # log deletion
    return "completed deleting foos at {}".format(timezone.now())
    
'''