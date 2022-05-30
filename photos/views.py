from django.shortcuts import render
from .models import Image, Location, Category
import datetime as dt


# Create your views here.
def home(request):
    heading = "Welcome to "
    title = "M's Photohub"
    return render(request, 'index.html', {"heading": heading, "title":title})

def search_photos(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_photos = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def display_photos(request):
    date = dt.date.today()
    images = Image.objects.all()
    categories = Category.objects.all()
    locations = Location.get_location()
    return render(request, 'display_images.html', {"date": date,"images":images, "locations":locations, "categories": categories})

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'location_images': images})