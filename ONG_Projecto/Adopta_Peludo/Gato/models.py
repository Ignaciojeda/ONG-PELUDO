from django.db import models

# Create your models here.
class Gato(models.Model):
    cod_gato=models.IntegerField(primary_key=True);
    nombre_gato=models.CharField(max_length=20);
    edad_gato=models.IntegerField();
    raza_gato=models.CharField(max_length=30);
    esterelizacion=models.BooleanField(blank=True, null=True);
    fecha_nac=models.DateField();
    
    def __str__(self):
        return "Nombre: "+str(self.nombre_gato)

