from django.db import models

# Create your models here.
class Photographer(models.Model):
    '''
    Class to define the photo uploader
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name
    
    def save_photographer(self):
        self.save()
    
    def delete_photographer(self):
        self.delete()

class Location(models.Model):
    '''
    Class to show and update the images' location
    '''
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    @classmethod
    def get_location(cls):
        location = Location.objects.all()
        return location
    
    @classmethod
    def edit_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

class Category(models.Model):
    '''
    Class to categorize the images
    '''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Image(models.Model):
    '''
    Class to upload an image
    '''
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = ('image/'), default="")
    image_link = models.CharField(max_length=2048)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    photographer = models.ForeignKey(Photographer, on_delete= models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default="")

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls, search_term):
        searched_photo = cls.objects.filter(category__icontains=search_term)
        return searched_photo
    
    @classmethod
    def filter_by_location(cls, location):
        photo_location = Image.objects.filter(location__name=location).all()
        return photo_location
    
    @classmethod
    def update_photo(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_images(cls, id):
        images = cls.objects.filter(id=id).all()
        return images
    
    def __str__(self):
        return(self.name)

    
    class Meta:
        ordering = ['date_uploaded']
    

