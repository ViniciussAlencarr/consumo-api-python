from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class ConsultaCep(models.Model):
    cep = models.CharField(max_length=8)