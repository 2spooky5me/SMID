from apps.base.api.viewsets.method_mixins import GeneralModelViewSet
from ..serializers.ubicacion_serializers import UbicacionSerializer

class UbicacionViewSet(GeneralModelViewSet):
    serializer_class = UbicacionSerializer
    queryset = UbicacionSerializer.Meta.model.objects.filter(status=True).order_by('-id')
    
    # Por si se preguntan donde esta la validacion a traves del create, se encuentra en
    # la validacion del serializador UbicacionSerializer