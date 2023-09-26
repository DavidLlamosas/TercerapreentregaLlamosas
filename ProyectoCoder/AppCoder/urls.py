from django.urls import path 
from .views import *

urlpatterns = [
    path("inicio/",ver_inicio, name="Inicio"),
    path("cursos/",ver_cursos, name= "VerCursos"),
    path("entregas/",ver_entregas, name= "VerEntregas"),
    path("estudiantes/",ver_estudiante, name= "VerEstudiantes"),
    path("profesores/",ver_profes, name= "VerProfes"),

    path("creacion/",ver_creacion, name = "VerCreacion"),

    path("creacion/crearcursos/", crear_cursos, name="CrearCursos"),
    path("creacion/crearestudiantes/", crear_estudiantes, name="CrearEstudiantes"),
    path("creacion/crearprofes/", crear_profes, name="CrearProfes"),
    path("creacion/crearentregas/", crear_entregas, name="CrearEntregas"),

    path("profesores/buscar/", buscar_profes, name="BuscarProfesores")
]