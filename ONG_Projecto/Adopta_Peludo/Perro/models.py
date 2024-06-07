from django.db import models

# Create your models here.
class perro(models.Model):
    cod_perro=models.IntegerField(primary_key=True);
    nombre_perro=models.CharField(max_length=20);
    edad_perro=models.IntegerField();
    raza_perro=models.CharField(max_length=30);
    esterelizacion=models.BooleanField(True);
    fecha_nac=models.DateField();