"""typer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from typer import settings
from typer_app.forms import LoginForm
from typer_app.views import update_profile, create_competition, type, JumperViewSet, CompetitionViewSet

router = routers.DefaultRouter()
router.register(r'v1/jumper', JumperViewSet, base_name="Jumpers"),
router.register(r'v1/competition', CompetitionViewSet, base_name="Competitions")



urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^admin/', admin.site.urls),
    url(r'', include('typer_app.urls'), name='home'),
    url(r'^login/', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/', views.logout, {'next_page': '/login'}),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile/', update_profile, name='profile'),
    url(r'^competition/add',create_competition, name='add_competition'),
    url(r'^type', type, name='type'),
]