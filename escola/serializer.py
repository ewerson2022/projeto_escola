#o serializers é responsavel por fazer a ponte entre o python e json 
from rest_framework import serializers
from escola.models import Curso, Aluno,Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome','rg', 'cpf', 'data_nascimento']
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__' 