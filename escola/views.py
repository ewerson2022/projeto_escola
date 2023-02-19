from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class CursoviewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaviewSet(viewsets.ModelViewSet):
    """exibindo todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer