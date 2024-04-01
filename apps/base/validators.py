from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\d{4}\-?1?\d{7,15}$', 
    message="Formato de numero telefonico: '9999-9999999'."
)