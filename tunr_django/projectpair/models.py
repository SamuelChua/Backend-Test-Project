from django.db import models
from django.conf import settings
# Create your models here.

class ProjectPair(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, default = "enter your occupation")
    