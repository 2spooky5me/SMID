from apps.base.api.generic_views import *
from ..serializers.piso_serializers import PisoSerializer

class PisoListAPIView(GeneralListAPIView):
    serializer_class = PisoSerializer

class PisoCreateAPIView(GeneralCreateAPIView):
    serializer_class = PisoSerializer
    
class PisoRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = PisoSerializer