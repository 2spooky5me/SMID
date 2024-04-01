from rest_framework import serializers
from ...models import Medico, Especialidad, Ubicacion
from .especialidad_serializers import EspecialidadSerializer
from apps.ubicaciones.api.serializers.ubicacion_serializers import UbicacionSerializer

class MedicoReadOnlySerializer(serializers.ModelSerializer):
    specialty = EspecialidadSerializer(many=True)
    location = UbicacionSerializer(many=True)
    
    class Meta:
        model = Medico
        fields = (
                'id','code',
                'identification','identification_nature',
                'rif','identification_rif',
                'sex','first_name',
                'second_name','last_name',
                'second_last_name','phone',
                'photo','specialty',
                'location'
                )

class MedicoSerializer(MedicoReadOnlySerializer):
    specialty = serializers.PrimaryKeyRelatedField(queryset=Especialidad.objects.all(), many=True)
    location = serializers.PrimaryKeyRelatedField(queryset=Ubicacion.objects.all(), many=True)