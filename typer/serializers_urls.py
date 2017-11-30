from rest_framework import routers

from typer_app.views import JumperViewSet, CompetitionViewSet

router = routers.DefaultRouter()
router.register(r'v1/jumper', JumperViewSet, base_name="Jumpers"),
router.register(r'v1/competition', CompetitionViewSet, base_name="Competitions")