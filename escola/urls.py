from django.urls import path
from django import views
from . import views


urlpatterns = [
    
    path('alunos/',views.AlunoViewSet, name ='alunos'),
    path('cursos/', views.CursoviewSet, name = 'cursos')
    
]