from django.shortcuts import render,redirect
from .models import Curso
from django.http import HttpResponse
# Create your views here.
def curso(request, nombre, camada):

    curso=Curso(nombre=nombre, camada=camada)
    curso.save()

    return  HttpResponse(f""" 
        <p> curso: {curso.nombre} - camada:{curso.camada} agregado </p>
    """)

def lista_curso(request):
    lista=Curso.objects.all
    return render(request, "lista_curso.html", {"lista_cursos":lista})

def inicio(request):
    return render(request,"inicio.html")

def cursos(request):
    lista=Curso.objects.all
    return render(request,"cursos.html", {"lista_cursos":lista})

def profesores(request):
    return render(request,"profesores.html")

def estudiante(request):
    return render(request,"estudiantes.html")

def cursoFormulario(request):
    #print("method:",request.method)
    #print("post:", request.POST)


    if request.method =="POST":
        curso=Curso(nombre=request.POST["curso"],camada=request.POST["camada"])
        curso.save()
        return redirect("Cursos")
      
    return render(request, "cursoFormulario.html")