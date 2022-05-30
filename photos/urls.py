from django.urls import path, URLPattern
from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search_results, name="search"),
    path('images/', views.display_photos, name="display_photos"),
    url(r'^location/(?P<location_name>\w+)/', views.image_location, name='location'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)