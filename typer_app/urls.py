from django.conf.urls import url
from django.views.generic import RedirectView

from django.conf.urls import url
from . import views

# We are adding a URL called /home
from typer_app.forms import LoginForm

urlpatterns = [
    url(r'^$', views.home, name='home'),
    ]

