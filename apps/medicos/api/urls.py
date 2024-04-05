from django.urls import path, include
from .views.especialidad_views import *
from .views.medico_views import *

urlpatterns = [
    path('', include('apps.medicos.api.routers'))
]