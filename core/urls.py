"""
URL configuration for SMID project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.authentication import BasicAuthentication
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg import openapi
import copy

from apps.base.users.views import Login, Logout, UserToken

# Esquema para la documentación de las API
class CustomSchemaGenerator(OpenAPISchemaGenerator):
    metodos = {
        'list': 'Listado',
        'destroy': 'Eliminar',
        'create': 'Crear',
        'update': 'Actualización completa',
        'partial_update': 'Actualización parcial',
        'retrieve': 'Obtención'
    }
    def get_overrides(self, view, method):
        
        """Get overrides specified for a given operation.

        :param view: the view associated with the operation
        :param str method: HTTP method
        :return: a dictionary containing any overrides set by :func:`@swagger_auto_schema <.swagger_auto_schema>`
        :rtype: dict
        """
        method = method.lower()
        action = getattr(view, 'action', method)
        action_method = getattr(view, action, None)
        overrides = getattr(action_method, '_swagger_auto_schema', {})
        if method in overrides:
            overrides = overrides[method]
        
        if not 'operation_summary' in overrides and (desc:=self.metodos.get(action)):
            desc = f'{desc} {view.get_serializer_class().Meta.model.__name__}'
            overrides['operation_summary'] = desc
        #import pdb;pdb.set_trace()

        return copy.deepcopy(overrides)



schema_view = get_schema_view(
    openapi.Info(
        title="Sinteg API",
        default_version='v0.1.030523',
        description="""
        Manual de documentación para el correcto uso de las API generadas por el servidor
        de Sinteg, Sistema de salud integral.
        
        A continuación se muestran los diferentes URL de las API con sus respectivos
        métodos que son capaces de aceptar, cabe destacar que todos están 
        protegidos por lo que es necesario iniciar sesión en un usuario con los
        permisos adecuados para hacer uso de estas API.
        """,
        terms_of_service=None,
        contact=openapi.Contact(email="programador3@cpv.com.ve", name="Leandro Fermín"),
    ),
    public=True,
    generator_class=CustomSchemaGenerator,
    permission_classes=[permissions.IsAdminUser,],
    authentication_classes=[BasicAuthentication,],
)

urlpatterns = [
    # Login y Logout
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    
    #Django admin y Token
    path('admin/', admin.site.urls),
    path('refresh-token/', UserToken.as_view(), name='refresh_token'),
    
    # Rutas para las API Viewset de las Apps
    path('medicos/', include('apps.medicos.api.routers'), name="medicos"),
    path('ubicaciones/', include('apps.ubicaciones.api.routers'), name="ubicaciones"),
    
    # Documentacion y Debug
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("__debug__/", include("debug_toolbar.urls")),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)