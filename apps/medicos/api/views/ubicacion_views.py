from apps.base.api.viewsets.method_mixins import GeneralModelViewSet
from ..serializers.ubicacion_serializers import UbicacionSerializer

class UbicacionViewSet(GeneralModelViewSet):
    """
    ViewSet para la gestión de ubicaciones de los medicos.
    """
    serializer_class = UbicacionSerializer
    queryset = UbicacionSerializer.Meta.model.objects.filter(status=True).order_by('-id')
    
    def create(self, request, *args, **kwargs):
        """
        Crea una nueva instancia del modelo con los datos proporcionados.

        Este método toma los datos de la solicitud y crea una nueva instancia del modelo.
        Si la creación es exitosa, devuelve la nueva instancia. En caso de error, devuelve un mensaje adecuado.

        Args:
            request: La solicitud HTTP.
            *args: Argumentos variables.
            **kwargs: Argumentos de palabras clave variables.

        Returns:
            Response: Una respuesta HTTP con la nueva instancia creada o un mensaje de error.
        """
        return super().create(request, *args, **kwargs)
    # Por si se preguntan donde esta la validacion a traves del create, se encuentra en
    # la validacion del serializador UbicacionSerializer