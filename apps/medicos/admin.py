from django.contrib import admin
from .models import *

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
