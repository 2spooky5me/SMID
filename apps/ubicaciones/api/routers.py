from rest_framework.routers import DefaultRouter
from apps.ubicaciones.api.views.torre_views import TorreViewSet
from apps.ubicaciones.api.views.piso_views import PisoViewSet
from apps.ubicaciones.api.views.localidad_views import LocalidadViewSet

router = DefaultRouter()
router.register(r'torre_cpv', TorreViewSet, basename="torre-viewset")
router.register(r'piso_cpv', PisoViewSet, basename="piso-viewset")
router.register(r'localidad_cpv', LocalidadViewSet, basename="localidad-viewset")

urlpatterns = router.urls