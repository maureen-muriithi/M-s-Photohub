from django.shortcuts import render


# Create your views here.
def home(request):
    heading = "Welcome to "
    title = "M's Photohub"
    return render(request, 'index.html', {"heading": heading, "title":title})

def search_photos(request):
    photo = 'My Photos'
    return render(request, 'search.html', {"photo": photo})