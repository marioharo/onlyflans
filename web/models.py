from django.db import models

# Create your models here.


class Flan(models.Model):
    img_url = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()