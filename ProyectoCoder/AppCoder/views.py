from django.shortcuts import render
#from django.http import HttpResponse
#from .models import Profesor     #Importamos la clase profesor de models aunque tambien podriamos importar todo con *
#COMO VIEWS ESTA DENTRO DE LA CARPETA DE APPCODER Y MODELS TAMBIEN ENTONCES, PODEMOS PONER .models en vez de AppCoder.models
from .models import *

"""
def profe_nuevo(request):
    profeN = Profesor(nombre = "Pepe", apellido="Python", email="pepe@hotmail.com", profesion="Biofísico")   #Siempre colocar por nombre, atributos...
    profeN.save() #En el caso que no se coloquen los nombres aparecera por ID...

    return HttpResponse(f"Hemos guardado al profesor {profeN.nombre}")   #Atributo de profeN, en este caso nombre.

def curso_nuevo(request):
    curso_fav = Curso(nombre= "Python", comision=47765)   #Siempre colocar por nombre, atributos...
    curso_fav.save() #En el caso que no se coloquen los nombres aparecera por ID...

    return HttpResponse(f"Bienvenidos al curso {curso_fav.nombre} comision {curso_fav.comision}") 
"""
#SI EXISTEN 5 DEF BLABLABLA ENTONCES HABRAN 5 URLS
#POR ELLO HAREMOS QUE CADA APLICACION POSEA SUS PROPIAS URLS POR ELLO CREAREMOS UN urls.py
def ver_inicio(request):
    nombre = "David Llamosas Arenas"
    return render(request, "AppCoder/inicio.html", {"name":nombre}) #El tercer argumento es contexto

def ver_cursos(request):
    return render(request , "AppCoder/ver_cursos.html")

def ver_profes(request):
    return render(request, "AppCoder/ver_profes.html")

def ver_entregas(request):
    return render(request , "AppCoder/ver_entregas.html")

def ver_estudiante(request):
    return render(request, "AppCoder/ver_estudiante.html")

def ver_creacion(request):
    return render(request, "AppCoder/ver_creacion.html")

#PARA CREAR LOS FORMULARIOS SE HACEN ACA ABAJO, CREAMOS MAS VISTASa

def crear_cursos(request):

    if request.method == 'POST':
        n_curso = Curso(nombre=request.POST["nombre"], comision=request.POST["comision"])
        n_curso.save()
        return render(request, "AppCoder/inicio.html")
    
    return render(request, "AppCoder/crear_cursos.html")

def crear_profes(request):

    profesion_a_buscar = request.GET.get('profesion', '')

    if request.method == 'POST':
        n_profe = Profesor(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"], profesion=request.POST["profesion"])
        n_profe.save()
        return render(request, "AppCoder/inicio.html")

    profesores = Profesor.objects.filter(profesion__icontains=profesion_a_buscar)

    return render(request, "AppCoder/crear_profes.html", {'profesores': profesores})

def crear_entregas(request):

    if request.method == 'POST':
        n_entregas = Entregable(nombre=request.POST["nombre"], apellido=request.POST["apellido"], curso=request.POST["curso"] ,fechadeentrega=request.POST["fechadeentrega"], entregado=request.POST["entregado"])
        n_entregas.save()
        return render(request, "AppCoder/inicio.html")
    
    return render(request, "AppCoder/crear_entregas.html")

def crear_estudiantes(request): #El request se usara cuando el usuario requiera de una peticion, por ejemplo un clic en el boton guardar.
    
    if request.method == 'POST':
        n_estudiante = Estudiante(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"])
        n_estudiante.save()
        return render(request, "AppCoder/inicio.html")
    
    return render(request, "AppCoder/crear_estudiantes.html")

# PARA LA BUSQUEDA

def buscar_profes(request):
    profesores_b = f"Aqui se muestran los profesores: {request.GET['profesion']}"

    return render(request, "AppCoder/buscar_profes.html",profesores_b)



