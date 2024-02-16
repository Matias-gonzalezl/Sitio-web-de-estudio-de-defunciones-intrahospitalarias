from django.db import models

# Create your models here.


class Region(models.Model):
    id_region = models.AutoField(db_column='id_region', primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)


class Hospital(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    direccion = models.CharField(max_length=60, blank=False, null=False)
    id_region = models.ForeignKey(
        'Region', on_delete=models.CASCADE, db_column='id_region')

    def __str__(self):
        return str(self.nombre)


class Paciente(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    run = models.IntegerField()
    ape_pat = models.CharField(max_length=30, blank=False, null=False)
    ape_mat = models.CharField(max_length=30, blank=False, null=False)
    fecha_def = models.DateField(blank=False, null=False)
    id_region = models.ForeignKey(
        'Region', on_delete=models.CASCADE, db_column='id_region')
    id_hospital = models.ForeignKey(
        'Hospital', on_delete=models.CASCADE, db_column='id_hospital')

    def __str__(self):
        return str(self.nombre)+" "+str(self.ape_pat)+" "+str(self.ape_mat)

class Estudio(models.Model):
    id_estudio = models.AutoField(db_column='id_estudio', primary_key=True)
    titulo = models.CharField(max_length=60, blank=False, null=False)
    cuerpo = models.CharField(max_length=5000, blank=False, null=False)
    conclusion = models.CharField(max_length=1000, blank=False, null=False)
    
    def __str__(self):
        return str(self.titulo)
