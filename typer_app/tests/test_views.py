from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from django.urls import reverse

from typer_app import views


class TestMainView(TestCase):
    bool_test = True
    def setUp(self):
        self.url = reverse('home')

    def test_home_view(self):
        req = RequestFactory().get(self.url)
        req.user = AnonymousUser()
        resp = views.home(req)
        assert 'login' in resp.url









