from django.contrib import admin
from .models import Torre, Piso, Localidad, Ubicacion

@admin.register(Torre)
class TorreAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    ordering = ['name']
    
@admin.register(Piso)
class PisoAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    ordering = ['name']

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    search_fields = ('local', 'type_local', 'tower__name', 'floor__name',)
    list_display = ['type_local_local', 'floor', 'tower']
    ordering = ['local']
    autocomplete_fields = ['tower', 'floor']
    
    @admin.display(description="Localidad")
    def type_local_local(self, obj):
        if obj.type_local != 'CO':
            return obj.type_local
        return f'Consultorio {obj.local}'
    
    def tower(self, obj):
        return obj.tower.name
    
    def floor(self, obj):
        return obj.floor.name
    
@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    search_fields = ('its_cpv', 'location', 
                    'location_cpv__tower__name', 'location_cpv__floor__name', 
                    'location_cpv__type_local', 'location_cpv__local',)
    list_display = ['its_cpv', '__str__']
    ordering = ['-its_cpv', 'location', 'location_cpv__tower__name']
    autocomplete_fields = ['location_cpv']
    
    def get_list_display_links(self, request, list_display):
        return ['__str__']
    
    @admin.display(description="¿Es CPV?")
    def its_cpv(self, obj):
        if obj.its_cpv != True:
            return 'No'
        return 'Si'
