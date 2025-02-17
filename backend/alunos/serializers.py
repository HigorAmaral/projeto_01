from rest_framework.serializers import ModelSerializer
from .models import Professor, Turma, Aluno

class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'