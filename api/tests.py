from django.test import TestCase
from .models import User, Profile


# Create your tests here.
class ProfileCreateTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(username='test_user')

    def test_profile_create(self):
        user = User.objects.get(username='test_user')
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.name, f'user_{user.id}')
