from django.db import models

from apps.base.models import BaseModel
from apps.medicos import models as medicos_models

# Create your models here.
class Torre(BaseModel):
    
    name =                  models.CharField(verbose_name='Nombre', max_length=20, unique=True, )
    
    class Meta: 
        verbose_name = 'torre'
        verbose_name_plural = 'torres'
        
    def clean(self) -> None:
        self.name = self.name.title()
        return super().clean()
    
    def delete(self, *args, **kwargs):
        # Verifica si hay alguna torre asociada con una localidad para evitar su eliminacion.
        localition = Localidad.objects.filter(tower=self)
        if localition.exists():
            raise Exception("No puedes eliminar esta torre porque está asociada a una localidad.")
        super().delete(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.name
    
class Piso(BaseModel):
    
    name =                  models.CharField(verbose_name='Nombre', max_length=20, unique=True, )
        
    class Meta: 
        verbose_name = 'piso'
        verbose_name_plural = 'pisos'
        
    def clean(self) -> None:
        self.name = self.name.title()
        return super().clean()
    
    def delete(self, *args, **kwargs):
        # Verifica si hay algun piso asociada con una localidad para evitar su eliminacion.
        if Localidad.objects.filter(floor=self).exists():
            raise Exception("No puedes eliminar este piso porque está asociado a una localidad.")
        super().delete(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.name

class Localidad(BaseModel):
    
    LOCAL_TYPES = {
        "CO": "Consultorio",
        "OT": "Otro"
    }
    
    tower =                 models.ForeignKey(Torre, verbose_name='Torre', on_delete=models.RESTRICT, )
    floor =                 models.ForeignKey(Piso, verbose_name='Piso', on_delete=models.RESTRICT, )
    type_local =            models.CharField(verbose_name='Tipo Local', max_length=2, choices=LOCAL_TYPES, null=True, blank=True, )
    local =                 models.CharField(max_length=100, null=True, blank=True, )

    class Meta: 
        verbose_name = 'localidad'
        verbose_name_plural = 'localidades'
        unique_together = ['tower', 'floor', 'type_local', 'local']
    
    def clean(self) -> None:
        if self.local:
            self.local = self.local.title()
        return super().clean()
    
    def delete(self, *args, **kwargs):
        # Verifica si hay alguna localidad asociada a una ubicacion para evitar su eliminacion.
        if medicos_models.Ubicacion.objects.filter(location_cpv=self).exists():
            raise Exception("No puedes eliminar esta localidad porque está asociado a una ubicacion.")
        super().delete(*args, **kwargs)
        
    def __str__(self) -> str:
        # Esto es temporal, lo quitare cuando dejemos de usar django admin para los registros,
        # luego cuando la aplicacion sea unicamente un microservicio, puedo colocar que cuando
        # se haga un registro a traves del API se coloque de una vez el string "consultorio"
        # en el campo de local.
        if self.type_local == "CO":
            message = f'{self.tower}, {self.floor}, {self.LOCAL_TYPES[self.type_local]} {self.local}' if self.type_local else f'{self.tower}, {self.floor}'
        else:
            message = f'{self.tower}, {self.floor}, {self.local}' if self.local else f'{self.tower}, {self.floor}'
        return message