from django.test import TestCase
from .models import User_profile
from django.contrib.auth.models import User


# Create your tests here.

class TestUser_profile(TestCase):

    def setUp(self):
        self.user = User(username='Prime')
        self.user.save()
        self.profile_test = User_profile(id=1, name='image', profile_picture='default.png', bio='this is a test User profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, User_profile))
