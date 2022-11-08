from django.shortcuts import render,redirect
from .form import CursoFormulario,ProfesorFormulario
from .models import Curso,Profesor, Estudiante
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
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



#CRUD Profesores
def listaProfesores(request):
    profesores=Profesor.objects.all()
    return render(request, "leerprofesores.html", {"profesores":profesores})

def crea_profesor(request):
    if request.method =="POST":
        mi_formulario= ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            profesor=Profesor(nombre=data["nombre"],apellido=data["apellido"],email=data["email"],profesion=data["profesion"])
            profesor.save()
            return redirect("listaProfesores")
    else: 
        mi_formulario=ProfesorFormulario()
     
    return render(request, "profesorFormulario.html",{'mi_formulario': mi_formulario})

def eliminaProfesor(request,id):
    if request.method =="POST":
        profesor=Profesor.objects.get(id=id)
        profesor.delete()
        profesores=Profesor.objects.all()
        return render(request, "leerprofesores.html", {"profesores":profesores})
        
def editar_profesor(request, id):

    profesor = Profesor.objects.get(id=id)

    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            profesor.nombre = data["nombre"]
            profesor.apellido = data["apellido"]
            profesor.email = data["email"]
            profesor.profesion = data["profesion"]

            profesor.save()

            return redirect('listaProfesores')
    
    else:

        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "apellido": profesor.apellido,
            "email": profesor.email,
            "profesion": profesor.profesion,
        })

    return render(request, "editarProfesor.html", {"miFormulario": miFormulario, "id": profesor.id})




#CRUD vista basada en clase (curso)
class CursoList(ListView):

    model = Curso
    template_name = 'curso_list.html'
    context_object_name = "cursos"

class CursoDetail(DetailView):

    model = Curso
    template_name = 'curso_detail.html'
    context_object_name = "curso"

class CursoCreate(CreateView):

    model = Curso
    template_name = 'curso_create.html'
    fields = ["nombre", "camada"]
    success_url = '/app-coder/'

class CursoUpdate(UpdateView):

    model = Curso
    template_name = 'curso_update.html'
    fields = ('__all__')
    success_url = '/app-coder/'

class CursoDelete(DeleteView):

    model = Curso
    template_name = 'curso_delete.html'
    success_url = '/app-coder/'
 
