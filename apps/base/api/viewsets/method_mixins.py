from rest_framework import viewsets, status
from rest_framework.response import Response

class GeneralModelViewSet(viewsets.ModelViewSet):
    serializer_class = None
    queryset = None
    
    def list(self, request):
        queryset = self.get_queryset().filter(status=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as exc:
            return Response({'error':f'{exc}'})
        
    def retrieve(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset().filter(id=pk, status=True).first())
        if queryset:
            serializer = self.get_serializer(queryset)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            {'error':f'No existe {self.serializer_class.Meta.model.__name__} con el id {pk}!.'},
            status=status.HTTP_404_NOT_FOUND
        )
    