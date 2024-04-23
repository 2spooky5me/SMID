from django.db import models
from apps.base.validators import phone_regex
from apps.base.models import BaseModel, PersonMixin, sex_choice, nature_identification_choice, nature_rif_choice
from django.core.exceptions import ValidationError
from apps.ubicaciones import models as ubicaciones_models

class Especialidad(BaseModel):
    
    name =                  models.CharField(verbose_name='Nombre', max_length=30, unique=True, )
    description =           models.TextField(verbose_name='Descripcion', null=True, blank=True, )

    def clean(self) -> None:
        self.name = self.name.title()
        return super().clean()
    
    def delete(self, *args, **kwargs):
        # Verifica si hay la especialidad esta asociada con un medico para evitar su eliminacion.
        if Medico.objects.filter(specialty=self).exists():
            raise Exception("No puedes eliminar esta especialidad porque está asociada a un medico.")
        super().delete(*args, **kwargs)
    
    class Meta:
        
        verbose_name='especialidad'
        verbose_name_plural='especialidades'
    
    def __str__(self) -> str:
        
        return self.name

class Ubicacion(BaseModel):
    
    its_cpv =               models.BooleanField(verbose_name='¿La ubicacion es CPV?', null=False, blank=False, )
    location_cpv =          models.OneToOneField(ubicaciones_models.Localidad, verbose_name='Localidad CPV', null=True, blank=True, on_delete=models.RESTRICT, )
    location =              models.TextField(verbose_name='Direccion', null=True, blank=True, )

    def clean(self) -> None:
        
        self.location = self.location.title()
        
        if self.its_cpv:
            if not self.location_cpv:
                raise ValidationError("Si la ubicación es CPV, debes proporcionar un valor para 'Localidad CPV'.")
            if self.location:
                raise ValidationError("Si la ubicación es CPV, NO debes proporcionar un valor para 'Dirección'.")
        else:
            if self.location_cpv:
                raise ValidationError("Si la ubicación NO es CPV, NO debes proporcionar un valor para 'Localidad CPV'.")
            if not self.location:
                raise ValidationError("Si la ubicación NO es CPV, debes proporcionar un valor para 'Dirección'.")

        
        return super(Ubicacion, self).clean()
        
    def __str__(self) -> str:
        
        if self.its_cpv:
            return f'{str(self.location_cpv)} (CPV)'
        
        return self.location
    
    class Meta:
        
        verbose_name='ubicacion'
        verbose_name_plural='ubicaciones'
        
class Medico(PersonMixin, BaseModel):
    
    code =                  models.CharField(verbose_name='Codigo', max_length=5, )
    identification =        models.CharField(verbose_name='Cédula de identidad', max_length=9, unique=True, )
    identification_nature = models.CharField(verbose_name='Naturaleza de la cedula', max_length=1, choices=nature_identification_choice, default='V', )
    rif =                   models.CharField(verbose_name='RIF', max_length=10, unique=True, )
    identification_rif =    models.CharField(verbose_name='Naturaleza del rif', max_length=1, choices=nature_rif_choice, default='V', )
    sex =                   models.CharField(verbose_name='Sexo',max_length=1, choices=sex_choice, default='M', )
    first_name =            models.CharField(verbose_name='Primer nombre', max_length=20, )
    second_name =           models.CharField(verbose_name='Segundo nombre', max_length=20, null=True, blank=True, )
    last_name =             models.CharField(verbose_name='Primer apellido', max_length=20, )
    second_last_name =      models.CharField(verbose_name='Segundo apellido', max_length=20, null=True, blank=True, )
    phone =                 models.CharField(verbose_name='Numero telefonico', validators=[phone_regex], max_length=17, null=True, blank=True, )
    photo =                 models.ImageField(verbose_name='Foto', upload_to='medicos', blank=True, )
    specialty =             models.ManyToManyField(Especialidad, verbose_name='Especialidad', through='MedicoEspecialidad', )
    location =              models.ManyToManyField(Ubicacion, verbose_name='Ubicacion', through='MedicoUbicacion', )
    
    def clean(self) -> None:
        self.first_name = self.first_name.upper()
        self.second_name = '' if not self.second_name else self.second_name.upper()
        self.last_name = self.last_name.upper()
        self.second_last_name = '' if not self.second_last_name else self.second_last_name.upper()
        return super(Medico, self).clean()
    
    class Meta:
        
        verbose_name='medico'
        verbose_name_plural='medicos'
    
class MedicoUbicacion(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.RESTRICT, blank=True, null=True, )
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.RESTRICT, blank=True, null=True, )
    
    class Meta:
        
        verbose_name='ubicacion del medico'
        verbose_name_plural='ubicaciones del medico'
    
    def __str__(self):
        return str(self.ubicacion)
        
class MedicoEspecialidad(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.RESTRICT, blank=True, null=True, )
    especialidad = models.ForeignKey(Especialidad, on_delete=models.RESTRICT, blank=True, null=True, )
    
    class Meta:
        
        verbose_name='especialidad del medico'
        verbose_name_plural='especialidades del medico'
    
    def __str__(self):
        return str(self.especialidad)