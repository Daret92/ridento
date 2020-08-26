from django.db import models

# Create your models here.
class Galery(models.Model):
    imagen = models.ImageField(upload_to="galeria")
    texto = models.CharField(max_length=30)
    primera = models.BooleanField(default=False)
    activa = models.BooleanField(default=True)

class Promos(models.Model):
    imagen = models.ImageField(upload_to="promos")
    texto = models.CharField(max_length=30)
    activa = models.BooleanField(default=True)

class Somos(models.Model):
    texto = models.CharField(max_length=1000)
    activa = models.BooleanField(default=False)
    