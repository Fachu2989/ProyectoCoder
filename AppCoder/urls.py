from msilib.schema import Patch
from django.urls import path
from .views import curso,lista_curso,cursos, estudiante, inicio, profesores


urlpatterns = [
    path("agrega/<nombre>/<camada>", curso),
    path("lista-cursos/", lista_curso),
    path("cursos/", cursos, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiantes"),
    path("", inicio ),
    path("lista-cursos/", lista_curso),
]
