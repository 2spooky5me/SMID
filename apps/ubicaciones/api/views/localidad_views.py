from rest_framework import status
from rest_framework.response import Response

from apps.base.api.viewsets.method_mixins import GeneralModelViewSet
from ..serializers.localidad_serializers import LocalidadSerializer

class LocalidadViewSet(GeneralModelViewSet):
    serializer_class = LocalidadSerializer
    queryset = LocalidadSerializer.Meta.model.objects.filter(status=True).order_by('-id')
    
    def create(self, request, *args, **kwargs):
        request.data['local'] = request.data['local'].capitalize()
        location_exists = self.get_queryset().filter(
            tower=request.data['tower'], floor=request.data['floor'], 
            type_local=request.data['type_local'], local=request.data['local']
            ).first()
        
        if location_exists:
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
            
        return super().create(request, *args, **kwargs)