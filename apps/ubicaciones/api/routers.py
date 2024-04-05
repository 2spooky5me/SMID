from rest_framework.routers import DefaultRouter
from apps.ubicaciones.api.views.piso_views import PisoViewSet
from apps.ubicaciones.api.views.torre_views import TorreViewSet
from apps.ubicaciones.api.views.localidad_views import LocalidadViewSet
from apps.ubicaciones.api.views.ubicacion_views import UbicacionViewSet

router = DefaultRouter()
router.register(r'piso_cpv', PisoViewSet)
router.register(r'torre_cpv', TorreViewSet)
router.register(r'localidad_cpv', LocalidadViewSet)
router.register(r'ubicacion', UbicacionViewSet)
urlpatterns = router.urls