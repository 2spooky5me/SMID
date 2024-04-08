from rest_framework import status
from rest_framework.response import Response

from apps.base.api.viewsets.method_mixins import GeneralModelViewSet
from ..serializers.torre_serializers import TorreSerializer

class TorreViewSet(GeneralModelViewSet):
    serializer_class = TorreSerializer
    queryset = TorreSerializer.Meta.model.objects.filter(status=True).order_by('-id')
    
    def create(self, request, *args, **kwargs):
        request.data['name'] = request.data['name'].lower().capitalize()
        piso_exists = self.get_queryset().filter(name=request.data['name']).first()
        
        if piso_exists:
            piso = self.get_serializer(
                piso_exists
            )
            return Response(
                    {
                        "error":"Ya existe una torre con este nombre.",
                        "data": piso.data
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
        return super().create(request, *args, **kwargs)