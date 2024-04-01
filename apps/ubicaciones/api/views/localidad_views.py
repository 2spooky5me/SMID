from apps.base.api.generic_views import *
from ..serializers.localidad_serializers import *

class LocalidadListAPIView(GeneralListAPIView):
    serializer_class = LocalidadReadOnlySerializer

class LocalidadCreateAPIView(GeneralCreateAPIView):
    serializer_class = LocalidadSerializer
    
class LocalidadRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = LocalidadSerializer