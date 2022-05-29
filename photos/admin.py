from django.contrib import admin
from .models import Photographer, Category, Image, Location

# Register your models here.
admin.site.register(Photographer)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Location)
admin.site.site_header = "M's PhotoHub - Administration"