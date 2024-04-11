from rest_framework import serializers
from ...models import Especialidad

class EspecialidadSerializer(serializers.ModelSerializer):
    # Clase Meta contiene metadatos para el serializador
    class Meta:
        model = Especialidad
        fields = ('id', 'status', 'name')
        # 'id' es la clave primaria del modelo
        # 'status' indica si la especialidad está activa o no
        # 'name' es el nombre de la especialidad