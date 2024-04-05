from django.db import models
from django.core.exceptions import ValidationError

from apps.base.models import BaseModel

# Create your models here.
class Torre(BaseModel):
    
    name =                  models.CharField(verbose_name='Nombre', max_length=20, unique=True, )
    
    class Meta: 
        verbose_name = 'torre'
        verbose_name_plural = 'torres'
        
    def clean(self) -> None:
        self.name = self.name.lower().capitalize()
        self.name = self.name[:-1] + self.name[-1].upper()
        return super().clean()
    
    def delete(self, *args, **kwargs):
        # Verifica si hay alguna torre asociada con una localidad para evitar su eliminacion.
        if Localidad.objects.filter(tower=self).exists():
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
        self.name = self.name.lower().capitalize()
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
    type_local =            models.CharField(verbose_name='Tipo Local', max_length=2, choices=LOCAL_TYPES, )
    local =                 models.CharField(max_length=100, )

    class Meta: 
        verbose_name = 'localidad'
        verbose_name_plural = 'localidad'
        unique_together = ['tower', 'floor', 'type_local', 'local']
    
    def clean(self) -> None:
        self.local = self.local.lower().capitalize()
        return super().clean()
    
    def delete(self, *args, **kwargs):
        # Verifica si hay alguna localidad asociada a una ubicacion para evitar su eliminacion.
        if Ubicacion.objects.filter(location_cpv=self).exists():
            raise Exception("No puedes eliminar esta localidad porque está asociado a una ubicacion.")
        super().delete(*args, **kwargs)
        
    def __str__(self) -> str:
        # Esto es temporal, lo quitare cuando dejemos de usar django admin para los registros,
        # luego cuando la aplicacion sea unicamente un microservicio, puedo colocar que cuando
        # se haga un registro a traves del API se coloque de una vez el string "consultorio"
        # en el campo de local.
        if self.type_local == "CO":
            return f'{self.tower}, {self.floor}, {self.LOCAL_TYPES[self.type_local]} {self.local}'
        else:
            return f'{self.tower}, {self.floor}, {self.local}'

class Ubicacion(BaseModel):
    
    its_cpv =               models.BooleanField(verbose_name='¿Es CPV?', )
    location_cpv =          models.OneToOneField(Localidad, verbose_name='Localidad CPV', null=True, blank=True, on_delete=models.RESTRICT, unique=True)
    location =              models.TextField(verbose_name='Direccion', null=True, blank=True, )

    def clean(self) -> None:
        
        self.location = self.location.upper()
        
        if self.its_cpv and self.location:
            raise ValidationError(
                "Si '¿Es CPV?' esta marcado, no debes proporcionar un valor para 'Direccion'."
            )
        
        elif self.its_cpv == False and self.location_cpv: 
            raise ValidationError(
                "Si '¿Es CPV?' NO esta marcado, no debes proporcionar un valor para 'Localidad CPV'."
            )
        
        return super(Ubicacion, self).clean()
        
    def __str__(self) -> str:
        
        if self.its_cpv:
            return str(self.location_cpv)
        
        return self.location
    
    class Meta:
        
        verbose_name='ubicacion'
        verbose_name_plural='ubicaciones'