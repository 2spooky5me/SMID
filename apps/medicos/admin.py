from django.contrib import admin
from .models import Especialidad, Ubicacion, Medico, MedicoEspecialidad, MedicoUbicacion

# Register your models here.
class EspecialidadAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    ordering = ['name']
    
class MedicoEspecialidadInline(admin.TabularInline):
    model = MedicoEspecialidad
    extra = 1
    autocomplete_fields = ['especialidad']

class MedicoUbicacionInline(admin.TabularInline):
    model = MedicoUbicacion
    extra = 1
    autocomplete_fields = ['ubicacion']
    
class MedicoAdmin(admin.ModelAdmin):
    inlines = [MedicoEspecialidadInline, MedicoUbicacionInline]
    
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    search_fields = ('location', 'location_cpv__tower__name', 'location_cpv__floor__name', 
                    'location_cpv__type_local', 'location_cpv__local',)
    list_display = ['__str__']
    ordering = ['-its_cpv', 'location', 'location_cpv__tower__name']
    autocomplete_fields = ['location_cpv']
    
    def get_list_display_links(self, request, list_display):
        return ['__str__']