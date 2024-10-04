from django.db import models

# Create your models here.
class PostSalida(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=500)
    cantidad = models.CharField(max_length=100)
    fecha_salida = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self