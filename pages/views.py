from django.shortcuts import render
from django.db.models import Q
from accounts.models import BusinessDetails, CoverImg, BusinessInfo, ProfileImg, Products, Gallery
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
import geocoder # Getting user location

# Create your views here.

lng = float(39.27492159469202)
lat = float(-6.819700757297852)
def get_coordinates(request):
    print("am receiving coordinates!!!!")
    global lat
    global lng
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)
    coordinates = [lat,lng]
    print(lat+"---"+lng)
    
    return coordinates

def index_view(request, *args, **kargs):
	
	context = {}
	return render(request, 'index.html', context)


def profile_view(request, *args, **kargs):
    id = kargs.get('id')
    user = request.user
    covers = CoverImg.objects.filter(user_id = id)
    logoimg = ProfileImg.objects.filter(user_id=id)
    info = BusinessInfo.objects.filter(user_id=id)
    details = BusinessDetails.objects.filter(user_id=id)
    photos = Gallery.objects.filter(user_id=id).all()
    products = Products.objects.filter(user_id=id).all()
    
    context={
        'covers':covers,
        'logoimg':logoimg,
        'info':info,
        'details':details,
        'photos':photos,
        'products':products,
    }
    return render(request, 'profile.html', context)


def products_all(request, *args, **kargs):
    userid = kargs.get('user_id')   
    products = Products.objects.filter(user_id=userid).all()
    
    
    context= {
        'products':products,
    }
    return render(request, 'products-all.html', context)


def product_view(request, *args, **kargs):
    id = kargs.get('id')
    userid = kargs.get('user_id')    
    products = Products.objects.filter(id=id, user_id=userid).all()    
    
    context= {
        'products':products,
    }
    return render(request, 'product-view.html', context)


def gallery(request, *args, **kargs):
    userid = kargs.get('user_id')
    photos = Gallery.objects.filter(user_id=userid)
    
    context= {
        'photos':photos,
    }
    return render(request, 'gallery-all.html', context)


def search_view(request, *args, **kargs):
    g = geocoder.ipinfo('me')
    print(lat)
    print(lng) 
    print(g.city)
 
    longitude = float(lng)
    latitude = float(lat)
    user_location = Point(longitude, latitude, srid=4326)
    
    if request.method == 'POST':
        query = request.POST.get('query')
        query_set = Q(city__icontains=query)|Q(business_name__icontains=query)|Q(street__icontains=query)|Q(business_type__icontains=query)
        infos = BusinessInfo.objects.filter(query_set)
        details = BusinessDetails.objects.all().annotate(distance=Distance('location', user_location)).order_by('distance')
        covers = CoverImg.objects.all()
    
    else:
        details = BusinessDetails.objects.annotate(distance=Distance('location', user_location)).order_by('distance')
        infos = BusinessInfo.objects.all()
        covers = CoverImg.objects.all()
    
    context = {
        'details':details,
        'infos':infos,
        'covers':covers, 
  
	}
    return render(request, 'search.html', context)

def search_category(request, *args, **kargs):    
    link_query = kargs.get('query')
    longitude = float(lng)
    latitude = float(lat)
    user_location = Point(longitude, latitude, srid=4326)
    
    if request.method == 'POST':
        query = request.POST.get('query')
        query_set = Q(city__icontains=query)|Q(business_name__icontains=query)|Q(street__icontains=query)|Q(business_type__icontains=query)
        infos = BusinessInfo.objects.filter(query_set)
        details = BusinessDetails.objects.all().annotate(distance=Distance('location', user_location)).order_by('distance')
        covers = CoverImg.objects.all()
    
    else:
        infos = BusinessInfo.objects.filter(business_type__icontains=link_query)
        details = BusinessDetails.objects.all().annotate(distance=Distance('location', user_location)).order_by('distance')        
        covers = CoverImg.objects.all()
    
    context = {
        'details':details,
        'infos':infos,
        'covers':covers, 
  
	}
    return render(request, 'search.html', context)

def orders_view(request, *args, **kargs):

	context = {}
	return render(request, 'orders.html', context)

def about_view(request, *args, **kargs):
    
	context = {}
	return render(request, 'about.html', context)

def contact_view(request, *args, **kargs):
    
	context = {}
	return render(request, 'contact.html', context)