
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunoViewSet, CursoviewSet, MatriculaviewSet, ListaMatriculasAluno, listaalunomatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet,basename= 'alunos')
router.register('cursos', CursoviewSet, basename= 'cursos')
router.register('matriculas', MatriculaviewSet, basename= 'matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('aluno/<int:pk>/matriculas/',ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/',listaalunomatriculados.as_view()),
]
