from django.db import models

class Pieza(models.Model):
    imagen = models.ImageField(upload_to='piezas/')
    numero = models.IntegerField()

