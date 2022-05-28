from urllib.parse import urlparse
from django.conf import urls
from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('/search', views.search_photos, name="photo"),
]