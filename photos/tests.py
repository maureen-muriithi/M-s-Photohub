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
    
    