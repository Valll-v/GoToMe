from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter

from accounts import views

router = DefaultRouter()
router.register("users", views.CustomUserViewSet)

User = get_user_model()

urlpatterns = router.urls
