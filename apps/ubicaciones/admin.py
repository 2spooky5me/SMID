from django.contrib import admin
from .models import Torre, Piso, Localidad

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
        if obj.local:
            if obj.type_local != 'CO':
                return obj.type_local
            return f'Consultorio {obj.local}'
        return 'No Especificada.'
    
    def tower(self, obj):
        return obj.tower.name
    
    def floor(self, obj):
        return obj.floor.name
