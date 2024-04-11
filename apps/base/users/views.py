from datetime import datetime

from django.contrib.sessions.models import Session
from .api.serializers import UserSerializerLogin

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

class UserToken(APIView):
    
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user = UserSerializerLogin().Meta.model.objects.filter(username=username).first()
            )
            return Response({
                'token': user_token.key
            })
        except:
            return Response({
                'error': 'Credenciales enviadas incorrectas.'
            }, status=status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context= {'request':request})
        
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            
            if user.is_active:
                token, create = Token.objects.get_or_create(user=user)
                user_serializer = UserSerializerLogin(user)
                #if create:
                return Response({
                    'token': token.key,
                    'usuario': user_serializer.data,
                    'message': 'Inicio de sesion exitoso.'
                }, status=status.HTTP_201_CREATED)
                    
                # else:
                #     """
                #         all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                #         if all_sessions.exists():
                #             for session in all_sessions:
                #                 session_data = session.get_decoded()
                #                 if user.id == int(session_data.get('_auth_user_id')):
                #                     session.delete()
                                    
                #         token.delete()
                #         token, create = Token.objects.get_or_create(user=user)
                #         return Response({
                #             'token': token.key
                #         }, status=status.HTTP_201_CREATED)
                #     """
                #     return Response({
                #         'error': 'Ya se a iniciado sesion con este usuario'
                #     }, status=status.HTTP_409_CONFLICT)
                        
            else:
                return Response(
                    {'error':'Este usuario no puede iniciar sesion.'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
                
        else:
            return Response(
                {'error':'Nombre de usuario o contraseña incorrectos.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
            
class Logout(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            token = request.POST.get('token')
            token = Token.objects.filter(key=token).first()
            
            if token:
                user=token.user
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                            
                token.delete()
                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token Eliminado'
                return Response(
                    {'token_message': token_message, 'session_message': session_message}
                )
            
            return Response(
                {'error':'No se a encontrado un usuario con estas credenciales'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        except:
            return Response(
                {'error':'No se a encontrado token en la peticion.'},
                status=status.HTTP_400_BAD_REQUEST
            )