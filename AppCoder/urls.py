
from django.urls import path
from .views import editar_perfil,registro, loginView, CursoList,CursoCreate,CursoUpdate,CursoDelete,CursoDetail, buscar,editar_profesor,eliminaProfesor,crea_profesor, busqueda_camada, curso, cursoFormulario,cursos, estudiante, inicio, profesores,listaProfesores
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("agrega/<nombre>/<camada>", curso),
    path("cursos/", cursos, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiantes"),
    path("", inicio, name="Inicio" ),
    path("cursoFormulario/", cursoFormulario, name="cursoFormulario"),
    path("busqueda_camada/", busqueda_camada, name="busqueda_camada"),
    path("buscar/", buscar, name="buscar"),
    
    #CRUD Profesores 
    path("listaprofesores/", listaProfesores, name="listaProfesores"),
    path("crea_profesores/", crea_profesor, name="crea_profesor"),
    path("eliminaprofesor/<int:id>", eliminaProfesor, name="eliminaprofesor"),
    path('editar-profesor/<int:id>', editar_profesor, name="EditarProfesor"),

    #CRUD Curso
    path('listaCursos', CursoList.as_view(), name="ListaCursos"),
    path('detalleCurso/<pk>', CursoDetail.as_view(), name="DetalleCurso"),
    path('creaCurso/', CursoCreate.as_view(), name="CreaCurso"),
    path('actualizarCurso/<pk>', CursoUpdate.as_view(), name="ActualizaCursos"),
    path('eliminarCurso/<pk>', CursoDelete.as_view(), name="EliminaCursos"),

    #login
    path('login/', loginView, name="Login"),
    path('registrar/', registro, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editarPerfil/', editar_perfil, name="editarPerfil"),
]
