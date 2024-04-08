from rest_framework.routers import DefaultRouter
from apps.medicos.api.views.especialidad_views import EspecialidadViewSet
from apps.medicos.api.views.medico_views import MedicoViewSet

router = DefaultRouter()
router.register(r'especialidad', EspecialidadViewSet)
router.register(r'medico', MedicoViewSet)
urlpatterns = router.urls