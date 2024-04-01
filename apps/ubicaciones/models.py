from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.
class Torre(BaseModel):
    
    name =                  models.CharField(verbose_name='Nombre', max_length=20, unique=True)

    historical =            HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
        
    class Meta: 
        verbose_name = 'torre'
        verbose_name_plural = 'torres'
        
    def __str__(self) -> str:
        return self.name
    
class Piso(BaseModel):
    
    name =                  models.CharField(verbose_name='Nombre', max_length=20, unique=True)
    
    historical =            HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
        
    class Meta: 
        verbose_name = 'piso'
        verbose_name_plural = 'pisos'
        
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
    local =                 models.CharField(max_length=100)
    
    historical =            HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
        
    class Meta: 
        verbose_name = 'localidad'
        verbose_name_plural = 'localidad'
        
    def __str__(self) -> str:
        if self.type_local == "CO":
            return f'{self.tower}, {self.floor}, {self.LOCAL_TYPES[self.type_local]} {self.local}'
        else:
            return f'{self.tower}, {self.floor}, {self.local}'

class Ubicacion(BaseModel):
    
    its_cpv =               models.BooleanField(verbose_name='¿Es CPV?', )
    location_cpv =          models.ForeignKey(Localidad, verbose_name='Localidad CPV', null=True, blank=True, on_delete=models.RESTRICT, )
    location =              models.TextField(verbose_name='Direccion', null=True, blank=True, )

    historical =            HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
    
    def clean(self) -> None:
        
        if self.location:
            self.location = self.location.upper()
            
        return super(Ubicacion, self).clean()
    
    def __str__(self) -> str:
        
        if self.location_cpv:
            return str(self.location_cpv)
        
        if self.location:
            return self.location
    
    class Meta:
        
        verbose_name='ubicacion'
        verbose_name_plural='ubicaciones'
    