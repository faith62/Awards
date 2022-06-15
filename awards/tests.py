from django.test import TestCase
from .models import Image,Profile,Comment,Stream,Follow,Likes

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.Africa = Image(image_name ="Africa",image_description ="Our Continent", design=1,usability=1,content=1,vote_submissions=2,url="ww.africa.com")
        self.Africa.save_image()    

    def test_instance(self):
        self.assertTrue(isinstance(self.Africa,Image))
    # Testing Save Method
    def test_save_method(self):
        self.Africa.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.Africa.save_image() 
        self.Africa.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image) == 0)
class ProfileTestClass(TestCase):

    def setUp(self):
        self.Faith = Profile(first_name = "Faith",last_name = "Chemutai",bio="Love and Life",  url="www.faith.com")
        self.Faith.save_profile()    

    def test_instance(self):
        self.assertTrue(isinstance(self.Faith,Profile))
    # Testing Save Method
    def test_save_method(self):
        self.Faith.save_profile()
        profiles= Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.Faith.save_profile()
        self.Faith.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)


    
       
