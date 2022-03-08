from django.test import TestCase
from .models import User_profile, Post
from django.contrib.auth.models import User


# Create your tests here.

class TestUser_profile(TestCase):

    def setUp(self):
        self.user = User(username='Prime')
        self.user.save()
        self.profile_test = User_profile(id=1, name='image', profile_picture='test.png', bio='this is a test User profile',
        user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, User_profile))
    
    def test_save_profile(self):
        self.profile_test.save_profile()
        after = User_profile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_profile(self):
        self.profile_test.delete_profile()
        profile = User_profile.objects.all()
        self.assertTrue(len(profile) == 0)    

class TestPost(TestCase):
    def setUp(self):
        self.profile_test = User_profile(name='Cosmas', user=User(username='prime'))
        self.profile_test.save()

        self.image_test = Post(user=self.profile_test,image='test.png', name='testing', caption='Testing caption',)
    def test_insatance(self):
        self.assertTrue(isinstance(self.image_test, Post))

