from django.db import models

# Create your models here.




class Residente(models.Model):
    nombre = models.CharField(max_length=100, blank=True, verbose_name="Nombre y Apellido")
    edad = models.IntegerField(blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    telefono = models.PositiveBigIntegerField(blank=True)
    dni = models.PositiveBigIntegerField(blank=True)
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N', 'No especifica'),
    )
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default='N')
   
    def __str__(self):
        return f'Residente: {self.nombre}'   
    
    
    
class Invitado(models.Model):
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE, verbose_name="Nombre del Inquilino", default=None)
    nombre = models.CharField(max_length=20, blank=True, verbose_name="Nombre y Apellido")
    apellido = models.CharField(max_length=50, blank=True)
    telefono = models.PositiveBigIntegerField(blank=True)
    
    def __str__(self):
        return f'{self.nombre}. Invitado de: {self.residente}'
   
    
class Sector(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    codigo = models.PositiveIntegerField(blank=True) 
    
    def __str__(self):
        return f'Sector: "{self.nombre}", cod: "{self.codigo}"'


    
class Staff(models.Model):
        nombre = models.CharField(max_length=100, blank=True)
        sector = models.ForeignKey(Sector, on_delete=models.CASCADE, blank=True)
        telefono = models.PositiveBigIntegerField(blank=True)

        def __str__(self):
            return f'{self.nombre}  --  Telefono: {self.telefono}'

    
    

