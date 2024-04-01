from datetime import datetime as dt
from django.db import models
from django.core.cache import cache

# Create your models here.
sex_choice = (
    ('M', 'MASCULINO'),
    ('F', 'FEMENINO'),
)
nature_identification_choice = (
    ('V', 'VENEZOLANO'),
    ('E', 'EXTRANJERO'),
)
nature_rif_choice = (
    ('V', 'VENEZOLANO'),
    ('E', 'EXTRANJERO'),
    ('J', 'JURIDICO'),
    ('P', 'PASAPORTE'),
    ('G', 'GOBIERNO')
)


class PersonMixin:
    
    def __str__(self) -> str:
        return f'{self.last_name} {self.second_last_name or ""}, {self.first_name} {self.second_name or ""}'


class BaseModel(models.Model):
    """Modelo Base que heredarán los demás
    """
    
    status =                models.BooleanField(default=True, verbose_name= 'Estado', help_text="Activo✅ / Inactivo ❌")
    created_date =          models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Fecha de creación')
    modified_date =         models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Fecha de modificación')
    deleted_date =          models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Fecha de Eliminación')
    changed_by =            models.ForeignKey('auth.User', on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Cambiado por (Usuario)", help_text="El último usuario en alterar el registro")
    
    #TODO Configuración de la auditoría 
    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        cache.clear() #? Limpia todo el cache
    
    def delete(self, *args, **kwargs) -> tuple[int, dict[str, int]]:
        self.status = False
        self.deleted_date = dt.now(tz=None)
        self.save()
    
    class Meta: 
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'