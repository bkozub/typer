
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from typer import serializers_urls
from typer_app.forms import LoginForm
from typer_app.views import TypeView, UserRankListView, guide, UserTypesView, \
    CompetitionResultView, CompetitionResultDetailView, UpdateProfileView, CreateCompetitionView

urlpatterns = [
    url(r'^api/', include(serializers_urls.router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^admin/', admin.site.urls),
    url(r'', include('typer_app.urls'), name='home'),
    url(r'^login/', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/', views.logout, {'next_page': '/login'}),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile/', UpdateProfileView.as_view(), name='profile'),
    url(r'^competition/add',CreateCompetitionView.as_view(), name='add_competition'),
    url(r'^type/', TypeView.as_view(), name='type'),
    url(r'^ranking', UserRankListView.as_view(), name='user_ranking'),
    url(r'^guide/', guide, name='how_to'),
    url(r'^usertypes/', UserTypesView.as_view(), name='user_types'),
    url(r'^competition/results', CompetitionResultView.as_view(), name='competition_results'),
    url(r'^competition/result/(?P<pk>[0-9]+)/$', CompetitionResultDetailView.as_view(), name='competition_results_detail'),

]