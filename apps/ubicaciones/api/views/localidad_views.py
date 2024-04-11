from rest_framework import status
from rest_framework.response import Response

from apps.base.api.viewsets.method_mixins import GeneralModelViewSet
from ..serializers.localidad_serializers import LocalidadSerializer

class LocalidadViewSet(GeneralModelViewSet):
    """
    ViewSet para la gestión de localidades del CPV.
    """
    serializer_class = LocalidadSerializer
    queryset = LocalidadSerializer.Meta.model.objects.all().order_by('-id')
    
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
        serializer = self.get_serializer(data=request.data)
        
        campos_requeridos = ["tower", "floor", "type_local", "local"]
        
        # Verifica si "tower", "floor", "type_local" y "local" estan en el request.
        if all(campo in request.data for campo in campos_requeridos):
            
            try:
                # Guardado de los datos del request en variables.
                tower_data = serializer.initial_data.get("tower")
                floor_data = serializer.initial_data.get("floor")
                type_local_data = serializer.initial_data.get("type_local")
                local_data = None if request.data["local"] == None else serializer.initial_data.get("local").capitalize()
                
                #Verifica si el registro existe
                location_exists = self.get_queryset().filter(
                    tower=tower_data, floor=floor_data, 
                    type_local=type_local_data, local=local_data
                ).first()
                
                if location_exists:
                    # Si el registro existe, devolver un mensaje de error junto con los detalles del registro existente
                    location = self.get_serializer(
                        location_exists
                    )
                    return Response(
                            {
                                "error":"Ya existe una localidad con los datos suministrados.",
                                "data": location.data
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )
                    
            except Exception as exc:
                # Manejo de excepción genérica
                return Response(
                    {'error':f'{exc}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        # Validar y guardar la data el registro
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        
        # Devuelve el objeto creado a traves de una respuesta HTTP 201.
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED
        )