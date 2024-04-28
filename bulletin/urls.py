from rest_framework.routers import DefaultRouter
from bulletin.apps import BulletinConfig
from bulletin.views import BulletinViewSet

app_name = BulletinConfig.name

router = DefaultRouter()
router.register(r'ads', BulletinViewSet, basename='ads')

urlpatterns = router.urls
