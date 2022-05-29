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

