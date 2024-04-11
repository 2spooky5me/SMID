from rest_framework import status
from rest_framework.response import Response

from apps.base.api.viewsets.method_mixins import GeneralModelViewSet
from ..serializers.especialidad_serializers import EspecialidadSerializer

class EspecialidadViewSet(GeneralModelViewSet):
    """
    ViewSet para la gestión de especialidades de los medicos.
    """
    serializer_class = EspecialidadSerializer
    queryset = EspecialidadSerializer.Meta.model.objects.filter(status=True).order_by('-id')
    
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
        # Serializa la data obtenida.
        serializer = self.get_serializer(data=request.data)

        # Verificar si el campo "name" está presente en el JSON
        if "name" not in request.data:
            return Response(
                {"error": "El campo 'name' es obligatorio en el JSON enviado."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            specialty_name_data = serializer.initial_data.get("name").lower().title()
            
            #Verifica si el registro existe
            especialidad_exists = self.get_queryset().filter(
                name=specialty_name_data
            ).first()
            
            if especialidad_exists:
                # Si el registro existe, devolver un mensaje de error junto con los detalles del registro existente.
                especialidad = self.get_serializer(
                    especialidad_exists
                )
                return Response(
                        {
                            "error":"Ya existe una especialidad con este nombre.",
                            "data": especialidad.data
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
            
        # Validar y guardar la data.
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        
        # Devuelve el objeto creado a traves de una respuesta HTTP 201.
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED
        )