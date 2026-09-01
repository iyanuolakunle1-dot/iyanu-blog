from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("accounts.urls")),
    path("api/", include("posts.urls")),
    path("api/", include("comments.urls")),
    path("api/", include("likes.urls")),
    path("api/doc/", SpectacularAPIView.as_view(), name="docs"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="docs"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="docs"), name="redoc-ui")
]


urlpatterns += static(
    settings.MEDIA_URL, 
    document_root = settings.MEDIA_ROOT
)
