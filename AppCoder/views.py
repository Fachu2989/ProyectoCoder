from django.shortcuts import render,redirect

from .form import CursoFormulario
from .models import Curso
from django.http import HttpResponse
# Create your views here.
def curso(request, nombre, camada):

    curso=Curso(nombre=nombre, camada=camada)
    curso.save()

    return  HttpResponse(f""" 
        <p> curso: {curso.nombre} - camada:{curso.camada} agregado </p>
    """)




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

    if request.method =="POST":
        mi_formulario= CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            curso=Curso(nombre=data["curso"],camada=data["camada"])
            curso.save()
            return redirect("Cursos")
    else: 
        mi_formulario=CursoFormulario()
     
    return render(request, "cursoFormulario.html",{'mi_formulario': mi_formulario})

def busqueda_camada(request):
    return render(request, 'busqueda_camada.html')

def buscar(request):
    camada_buscada= request.GET['camada']
    curso= Curso.objects.get(camada=camada_buscada)
    return render(request,'resultado_busqueda.html',{"curso":curso, "camada": camada_buscada})