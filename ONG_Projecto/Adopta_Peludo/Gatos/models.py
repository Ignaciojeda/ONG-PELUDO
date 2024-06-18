from django.db import models

class Sexo(models.Model):
    id_sexo = models.AutoField(db_column='idSexo', primary_key=True)
    sexo = models.CharField(max_length=20, blank=False, null=False)


class Mascota(models.Model):
    id_mascota = models.CharField(primary_key=True, max_length=10)
    nombre_mascota = models.CharField(null=True, max_length=20, )
    fecha_nacimiento = models.DateField(blank=False, null=True)
    raza_mascota = models.CharField(null=True,max_length=20)
    id_sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, db_column='idSexo')

