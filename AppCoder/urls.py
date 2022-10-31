
from django.urls import path
from .views import curso, cursoFormulario,lista_curso,cursos, estudiante, inicio, profesores


urlpatterns = [
    path("agrega/<nombre>/<camada>", curso),
    path("cursos/", cursos, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiantes"),
    path("", inicio, name="Inicio" ),
    path("cursoFormulario/", cursoFormulario, name="cursoFormulario"),
]
