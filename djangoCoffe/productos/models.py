from django.db import models

class Product(models.Model):
    name = models.TextField(max_length=100, verbose_name='nombre')
    description = models.TextField(max_length=150,verbose_name='descripción')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='precio')
    available = models.BooleanField(default=True, verbose_name='disponible')
    photo = models.ImageField(upload_to='productos', null=True, blank=True, verbose_name='foto')

    def __str__(self):
        return self.name
# Create your models here.
