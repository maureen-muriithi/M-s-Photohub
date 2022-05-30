from django.urls import path, URLPattern
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search_photos, name="search_photos"),
    path('images/', views.display_photos, name="display_photos")
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)