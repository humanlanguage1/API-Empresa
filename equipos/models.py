from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=200, default='')
    email = models.EmailField()
    area = models.CharField(max_length=100, default='')
    cargo = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nombre + ' ' + self.cargo

class Equipo(models.Model):
    empleado = models.ForeignKey(Empleado,on_delete=models.RESTRICT)
    tipo = models.CharField(max_length=100, default='')
    marca = models.CharField(max_length=100, default='')
    modelo = models.CharField(max_length=100, default='')
    procesador = models.CharField(max_length=100,default='')
    serie = models.CharField(max_length=100,default='')
    memoria = models.CharField(max_length=100,default='')
    disco = models.CharField(max_length=100,default='')
    
    def __str__(self):
         return self.marca + ' - ' + self.modelo + ' - ' + self.serie    