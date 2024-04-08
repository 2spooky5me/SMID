from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q

from apps.base.api.viewsets.method_mixins import GeneralModelViewSet
from ..serializers.medico_serializers import MedicoSerializer

class MedicoViewSet(GeneralModelViewSet):
    serializer_class = MedicoSerializer
    queryset = MedicoSerializer.Meta.model.objects.filter(status=True).order_by('-id')
    search_fields = ['first_name']
    
    def create(self, request, *args, **kwargs):
        medico_exists = self.get_queryset().filter(
            Q(code=request.data['code']) | 
            Q(identification=request.data['identification']) |
            Q(rif=request.data['rif']) 
        ).first()
        
        # Si se encuentra una coincidencia, determina qué campo fue el responsable
        if medico_exists:
            medico = self.get_serializer(
                medico_exists
            )
            field_mapping = {
                'code': 'el codigo suministrado',
                'rif': 'el rif suministrado',
                'identification': 'la cedula suministrada'
            }
            for field, field_name in field_mapping.items():
                if getattr(medico_exists, field) == request.data[field]:
                    return Response(
                    {
                        "error":f"Ya existe un medico con {field_name}'.",
                        "data": medico.data
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
        # if medico_exists:
        #     medico = self.get_serializer(
        #         medico_exists
        #     )
        #     return Response(
        #             {
        #                 "error":"Ya existe un medico con este nombre.",
        #                 "data": medico.data
        #             },
        #             status=status.HTTP_400_BAD_REQUEST
        #         )
            
        return super().create(request, *args, **kwargs)