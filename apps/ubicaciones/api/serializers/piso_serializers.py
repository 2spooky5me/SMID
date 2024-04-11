from rest_framework import serializers
from ...models import Piso

# Serializador para el modelo Piso
class PisoSerializer(serializers.ModelSerializer):
    
    # Clase Meta contiene metadatos para el serializador
    class Meta:
        model = Piso # El modelo al que está vinculado el serializador
        fields = ('id', 'status', 'name') # Campos que se incluirán en la serialización
        # 'id' es la clave primaria del modelo
        # 'status' indica si la torre está activa o no
        # 'name' es el nombre de la torre