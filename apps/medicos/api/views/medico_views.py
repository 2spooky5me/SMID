from apps.base.api.generic_views import *
from ..serializers.medico_serializers import MedicoSerializer, MedicoReadOnlySerializer

class MedicoListAPIView(GeneralListAPIView):
    serializer_class = MedicoReadOnlySerializer

class MedicoCreateAPIView(GeneralCreateAPIView):
    serializer_class = MedicoSerializer
    
class MedicoRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = MedicoSerializer