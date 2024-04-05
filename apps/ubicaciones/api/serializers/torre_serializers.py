from rest_framework import serializers
from ...models import Torre

class TorreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torre
        fields = ('id', 'status', 'name')