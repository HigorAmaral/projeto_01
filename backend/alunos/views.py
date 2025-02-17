from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Professor, Turma, Aluno
from .serializers import ProfessorSerializer, TurmaSerializer, AlunoSerializer

class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
