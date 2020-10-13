from django.contrib.auth.models import User
from django.test import TestCase
from faker import Faker

from accounts.models import Profile

f = Faker()


# Create your tests here.

class AccountsTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_create_user(self):
        email = f.email()
        user = User.objects.create_user(
            username=f.user_name(),
            email=f.email(),
            password=f.password()
        )
        profile = Profile.object.get(user_id=user.id)
        self.assertEqual(profile.nickname, email)

    def test_profile_age(self):

        pass

    def tearDown(self) -> None:
        pass
