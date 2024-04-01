from django.urls import path
from .views.especialidad_views import *
from .views.medico_views import *

urlpatterns = [
    path('especialidad/list/', 
        EspecialidadListAPIView.as_view(), 
        name='especialidad_list_all_view'),
    
    path('especialidad/list/<int:pk>', 
        EspecialidadListAPIView.as_view(), 
        name='especialidad_list_id_view'),
    
    path('especialidad/create/', 
        EspecialidadCreateAPIView.as_view(), 
        name='especialidad_create_view'),
    
    path('especialidad/RUD/<int:pk>', 
        EspecialidadRetrieveUpdateDestroyAPIView.as_view(), 
        name='especialidad_RUD_view'),
    
    path('medico/list/', 
        MedicoListAPIView.as_view(), 
        name='medico_list_all_view'),
    
    path('medico/list/<int:pk>', 
        MedicoListAPIView.as_view(), 
        name='medico_list_id_view'),
    
    path('medico/create/', 
        MedicoCreateAPIView.as_view(), 
        name='medico_create_view'),
    
    path('medico/RUD/<int:pk>', 
        MedicoRetrieveUpdateDestroyAPIView.as_view(), 
        name='medico_RUD_view')
]