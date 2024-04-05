from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ...models import Ubicacion, Localidad
from .localidad_serializers import LocalidadSerializer

class UbicacionSerializer(serializers.ModelSerializer):
    location_cpv = serializers.PrimaryKeyRelatedField(
        queryset=Localidad.objects.filter(status=True), 
        many=False
    )
    
    class Meta:
        model = Ubicacion
        fields = ('id', 'status', 'its_cpv', 'location_cpv', 'location')
    
    def validate(self,attrs):
        
        if attrs['its_cpv']:
            
            if 'location' in attrs:
                raise serializers.ValidationError({
                    'error':'Necesita indicar unicamente la localidad del medico en el CPV.'
                })
            
            ubicacion_exists = Ubicacion.objects.filter(
                location_cpv=attrs['location_cpv']
                ).first()
            
            if ubicacion_exists:
                ubicacion = UbicacionSerializer(
                    ubicacion_exists
                )
                raise serializers.ValidationError(
                        {
                            "error":"Ya existe una ubicacion con la localidad del CPV suministrada.",
                            "data": ubicacion.data
                        }
                    )
        
        if not attrs['its_cpv'] and 'location_cpv' in attrs:
            raise serializers.ValidationError({
                'error':'Necesita indicar unicamente la localidad del medico.'
            })
            
        return super().validate(attrs)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        if data['its_cpv']:
            
            location_cpv_serializer = LocalidadSerializer(
                Localidad.objects.filter(status=True, id=data['location_cpv'])
                .first()
            )
            
            return {
                'id':data['id'],
                'status':data['status'],
                'its_cpv':data['its_cpv'],
                'location_cpv':location_cpv_serializer.data
            }
            
        return {
            'id':data['id'],
            'status':data['status'],
            'its_cpv':data['its_cpv'],
            'location':data['location']
        }