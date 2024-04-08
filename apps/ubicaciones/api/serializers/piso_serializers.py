from rest_framework import serializers
from ...models import Piso

class PisoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Piso
        fields = ('id', 'status', 'name')