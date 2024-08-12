from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import QuerySet
# from rest_framework.permissions import IsAuthenticated




class GeneralModelViewSet(viewsets.ModelViewSet):
    # `serializer_class` y `queryset` deben ser definidos en las clases hijas.
    serializer_class = None
    queryset = None
    # permission_classes = (IsAuthenticated, )
    
    def list(self, request):
        """
        Devuelve una lista de instancias activas del modelo.

        Este método se sobrescribe para filtrar la queryset por el estado activo.
        Si se configura la paginación, se devuelve una respuesta paginada.
        De lo contrario, se devuelve una lista completa de instancias activas.

        Args:
            request: La solicitud HTTP.

        Returns:
            Response: Una respuesta HTTP con datos serializados de instancias activas.
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """
        Recupera una instancia específica del modelo por su ID.

        Filtra la queryset por ID y estado activo. Si la instancia existe,
        devuelve los datos serializados. Si no, devuelve un error 404.

        Args:
            request: La solicitud HTTP.
            pk: El identificador primario de la instancia a recuperar.

        Returns:
            Response: Una respuesta HTTP con los datos de la instancia o un mensaje de error.
        """
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
            
    def update(self, request, *args, **kwargs):
        """
        Actualiza una instancia del modelo con los datos proporcionados.

        Este método toma los datos de la solicitud y actualiza la instancia del modelo correspondiente.
        Si la actualización es exitosa, devuelve la instancia actualizada. En caso de error, devuelve un mensaje adecuado.

        Args:
            request: La solicitud HTTP.
            *args: Argumentos variables.
            **kwargs: Argumentos de palabras clave variables.

        Returns:
            Response: Una respuesta HTTP con la instancia actualizada o un mensaje de error.
        """
        return super().partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Actualiza parcialmente una instancia del modelo con los datos proporcionados.

        A diferencia del método 'update', este método permite actualizar solo algunos campos de la instancia.
        Si la actualización parcial es exitosa, devuelve la instancia actualizada. Si no, devuelve un mensaje de error.

        Args:
            request: La solicitud HTTP.
            *args: Argumentos variables.
            **kwargs: Argumentos de palabras clave variables.

        Returns:
            Response: Una respuesta HTTP con la instancia actualizada parcialmente o un mensaje de error.
        """
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        Elimina una instancia del modelo.

        Intenta eliminar la instancia utilizando el método 'destroy' estándar.
        Si ocurre una excepción, devuelve un error con estado HTTP 401 No Autorizado.

        Args:
            request: La solicitud HTTP.
            *args: Argumentos variables.
            **kwargs: Argumentos de palabras clave variables.

        Returns:
            Response: Una respuesta HTTP con el resultado de la operación de eliminación.
        """
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as exc:
            return Response(
                {'error':f'{exc}'},
                status=status.HTTP_401_UNAUTHORIZED
            )