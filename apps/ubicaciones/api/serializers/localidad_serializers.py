from rest_framework import serializers
from ...models import Localidad, Torre, Piso
from .torre_serializers import TorreSerializer
from .piso_serializers import PisoSerializer

class LocalidadReadOnlySerializer(serializers.ModelSerializer):
    tower = TorreSerializer(many=False)
    floor = PisoSerializer(many=False)
    
    class Meta:
        model = Localidad
        fields = ('id','tower', 'floor', 'type_local', 'local')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        if data['type_local'] == 'CO':
            local = data['local']
            data['local'] = f'Consultorio {local}'
        return data

class LocalidadSerializer(LocalidadReadOnlySerializer):
    tower = serializers.PrimaryKeyRelatedField(queryset=Torre.objects.all(), many=False)
    floor = serializers.PrimaryKeyRelatedField(queryset=Piso.objects.all(), many=False)
