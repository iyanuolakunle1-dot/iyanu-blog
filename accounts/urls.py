from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from django.urls import path
urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="auth-register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="auth-token"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
]