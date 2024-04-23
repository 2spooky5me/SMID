from rest_framework import serializers

from ...models import Medico, Especialidad, Ubicacion
from .especialidad_serializers import EspecialidadSerializer
from apps.medicos.api.serializers.ubicacion_serializers import UbicacionSerializer

# Serializador para el modelo Medico
class MedicoSerializer(serializers.ModelSerializer):
    # Campo 'specialty' que hace referencia a las claves primarias de Especialidad
    # Incluye múltiples instancias de Especialidad con status=True
    specialty = serializers.PrimaryKeyRelatedField(
        queryset=Especialidad.objects.filter(status=True), 
        many=True  # Permite múltiples especialidades para un médico
    )
    # Campo 'location' que hace referencia a las claves primarias de Ubicacion
    # Incluye múltiples instancias de Ubicacion con status=True
    location = serializers.PrimaryKeyRelatedField(
        queryset=Ubicacion.objects.filter(status=True), 
        many=True  # Permite múltiples ubicaciones para un médico
    )
    
    # Clase Meta contiene metadatos para el serializador
    class Meta:
        model = Medico  # El modelo al que está vinculado el serializador
        fields = (
            'status', 'id', 'code',
            'identification', 'identification_nature',
            'rif', 'rif_nature',
            'sex', 'first_name',
            'second_name', 'last_name',
            'second_last_name', 'phone',
            'photo', 'specialties', 'location'
        )  # Campos que se incluirán en la serialización
    
    # Método para personalizar la representación de los datos del modelo Medico
    def to_representation(self, instance):
        # Llama al método to_representation del padre para obtener el diccionario inicial
        data = super().to_representation(instance)
        
        # Obtén todos los objetos de especialidad y ubicación con status=True
        all_specialties = Especialidad.objects.filter(status=True)
        all_locations = Ubicacion.objects.filter(status=True)
        
        # Crea un diccionario para mapear identificadores a datos de especialidad y ubicación
        specialty_dict = {specialty.id: EspecialidadSerializer(specialty).data for specialty in all_specialties}
        location_dict = {location.id: UbicacionSerializer(location).data for location in all_locations}
        
        # Reemplaza los identificadores en 'data' con los datos correspondientes de especialidad y ubicación
        data['specialty'] = [specialty_dict.get(pk) for pk in data['specialty']]
        data['location'] = [location_dict.get(pk) for pk in data['location']]
        
        data['full_name'] = f'{data["last_name"]} {data["second_last_name"]}, {data["first_name"]} {data["second_name"]}'
        
        return data  # Devuelve el diccionario 'data' actualizado