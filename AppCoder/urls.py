
from django.urls import path
from .views import curso, cursoFormulario,lista_curso,cursos, estudiante, inicio, profesores


urlpatterns = [
    path("agrega/<nombre>/<camada>", curso),
    path("lista-cursos/", lista_curso),
    path("cursos/", cursos, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiantes"),
    path("", inicio, name="Inicio" ),
    path("lista-cursos/", lista_curso),
    path("cursoFormulario/", cursoFormulario, name="cursoFormulario"),
]
