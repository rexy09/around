from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
# Email
from django.core.mail import send_mail
from django.conf import settings
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
# Forms
from .models import BusinessInfo, BusinessDetails, CoverImg, ProfileImg, Gallery
from post.models import Post
from .forms import SignUpForm, LoginForm, BusinessInfoForm, BusinessDetailsForm, CoverImgForm, ProfileImgForm, GalleryImgForm
from .tokens import account_activation_token
# location point
from django.contrib.gis.geos import Point
from django.core.files import File
from PIL import Image
from io import BytesIO
import os
from django.db.models import Q
User = get_user_model()


# Create your views here.

# User login view
def login_view(request, *args, **kargs):    
    if request.method == 'POST':
            l_form = LoginForm(request.POST or None)
            if l_form.is_valid():
                 # Login Form
                username = l_form.cleaned_data.get('username')
                password = l_form.cleaned_data.get('password')
                user = User.objects.filter(Q(username=username)|Q(email=username)).first()
                # authentication
                if user == None:
                    messages.error(request, "Invalid username or password.")
                else:
                    if user.is_active == True:                        
                        user_auth = authenticate(request, username=user.username, password=password, is_active=True)
                        if user_auth is not None:
                            login(request, user_auth)
                            return redirect('/')
                        else:
                            messages.error(request, "Invalid username or password.")
                    else:
                        messages.error(request, "Account is not activated!, please check your email.")
            
    else:
        l_form = LoginForm()
        
    
    context={
        'l_form':l_form,        
    }
    
    return render(request, 'login.html', context)

# Signup view
def signup_view(request):
    if request.method == 'POST':
            s_form = SignUpForm(request.POST or None)
            if s_form.is_valid():
                # Sign Up Form
                user = s_form.save(commit=False)
                user.is_active = False
                email = s_form.cleaned_data.get('email')
                passwd1 = s_form.cleaned_data.get('password1')
                passwd2 = s_form.cleaned_data.get('password2')
                
                if passwd1 == passwd2:
                    user.set_password(passwd1)
                    user.save()
                    
                    current_site = get_current_site(request)
                    subject = 'Activate Your Around Tz Account'
                    message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                    })
                    from_email=settings.EMAIL_HOST_USER
                    user_email = email
                    to_email = [user_email,]
                    send_mail(subject, message, from_email, to_email )                
                   
                    return redirect('accounts:email_sent')
                   
                else:
                    messages.error(request, "Password must match")
                   
                
                
    else:
        s_form = SignUpForm()
    context ={
        's_form':s_form,        
    }
    return render(request, 'signup.html', context)

def confirmation_email(request, *args, **kwargs):
    return render(request, 'email_sent.html', {})

# logout view
def logout_view(request, *args, **kwargs):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect('index')
    context = {

	}
    return render(request, 'signup.html', context)


# Account activation
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('accounts:activation_success')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('<h4>Invalid Activation link!</h4>')

def activation_success(request):
    return render(request, 'activation_success.html', {})


# Password rest
def password_reset_view(request):
    
	return render(request, 'password_reset.html', {})

@login_required
def myprofile_view(request, *args, **kwargs):
    user = request.user
    covers = CoverImg.objects.filter(user_id = user.id)
    logoimg = ProfileImg.objects.filter(user_id=user.id)
    info = BusinessInfo.objects.filter(user_id=user.id)
    details = BusinessDetails.objects.filter(user_id=user.id)
    photos = Gallery.objects.filter(user_id=user.id).all()
    posts = Post.objects.filter(author_id=user.id).all()
    
    context={
        'covers':covers,
        'logoimg':logoimg,
        'info':info,
        'details':details,
        'photos':photos,
        'posts':posts,
    }
    
    return render(request, 'myprofile.html', context)



def psettings_view(request, *args, **kargs):
    
    context= {
        
    }
    return render(request, 'psettings.html', context)



# BUSINESS INFO
@login_required
def businessinfo(request, *args, **kargs):
    user = request.user
    info_obj = BusinessInfo.objects.filter(user_id=user.id).first()
    
    if request.method == 'POST':
            form = BusinessInfoForm(request.POST or None, instance=info_obj)
            if form.is_valid():
                info = form.save(commit=False)
                info.user = user
                info.save()
                
                return redirect('accounts:myprofile')
                
    else:
        if info_obj == '':
            form = BusinessInfoForm()
        else:
            form = BusinessInfoForm(instance=info_obj)
            
    context= {        
        'form':form,        
    }
    return render(request, 'business_info.html', context)



