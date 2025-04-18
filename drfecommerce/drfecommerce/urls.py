from django.contrib import admin
from django.urls import path, include

# for api documentation
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework.routers import DefaultRouter

from drfecommerce.product import views


router = DefaultRouter()
router.register(r"category", views.CategoryViewSet)
router.register(r"brand", views.BrandViewSet)
router.register(r"product", views.ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # The main api documentation page
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")), #name="swagger"
]
