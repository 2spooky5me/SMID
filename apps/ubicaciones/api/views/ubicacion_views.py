from apps.base.api.generic_views import *
from ..serializers.ubicacion_serializers import *

class UbicacionListAPIView(GeneralListAPIView):
    serializer_class = UbicacionReadOnlySerializer

class UbicacionCreateAPIView(GeneralCreateAPIView):
    serializer_class = UbicacionSerializer
    
class UbicacionRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = UbicacionSerializer