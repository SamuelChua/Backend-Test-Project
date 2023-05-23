from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class ProjectPair(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField( verbose_name='email', max_length=255, unique=True)
