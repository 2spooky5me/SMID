from rest_framework import serializers
from ...models import Torre

# Serializador para el modelo Torre
class TorreSerializer(serializers.ModelSerializer):
    # Clase Meta contiene metadatos para el serializador
    class Meta:
        model = Torre # El modelo al que está vinculado el serializador
        fields = ('id', 'status', 'name') # Campos que se incluirán en la serialización
        # 'id' es la clave primaria del modelo
        # 'status' indica si la torre está activa o no
        # 'name' es el nombre de la torre