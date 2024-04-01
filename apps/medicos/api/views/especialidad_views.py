from apps.base.api.generic_views import *
from ..serializers.especialidad_serializers import EspecialidadSerializer

class EspecialidadListAPIView(GeneralListAPIView):
    serializer_class = EspecialidadSerializer
    
class EspecialidadCreateAPIView(GeneralCreateAPIView):
    serializer_class = EspecialidadSerializer
    
class EspecialidadRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = EspecialidadSerializer