from rest_framework import serializers

from ...models import Medico, Especialidad, Ubicacion
from .especialidad_serializers import EspecialidadSerializer
from apps.medicos.api.serializers.ubicacion_serializers import UbicacionSerializer

# Serializador para el modelo Medico
class MedicoSerializer(serializers.ModelSerializer):
    # Campo 'specialty' que hace referencia a las claves primarias de Especialidad
    # Incluye múltiples instancias de Especialidad con status=True
    specialties = serializers.PrimaryKeyRelatedField(
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
            'photo', 'specialties', 'location',
            "is_actionist", "n_actions"
        )  # Campos que se incluirán en la serialización
    
    # Método para personalizar la representación de los datos del modelo Medico
    def to_representation(self, instance:Medico):
        # Llama al método to_representation del padre para obtener el diccionario inicial
        data = super().to_representation(instance)
        
        data['specialties'] = EspecialidadSerializer(instance.specialties, many=True).data
        data['location'] = UbicacionSerializer(instance.location, many=True).data
        data['full_name'] = f'{data["last_name"]} {data["second_last_name"]}, {data["first_name"]} {data["second_name"]}'
        
        return data  # Devuelve el diccionario 'data' actualizado