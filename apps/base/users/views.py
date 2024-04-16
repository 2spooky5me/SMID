from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .api.serializers import CustomTokenObtainPairSerializer, UserSerializerLogin
from .models import User

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )
        
        if user:
            login_serializer = self.serializer_class(data=request.data)
            
            if login_serializer.is_valid():
                user_serializer = UserSerializerLogin(user,)
                
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Exitoso'
                }, status=status.HTTP_200_OK)
                
            return Response({
                'error': 'Contraseña o nombre de usuario incorrecto.'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({
                'error': 'Por favor indique las credenciales de usuario.'
            }, status=status.HTTP_400_BAD_REQUEST)
            
class Logout(GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.data.get('username', ''))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({
                'message': 'Sesion cerrada correctamente.'
            }, status=status.HTTP_200_OK)
        return Response({
                'message': 'No existe este usuario.'
            }, status=status.HTTP_400_BAD_REQUEST)