from rest_framework import status
from rest_framework.response import Response

from apps.base.api.viewsets.method_mixins import GeneralModelViewSet
from ..serializers.especialidad_serializers import EspecialidadSerializer

class EspecialidadViewSet(GeneralModelViewSet):
    serializer_class = EspecialidadSerializer
    queryset = EspecialidadSerializer.Meta.model.objects.filter(status=True).order_by('-id')
    
    def create(self, request, *args, **kwargs):
        request.data['name'] = request.data['name'].lower().title()
        especialidad_exists = self.get_queryset().filter(name=request.data['name']).first()
        
        if especialidad_exists:
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
            
        return super().create(request, *args, **kwargs)