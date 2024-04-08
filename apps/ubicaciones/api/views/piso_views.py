from rest_framework import status
from rest_framework.response import Response

from apps.base.api.viewsets.method_mixins import GeneralModelViewSet
from ..serializers.piso_serializers import PisoSerializer

class PisoViewSet(GeneralModelViewSet):
    serializer_class = PisoSerializer
    queryset = PisoSerializer.Meta.model.objects.filter(status=True).order_by('-id')
    
    def create(self, request, *args, **kwargs):
        request.data['name'] = request.data['name'].lower().capitalize()
        torre_exists = self.get_queryset().filter(name=request.data['name']).first()
        
        if torre_exists:
            torre = self.get_serializer(
                torre_exists
            )
            return Response(
                    {
                        "error":"Ya existe un piso con este nombre.",
                        "data": torre.data
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
        return super().create(request, *args, **kwargs)