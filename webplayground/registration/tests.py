from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com',
                                 password='test1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)
