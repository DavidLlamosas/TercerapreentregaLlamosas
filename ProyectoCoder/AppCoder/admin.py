from django.contrib import admin
from .models import *

# Registramos los modelos importandolos desde models

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Entregable)