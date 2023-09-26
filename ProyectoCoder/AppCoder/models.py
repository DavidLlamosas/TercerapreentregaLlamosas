from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()

class Estudiante(models.Model):
    #def __init__(self): #Ya no necesitas realizar un __init__ pero debemos heredar 
    #    pass
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()         #Solo puede recibir emails.
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    curso = models.CharField(max_length=30)
    fechadeentrega = models.DateField() #Fecha para saber cuando fue 
    entregado = models.BooleanField()   #Bolean para saber si si o no.


