@login_required
def businessdetails_view(request, *args, **kargs):
    
    user = request.user
    details_obj = BusinessDetails.objects.filter(user_id=user.id).first()
    
    if request.method =='POST':
        form = BusinessDetailsForm(request.POST or None, instance=details_obj) # None means initialize empty form
        if form.is_valid():
            details = form.save(commit=False)
            details.user = user
            longitude = form.cleaned_data.get('longitude')
            latitude = form.cleaned_data.get('latitude')
            point = Point((longitude, latitude), srid=4326)
            details.location = point          
            details.save()
            
            return redirect('accounts:myprofile')
        
    else:
        if details_obj == '':
            form = BusinessDetailsForm()
        else:
            form = BusinessDetailsForm(instance=details_obj)     
    
        
    context= {
        'form':form,
        
    }
    return render(request, 'business_details.html', context)



@login_required
def cover_img(request, *args, **kargs):
    user = request.user
    photos = CoverImg.objects.filter(user_id=user.id)
    image_path = False
    for p in photos:
        image_path = p.image.path
        
    # Call the delete function
    # photos.delete()
    
    if request.method == 'POST':
        if image_path == False:
            pass
        else:
            os.remove(image_path)
        form = CoverImgForm(request.POST, request.FILES)
        if form.is_valid():
            cover = form.save(commit=False)
            cover.user = user
            x = form.cleaned_data.get('x')
            y = form.cleaned_data.get('y')
            w = form.cleaned_data.get('width')
            h = form.cleaned_data.get('height')
            image = form.cleaned_data.get('image')
            
            img = Image.open(image)
            rgb_im = img.convert('RGB')
            cropped_image = rgb_im.crop((x, y, w+x, h+y))
            im_io = BytesIO() 
            cropped_image.save(im_io, 'JPEG', quality=85,)
            newimage = File(im_io, name=image.name)
            cover.image = newimage
            cover.save()
            return redirect('accounts:myprofile')
    else:
        form = CoverImgForm()
    
    context= {
        'form':form,
        'photos':photos,
    }
    return render(request, 'cover.html', context)

@login_required
def cover_img_delete(request, *args, **kargs):
    id = kargs.get('id')
    user = request.user
    photos = CoverImg.objects.filter(user_id=user.id)
    image_path = False
    for p in photos:
        image_path = p.image.path
        
    # Call the delete function    
    if request.method == 'POST':
            os.remove(image_path)
            photos.delete()
        
            return redirect('accounts:myprofile')
    
    context= {
        'photos':photos,
    }
    return render(request, 'cover_delete.html', context)

@login_required
def profile_img(request):
    user = request.user
    photos = ProfileImg.objects.filter(user_id=user.id)
    image_path = False
    for p in photos:
        image_path = p.image.path
    
    if request.method == 'POST':
        if image_path == False:
                pass
        else:
            os.remove(image_path)
            
        form = ProfileImgForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            x = form.cleaned_data.get('x')
            y = form.cleaned_data.get('y')
            w = form.cleaned_data.get('width')
            h = form.cleaned_data.get('height')
            image = form.cleaned_data.get('image')
            
            img = Image.open(image)
            rgb_im = img.convert('RGB')
            cropped_image = rgb_im.crop((x, y, w+x, h+y))
            im_io = BytesIO() 
            cropped_image.save(im_io, 'JPEG', quality=85,)
            newimage = File(im_io, name=image.name)
            profile.image = newimage
            profile.save()
            return redirect('accounts:myprofile')
    else:
        form = ProfileImgForm()
    
    context= {
        'form':form,
        'photos':photos,
    }
    return render(request, 'profile_img.html', context)


@login_required
def profile_img_delete(request, *args, **kwargs):
    id = kwargs.get('id')
    user = request.user
    photos = ProfileImg.objects.filter(user_id=user.id)
    image_path = False
    for p in photos:
        image_path = p.image.path
    
    if request.method == 'POST':
        os.remove(image_path)
        photos.delete()
        return redirect('accounts:myprofile')
        
    context= {
        'photos':photos,
    }
    return render(request, 'profile_img_delete.html', context)



@login_required
def gallery(request, *args, **kargs):
    user = request.user
    photos = Gallery.objects.filter(user_id=request.user.id).order_by('-date_updated')
    if request.method == 'POST':
        form = GalleryImgForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        if form.is_valid():
                        
            for file in files:            
                img = Image.open(file)
                rgb_im = img.convert('RGB')
                im_io = BytesIO() 
                rgb_im.save(im_io, 'JPEG', quality=85,)
                newimage = File(im_io, name=file.name)
                gallery = Gallery(user=user, image=newimage)
                gallery.save()
            return redirect('accounts:myprofile')
    else:
        form = GalleryImgForm()
    
    context= {
        'form':form,
        'photos':photos,
    }
    return render(request, 'gallery.html', context)

@login_required
def gallery_delete(request, *args, **kargs):
    id = kargs.get('id')
    user = request.user
    photos = Gallery.objects.filter(id=id, user_id=user.id)
    img_path = False
    for p in photos:
        img_path = p.image.path
        
    if request.method == 'POST':
        os.remove(img_path)
        photos.delete()
        
        return redirect('accounts:myprofile')   
        
  
    context= {
        'photos':photos,
    }
    return render(request, 'gallery_delete.html', context)