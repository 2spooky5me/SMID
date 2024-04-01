from django.urls import path
from .views.torre_views import *
from .views.piso_views import *
from .views.localidad_views import *
from .views.ubicacion_views import *

urlpatterns = [
    path('torre/list/', 
        TorresListAPIView.as_view(), 
        name='torres_list_all_view'),
    
    path('torre/list/<int:pk>', 
        TorresListAPIView.as_view(), 
        name='torres_list_id_view'),
    
    path('torre/create/', 
        TorresCreateAPIView.as_view(), 
        name='torres_create_view'),
    
    path('torre/RUD/<int:pk>', 
        TorresRetrieveUpdateDestroyAPIView.as_view(), 
        name='torres_RUD_view'),
    
    path('piso/list/', 
        PisoListAPIView.as_view(), 
        name='piso_list_all_view'),
    
    path('piso/list/<int:pk>', 
        PisoListAPIView.as_view(), 
        name='piso_list_id_view'),
    
    path('piso/create/', 
        PisoCreateAPIView.as_view(), 
        name='piso_create_view'),
    
    path('piso/RUD/<int:pk>', 
        PisoRetrieveUpdateDestroyAPIView.as_view(), 
        name='piso_RUD_view'),
    
    path('localidad/list/', 
        LocalidadListAPIView.as_view(), 
        name='localidad_list_all_view'),
    
    path('localidad/list/<int:pk>', 
        LocalidadListAPIView.as_view(), 
        name='localidad_list_id_view'),
    
    path('localidad/create/', 
        LocalidadCreateAPIView.as_view(), 
        name='localidad_create_view'),
    
    path('localidad/RUD/<int:pk>', 
        LocalidadRetrieveUpdateDestroyAPIView.as_view(), 
        name='localidad_RUD_view'),
    
    path('ubicacion/list/', 
        UbicacionListAPIView.as_view(), 
        name='ubicaciones_list_all_view'),
    
    path('ubicacion/list/<int:pk>', 
        UbicacionListAPIView.as_view(), 
        name='ubicaciones_list_id_view'),
    
    path('ubicacion/create/', 
        UbicacionCreateAPIView.as_view(), 
        name='ubicaciones_create_view'),
    
    path('ubicacion/RUD/<int:pk>', 
        UbicacionRetrieveUpdateDestroyAPIView.as_view(), 
        name='ubicaciones_RUD_view')
]