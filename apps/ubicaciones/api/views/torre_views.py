from rest_framework import status
from rest_framework.response import Response

from apps.base.api.viewsets.method_mixins import GeneralModelViewSet
from ..serializers.torre_serializers import TorreSerializer

class TorreViewSet(GeneralModelViewSet):
    """
    ViewSet para la gestión de torres del CPV.
    """
    serializer_class = TorreSerializer
    queryset = TorreSerializer.Meta.model.objects.all().order_by('-id')
    
    def create(self, request, *args, **kwargs) -> Response:
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
        
        # Verificar si el campo "name" está presente en el JSON
        if "name" not in request.data:
            return Response(
                {"error": "El campo 'name' es obligatorio en el JSON enviado."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            tower_name_data = serializer.initial_data.get("name")

            #Verifica si el registro existe
            torre_existente = self.get_queryset().filter(
                name=tower_name_data.title()
            ).first()
            
            if torre_existente:
                # Si el registro existe, devolver un mensaje de error junto con los detalles del registro existente
                torre = self.get_serializer(torre_existente)
                return Response(
                    {
                        "error": f"Ya existe una torre con el nombre: '{tower_name_data}'",
                        "detail": torre.data
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        except AttributeError as exc:
            # Manejo de excepción de Atributos
            return Response(
                {'error':f'El campo "name" debe de ser string.'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        except Exception as exc:
            # Manejo de excepción genérica
            return Response(
                {'error':f'{exc}'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Validar y guardar la data del registro
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        
        # Devuelve el objeto creado a traves de una respuesta HTTP 201.
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED
        )