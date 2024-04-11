from django.db import models
from django.contrib.auth.models import User
from simple_history import register

# Create your models here.

register(User, 'django.contrib.auth')