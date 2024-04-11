from ..models import User
from rest_framework import serializers

class UserSerializerLogin(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 
            'last_name',  'is_superuser', 'is_staff'
            )
        
    def to_representation(self, instance):
        """
        Funcion para la representacion de los datos de usuario al iniciar sesion
        
        args:
            instance(User) => Instancia del usuario
        returns:
            representation(OrderedDict): Devuelve un diccionario con el siguiente esquema
            {
                username: "username",
                email: "email@cpv.com.ve",
                is_superuser: True | False,
                user_permissions: ['string' ...]
                first_name: "name",
                last_name:"name",
            }
        """
        representation =  super().to_representation(instance)
        representation['user_permissions'] = instance.get_all_permissions()
        
        return representation