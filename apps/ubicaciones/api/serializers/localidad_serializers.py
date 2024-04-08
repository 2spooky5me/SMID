from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ...models import Localidad, Torre, Piso
from .torre_serializers import TorreSerializer
from .piso_serializers import PisoSerializer
        
class LocalidadSerializer(serializers.ModelSerializer):
    tower = serializers.PrimaryKeyRelatedField(
        queryset=Torre.objects.filter(status=True), 
        many=False
    )
    floor = serializers.PrimaryKeyRelatedField(
        queryset=Piso.objects.filter(status=True),
        many=False
    )
    
    class Meta:
        model = Localidad
        fields = ('id', 'status', 'tower', 'floor', 'type_local', 'local')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        tower_serializer = TorreSerializer(
            Torre.objects.filter(status=True, id=data['tower'])
            .first()
        )
        data['tower'] = tower_serializer.data
        
        floor_serializer = PisoSerializer(
            Piso.objects.filter(status=True, id=data['floor'])
            .first()
        )
        data['floor'] = floor_serializer.data
            
        return data