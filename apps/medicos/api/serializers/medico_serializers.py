from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ...models import Medico, Especialidad, Ubicacion
from .especialidad_serializers import EspecialidadSerializer
from apps.ubicaciones.api.serializers.ubicacion_serializers import UbicacionSerializer

class MedicoSerializer(serializers.ModelSerializer):
    specialty = serializers.PrimaryKeyRelatedField(queryset=Especialidad.objects.filter(status=True), many=True)
    location = serializers.PrimaryKeyRelatedField(queryset=Ubicacion.objects.filter(status=True), many=True)
    
    class Meta:
        model = Medico
        fields = (
            'status', 'id', 'code',
            'identification', 'identification_nature',
            'rif', 'identification_rif',
            'sex', 'first_name',
            'second_name', 'last_name',
            'second_last_name', 'phone',
            'photo','specialty', 'location'
        )
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # Obtén todos los objetos de especialidad y ubicación
        all_specialties = Especialidad.objects.filter(status=True)
        all_locations = Ubicacion.objects.filter(status=True)
        
        # Crea un diccionario para mapear identificadores a datos de especialidad y ubicación
        specialty_dict = {specialty.id: EspecialidadSerializer(specialty).data for specialty in all_specialties}
        location_dict = {location.id: UbicacionSerializer(location).data for location in all_locations}
        
        # Reemplaza los identificadores con los datos correspondientes
        data['specialty'] = [specialty_dict.get(pk) for pk in data['specialty']]
        data['location'] = [location_dict.get(pk) for pk in data['location']]
        return data