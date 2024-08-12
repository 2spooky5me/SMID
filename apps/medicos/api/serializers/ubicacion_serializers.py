from rest_framework import serializers

from ...models import Ubicacion
from apps.ubicaciones.models import Localidad
from apps.ubicaciones.api.serializers.localidad_serializers import LocalidadSerializer

# Serializador para el modelo Ubicacion
class UbicacionSerializer(serializers.ModelSerializer):
    # Campo 'location_cpv' que hace referencia a la clave primaria de Localidad
    # Solo incluye objetos de Localidad con status=True
    location_cpv = serializers.PrimaryKeyRelatedField(
        queryset=Localidad.objects.filter(status=True), 
        many=False  # Indica que el campo 'location_cpv' no acepta múltiples instancias
    )
    
    # Clase Meta contiene metadatos para el serializador
    class Meta:
        model = Ubicacion  # El modelo al que está vinculado el serializador
        fields = ('id', 'status', 'its_cpv', 'location_cpv', 'location')  # Campos que se incluirán en la serialización
    
    # Método para validar los atributos antes de guardar una instancia del modelo
    def validate(self, attrs):
        # Si 'its_cpv' es verdadero, se deben seguir reglas específicas
        if attrs['its_cpv']:
            # Si 'location' está presente, se lanza un error
            if 'location' in attrs:
                raise serializers.ValidationError({
                    'error': 'Necesita indicar únicamente la localidad del médico en el CPV.'
                })
            
            # Verifica si ya existe una ubicación con la misma 'location_cpv'
            ubicacion_exists = Ubicacion.objects.filter(
                location_cpv=attrs['location_cpv']
            ).first()
            
            # Si existe, se lanza un error con los datos de la ubicación existente
            if ubicacion_exists:
                ubicacion = UbicacionSerializer(ubicacion_exists)
                raise serializers.ValidationError({
                    "error": "Ya existe una ubicación con la localidad del CPV suministrada.",
                    "data": ubicacion.data
                })
        
        # Si 'its_cpv' es falso y 'location_cpv' está presente, se lanza un error
        if not attrs['its_cpv'] and 'location_cpv' in attrs:
            raise serializers.ValidationError({
                'error': 'Necesita indicar únicamente la localidad del médico.'
            })
        
        # Llama al método validate del padre para continuar con la validación
        return super().validate(attrs)
    
    # Método para personalizar la representación de los datos del modelo Ubicacion
    def to_representation(self, instance:Ubicacion):
        # Llama al método to_representation del padre para obtener el diccionario inicial
        data = super().to_representation(instance)
        
        # Si 'its_cpv' es verdadero, se personaliza la representación de 'location_cpv'
        if data['its_cpv']:
            # Serializa la localidad relacionada y la añade al diccionario 'data'
            location_cpv_serializer = LocalidadSerializer(
                instance.location_cpv  # Obtiene la primera instancia que coincide
            )
            
            # Devuelve un diccionario personalizado para 'its_cpv' verdadero
            return {
                'id': data['id'],
                'status': data['status'],
                'its_cpv': data['its_cpv'],
                'location_cpv': location_cpv_serializer.data
            }
        
        # Devuelve un diccionario personalizado para 'its_cpv' falso
        return {
            'id': data['id'],
            'status': data['status'],
            'its_cpv': data['its_cpv'],
            'location': data['location']
        }