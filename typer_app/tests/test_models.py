import unittest
from unittest import TestCase

import pytest
from django.contrib.auth.models import User
from mixer.backend.django import mixer

from typer_app.models import UserProfile

@pytest.mark.django_db
class TestMainView(TestCase):
    def setUp(self):
        self.user = mixer.blend(User)

    def test_user_profile_create_signal(self):
        self.user.save()
        self.assertIn(self.user.id,UserProfile.objects.values_list('user',flat=True))


if __name__ == "__main__":
    unittest.main()
