from rest_framework.routers import DefaultRouter
from apps.medicos.api.views.especialidad_views import EspecialidadViewSet
from apps.medicos.api.views.medico_views import MedicoViewSet
from apps.medicos.api.views.ubicacion_views import UbicacionViewSet

router = DefaultRouter()
router.register(r'especialidad', EspecialidadViewSet)
router.register(r'medico', MedicoViewSet)
router.register(r'ubicacion', UbicacionViewSet, basename="ubicacion-viewset")
urlpatterns = router.urls