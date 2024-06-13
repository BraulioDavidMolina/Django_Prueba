from django.db import models

# Create your models here.
class Alumno(models.Model):
    matricula = models.CharField(max_length=12)
    nombre = models.TextField()
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)