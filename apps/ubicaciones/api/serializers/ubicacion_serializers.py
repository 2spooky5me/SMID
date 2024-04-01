from rest_framework import serializers
from ...models import Ubicacion, Localidad
from .localidad_serializers import LocalidadSerializer

class UbicacionReadOnlySerializer(serializers.ModelSerializer):
    location_cpv = LocalidadSerializer(many=False)
    
    class Meta:
        model = Ubicacion
        fields = ('id','its_cpv','location_cpv','location')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        if data['location_cpv']:
            data['location_cpv'] = LocalidadSerializer(instance.location_cpv).data
            return {'id':data['id'],
                    'its_cpv':data['its_cpv'],
                    'location_cpv':data['location_cpv']
                    }
        
        if data['location']:
            return {'id':data['id'],
                    'its_cpv':data['its_cpv'],
                    'location':data['location']
                    }

class UbicacionSerializer(UbicacionReadOnlySerializer):
    location_cpv = serializers.PrimaryKeyRelatedField(queryset=Localidad.objects.all(), many=False)
    
    def validate(self,data):
        
        if data['its_cpv'] == True and 'location_cpv' not in data or data['its_cpv'] == True and 'location' in data:
            raise serializers.ValidationError({
                'error':'Necesita indicar unicamente la localidad del medico en el CPV.'
                })
        
        if data['its_cpv'] == False and 'location' not in data or data['its_cpv'] == False and 'location_cpv' in data:
            raise serializers.ValidationError({
                'error':'Necesita indicar unicamente la localidad del medico.'
                })
            
        return data