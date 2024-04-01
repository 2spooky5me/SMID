from apps.base.api.generic_views import *
from ..serializers.torre_serializers import TorreSerializer

class TorresListAPIView(GeneralListAPIView):
    serializer_class = TorreSerializer

class TorresCreateAPIView(GeneralCreateAPIView):
    serializer_class = TorreSerializer
    
class TorresRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = TorreSerializer