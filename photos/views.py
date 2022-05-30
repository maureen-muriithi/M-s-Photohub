from email.mime import message
from unicodedata import category
from django.shortcuts import render
from .models import Image, Location, Category
import datetime as dt


# Create your views here.
def home(request):
    heading = "Welcome to "
    title = "M's Photohub"
    return render(request, 'index.html', {"heading": heading, "title":title})

def display_photos(request):
    date = dt.date.today()
    images = Image.objects.all()
    categories = Category.objects.all()
    locations = Location.get_location()
    return render(request, 'display_images.html', {"date": date,"images":images, "locations":locations, "categories": categories})

def image_location(request, location_name):
    images = Image.filter_by_location(location_name)
    locations = Location.get_location()
    message = f"{location_name}"
    print(images)
    return render(request, 'location.html', {'location_images': images, "locations": locations, "message":message})

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_photo = Image.search_by_category(category)
        message = f"{category}"
        print(searched_photo)
        return render(request, 'search.html', {"message": message, "images": searched_photo})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html', {"message": message})
