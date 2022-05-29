from django.test import TestCase
from .models import Photographer, Category, Location, Image

# Create your tests here.
class Test_Photographer(TestCase):
    '''
    Test class for the Photographer model
    '''
    def setUp(self):
        self.maureen = Photographer(first_name = 'Maureen', last_name = 'Muriithi', email = 'moh2wanja@gmail.com', phone_number = '0713925352')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.maureen, Photographer))

    def test_save_photographer(self):
        self.maureen.save_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0)
    
    # def test_delete_photographer(self):
    #     self.maureen.delete_photographer()
    #     photographers = Photographer.objects.all()
    #     self.assertTrue(len(photographers) > 0)

class Test_Location(TestCase):
    '''
    Test class for the photos' location model
    '''
    def setUp(self):
        self.location = Location(name = 'Narobi')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_location()
        self.assertTrue(len(locations) > 0)

    def test_get_location(self):
        self.location.save_location()
        locations = Location.get_location()
        self.assertTrue(len(locations) > 1)

    def test_edit_location(self):
        new_location = 'Mombasa'
        self.location.save_location()
        self.location.edit_location(self.location.id, new_location)
        editted_location = Location.objects.filter(name='Mombasa')
        self.assertTrue(len(editted_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class Test_Category(TestCase):
    '''
    Test class for the photos' category model
    '''
    def setUp(self):
        self.category = Category(name = 'Food-category')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))
    
    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

class Test_Image(TestCase):
    '''
    Test class for the image model
    '''

    def setUp(self):
        self.location = Location(name='Paris')
        self.location.save_location()

        self.category = Category(name='Travel')
        self.category.save_category()

        self.image = Image(id=1, name='travelImage', description='This is the eiffel Tower in Paris', location=self.location, category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image.save_image()
        self.image.update_photo(self.image.id, 'photos/test.jpg')
        updated_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(updated_img) > 0)

    def test_filter_image_by_location(self):
        self.image.save_image()
        filtered_images = self.image.filter_by_location(location='nairobi')
        self.assertTrue(len(filtered_images) == 1)

    def test_search_image_by_category(self):
        category = 'food'
        searched_img = self.image.search_by_category(category)
        self.assertTrue(len(searched_img) > 1)

    def tearDown(self):
        Photographer.all().delete()
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


    


    
    