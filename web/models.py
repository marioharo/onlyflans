from django.db import models

# Create your models here.


class Flan(models.Model):
    img_url = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return self.title