from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ...models import Localidad, Torre, Piso
from .torre_serializers import TorreSerializer
from .piso_serializers import PisoSerializer

# Serializador para el modelo Localidad
class LocalidadSerializer(serializers.ModelSerializer):
    # Campo 'tower' que hace referencia a la clave primaria de Torre
    # Solo incluye objetos de Torre con status=True
    tower = serializers.PrimaryKeyRelatedField(
        queryset=Torre.objects.filter(status=True), 
        many=False
    )
    
    # Campo 'floor' que hace referencia a la clave primaria de Piso
    # Solo incluye objetos de Piso con status=True
    floor = serializers.PrimaryKeyRelatedField(
        queryset=Piso.objects.filter(status=True),
        many=False
    )
    
    # Clase Meta contiene metadatos para el serializador
    class Meta:
        model = Localidad # El modelo al que está vinculado el serializador
        fields = ('id', 'status', 'tower', 'floor', 'type_local', 'local') # Campos que se incluirán en la serialización
        # 'id' es la clave primaria del modelo
        # 'status' indica si la torre está activa o no
        # 'tower' es la Torre vinculada con la Localidad
        # 'floor' es el Piso vinculado con la Localidad
        # 'type_local' es el tipo de localidad.
        # 'local' nombre de la localidad.
    
    # Método para representar los datos del modelo Localidad, sobreescrita para serializar la Torre y el Piso.
    def to_representation(self, instance):
        # Llama al método to_representation del padre para obtener el diccionario inicial
        data = super().to_representation(instance)

        # Serializa el objeto Torre relacionado y lo añade al diccionario 'data'
        tower_serializer = TorreSerializer(
            Torre.objects.filter(status=True, id=data['tower'])
            .first() # Obtiene la primera instancia que coincide
        )
        data['tower'] = tower_serializer.data
        
        # Serializa el objeto Piso relacionado y lo añade al diccionario 'data'
        floor_serializer = PisoSerializer(
            Piso.objects.filter(status=True, id=data['floor'])
            .first() # Obtiene la primera instancia que coincide
        )
        data['floor'] = floor_serializer.data
            
        return data # Devuelve el diccionario 'data' actualizado