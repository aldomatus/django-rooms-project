# Django
from django.test import TestCase

# Python
import os
import random
import environ

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

from users.models import User

env = environ.Env()
environ.Env.read_env()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


class UserTestCase(TestCase):
    def setUp(self):
        user = User(
            user_email='testing_login@cosasdedevs.com',
            is_admin=False
        )
        user.save()
        random_number = str(random.randint(10, 1000))
        self.email = f"aldo.matus{random_number}@gmail.com"
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    def test_signup_user(self):
        """Check if we can create an user"""

        client = APIClient()
        response = client.post(
            '/users/signup/', {
                "user_email": "aldomm61@gmail.com",
                "is_admin": 0
            },
            # format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
