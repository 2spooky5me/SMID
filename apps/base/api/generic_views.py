from rest_framework import generics, status
from rest_framework.response import Response

class GeneralListAPIView(generics.ListAPIView):
    serializer_class = None
    
    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk:
            return model.objects.filter(id = pk, status = True).first()
        else:
            return model.objects.filter(status = True)
    
    def get(self, request, pk=None):
        if pk:
            model = self.get_queryset(pk)
            serializer = self.get_serializer(model, many=False)
            if model == None:
                return Response({'error':f'No existe {serializer.Meta.model.__name__} con el id {pk}!.'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            model = self.get_queryset()
            serializer = self.get_serializer(model, many=True)
        return Response(serializer.data)
    
class GeneralCreateAPIView(generics.CreateAPIView):
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'{serializer.Meta.model.__name__} creado correctamente',
                            'object':serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GeneralRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = None
    
    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk:
            return model.objects.filter(id = pk, status = True).first()
        return model.objects.filter(status = True)
    
    def patch(self, request, pk=None):
        
        if self.get_queryset(pk):
            serializer = self.get_serializer(self.get_queryset(pk), data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'error':f'No existe {serializer.Meta.model.__name__} con estos datos!.'}, 
                        status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        
        if self.get_queryset(pk):
            serializer = self.get_serializer(self.get_queryset(pk), data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'error':f'No existe {serializer.Meta.model.__name__} con estos datos!.'}, 
                        status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        serializer_class = self.get_serializer()
        data = self.get_queryset().filter(id=pk).first()
        
        if data:
            data.status=False
            data.save()
            return Response({'message':f'{serializer_class.Meta.model.__name__} eliminado correctamente!.'}, 
                            status=status.HTTP_200_OK)
        return Response({'message':f'No existe {serializer_class.Meta.model.__name__} con estos datos!.'}, 
                        status=status.HTTP_400_BAD_REQUEST)