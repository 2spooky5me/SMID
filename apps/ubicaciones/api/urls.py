from django.urls import path, include
from .views.torre_views import *
from .views.piso_views import *
from .views.localidad_views import *
from .views.ubicacion_views import *

urlpatterns = [
    path('', include('apps.ubicaciones.api.routers'))
]