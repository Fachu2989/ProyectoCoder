
from django.urls import path
from .views import buscar, busqueda_camada, curso, cursoFormulario,cursos, estudiante, inicio, profesores


urlpatterns = [
    path("agrega/<nombre>/<camada>", curso),
    path("cursos/", cursos, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiantes"),
    path("", inicio, name="Inicio" ),
    path("cursoFormulario/", cursoFormulario, name="cursoFormulario"),
    path("busqueda_camada/", busqueda_camada, name="busqueda_camada"),
    path("buscar/", buscar, name="buscar"),
]
