from django.db import models
import uuid
# Create your models here.


class Flan(models.Model):
    """Modelo para los productos en venta"""
    flan_uuid = models.UUIDField()
    img_url = models.CharField(max_length=200)
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    slug = models.SlugField(null=True, blank=True)
    is_private = models.BooleanField()

    def __str__(self) -> str:
        if self.is_private == True:
            self.is_private = 'PRIVADO'
        elif self.is_private == False:
            self.is_private = 'NO PRIVADO'
        return f'{self.nombre}: ${self.precio} - ({self.is_private})'
    

class NewsletterForm(models.Model):
    newsletter_email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.newsletter_email}'


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False) # agrega automáticamente un uuid4
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    customer_lastname = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.customer_name} {self.customer_lastname}'