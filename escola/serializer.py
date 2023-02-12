from rest_framework import serializers
from escola.models import Curso, Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'cpf', 'data_nascimento']
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
#o serializers é responsavel por fazer a ponte entre o python e json 