from .views import LikeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"likes", LikeViewSet, basename="likes")

urlpatterns = router.urls