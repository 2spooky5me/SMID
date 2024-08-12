from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters
#from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Prefetch

from apps.base.api.viewsets.method_mixins import GeneralModelViewSet
from apps.medicos.models import Ubicacion
from ..serializers.medico_serializers import MedicoSerializer

class MedicoViewSet(GeneralModelViewSet):
    """
    ViewSet para la gestión de medicos.
    """
    serializer_class = MedicoSerializer
    queryset = MedicoSerializer.Meta.model.objects.all().order_by('last_name')\
        .prefetch_related(
            "specialties", 
            # "location__medicos_ubicacion__ubicacion__location_cpv__tower",
            # "location__medicos_ubicacion__ubicacion__location_cpv__floor",
            Prefetch("location", Ubicacion.objects.select_related("location_cpv__tower", "location_cpv__floor"))
            )\
        .select_related("changed_by")
    
    search_fields = [
        'code', 'rif', 'identification', 
        'first_name', 'second_name', 'last_name',
        'second_last_name', 'specialties__name',
        'location__location_cpv__tower__name',
        'location__location_cpv__floor__name',
        'location__location'
        ]
    
    
    
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
        # Serializa la data obtenida y comprueba si es valida.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Verifica si un registro con el mismo "code", "identification" o "rif" ya existe.
        medico_exists = self.get_queryset().filter(
            Q(code=serializer.initial_data.get("code")) | 
            Q(identification=serializer.initial_data.get("identification")) |
            Q(rif=serializer.initial_data.get("rif")) 
        ).first()
        
        if medico_exists:
            # Si el registro existe, devolver un mensaje de error junto con los detalles del registro existente.
            medico = self.get_serializer(
                medico_exists
            )
            field_mapping = {
                'code': 'el codigo suministrado',
                'rif': 'el rif suministrado',
                'identification': 'la cedula suministrada'
            }
            # Devuelve el mensaje correspondiente dependiendo de cual fue el dato que existe del registro junto con el registro.
            for field, field_name in field_mapping.items():
                if getattr(medico_exists, field) == request.data[field]:
                    return Response(
                    {
                        "error":f"Ya existe un medico con {field_name}'.",
                        "data": medico.data
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        # Guarda el registro en al base de datos.
        serializer.save()
        return super().create(request, *args, **kwargs)