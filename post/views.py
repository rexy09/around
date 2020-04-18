from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from accounts.models import *
from django.core.files import File
from PIL import Image
from io import BytesIO
import os
from django.db.models import Q

# Create your views here.
from datetime import datetime, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_post(request):
    
    if request.method =='POST':
        query = request.POST.get('query')
        query_set = Q(title__icontains=query)|Q(price__icontains=query)|Q(content__icontains=query)
        post_list = Post.objects.filter(query_set).all().order_by('-date_updated')
        
        page = request.GET.get('page', 1)

        paginator = Paginator(post_list, 10)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)        
        
    else:        
        post_list = Post.objects.all().order_by('-date_updated')

        page = request.GET.get('page', 1)

        paginator = Paginator(post_list, 10)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

    context = {
        'posts':posts,
        
    }
    return render(request, 'posts.html', context)


def all_posts(request, *args, **kwargs):
    id = kwargs.get('id')
    post_list = Post.objects.filter(author_id=id).all().order_by('-date_updated')
    
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts':posts,
        
    }
    return render(request, 'all_posts.html', context)


@login_required
def posts_all(request, *args, **kwargs):
    user = request.user
    post_list = Post.objects.filter(author_id=user.id).all().order_by('-date_updated')
    
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    context = {
        'posts':posts,
        
    }
    return render(request, 'posts_all.html', context)

@login_required
def add_post(request, *args, **kwargs):
    user = request.user
    obj = BusinessDetails.objects.filter(user_id=user.id).first()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        form_img = PostImgForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        
        if form_img.is_valid() and form.is_valid():            
            post = form.save(commit=False)
            post.author = user
            post.phone = obj.phone
            post.image = form_img.cleaned_data.get('file')
            post.save()
            
            for file in files:
                img = Image.open(file)
                rgb_im = img.convert('RGB')
                im_io = BytesIO() 
                rgb_im.save(im_io, 'JPEG', quality=85,)
                newimage = File(im_io, name=file.name)
                post_img = PostImage(post=post, file=newimage)
                post_img.save()
              
            return redirect('post:posts')
    else:
        form = PostForm()
        form_img = PostImgForm()


    context = {
        'form':form,
        'form_img':form_img,
        
    }
    return render(request, 'add_post.html', context)


def view_post(request, *args, **kargs):
    id = kargs.get('id')
    posts = Post.objects.filter(id=id)
    photos = PostImage.objects.filter(post_id=id).all().order_by('-date_updated')
    for post in posts:
        logoimg = ProfileImg.objects.filter(user_id=post.author_id)
        info = BusinessInfo.objects.filter(user_id=post.author_id)
    
    context= {
        'posts':posts,
        'photos':photos,
        'logoimg':logoimg,
        'info':info,
           
    }
    return render(request, 'view_post.html', context)

@login_required
def post_view(request, *args, **kargs):
    id = kargs.get('id')
    user = request.user    
    posts = Post.objects.filter(id=id, author_id=user.id)
    photos = PostImage.objects.filter(post_id=id).all().order_by('-date_updated')
    logoimg = ProfileImg.objects.filter(user_id=user.id)
    info = BusinessInfo.objects.filter(user_id=user.id)
    
    context= {
        'posts':posts,
        'photos':photos,
        'logoimg':logoimg,
        'info':info,
           
    }
    return render(request, 'post_view.html', context)

@login_required
def edit_post(request, *args, **kwargs):
    id = kwargs.get('id')
    user = request.user
    posts = Post.objects.filter(id=id, author_id=user.id).first()
    photos = PostImage.objects.filter(post_id=id).all().order_by('-date_updated')
    # getting image name
    img_url = False
    img_url = posts.image
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=posts)
        files = request.FILES.getlist('file')
        print(files)
        if form.is_valid():            
            post = form.save(commit=False)
            post.save()
                        
            for file in files:
                img = Image.open(file)
                rgb_im = img.convert('RGB')
                im_io = BytesIO() 
                rgb_im.save(im_io, 'JPEG', quality=85,)
                newimage = File(im_io, name=file.name)
                post_img = PostImage(post=posts, file=newimage)
                post_img.save()
              
            return redirect('post:posts')
            
    else:
        form = PostForm(instance=posts)
    
    context= {
        'form':form,
        'photos':photos,
    }
    return render(request, 'edit_post.html', context)

@login_required
def delete_post(request, *args, **kwargs):    
    id = kwargs.get('id')
    user = request.user
    posts = Post.objects.filter(id=id, author_id = user.id)
    photos = PostImage.objects.filter(post_id=id).all().order_by('-date_updated')
    logoimg = ProfileImg.objects.filter(user_id=user.id)
    info = BusinessInfo.objects.filter(user_id=user.id)
        
    if request.method == 'POST':
        for photo in photos:
            photo.file.delete()
            photo.delete()
        
        for post in posts:
            post.image.delete()
            post.delete()
        
        return redirect('post:posts_all')           
            
    
    context= {
        'posts':posts,
        'photos':photos,
        'logoimg':logoimg,
        'info':info,
           
    }
    return render(request, 'delete_post.html', context)

@login_required
def delete_post_img(request, *args, **kwargs):    
    id = kwargs.get('id')
    pid = kwargs.get('pid')
    user = request.user
    posts = Post.objects.filter(id=pid, author_id=user.id).first()    
    photos = PostImage.objects.filter(id=id, post_id=posts.id).all().order_by('-date_updated')
        
    if request.method == 'POST':
        for photo in photos:
            photo.file.delete()
            photo.delete()
        
        return redirect('post:edit_post', pid)           
            
    
    context= {
        'posts':posts,
        'photos':photos,
           
    }
    return render(request, 'delete_post_img.html', context)

# ------------------------------------------------------------
'''
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
def upload_file_view(request):
    request.upload_handlers.insert(0, ProgressBarUploadHandler(request))
    return _upload_file_view(request)

@csrf_protect
def _upload_file_view(request):
    ... # Process request
  '''  
    
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