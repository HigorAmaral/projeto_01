from django.db import models

# Create your models here.
from django.db import models

    # Trabalho
    

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    disciplina = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nome}  -  {self.disciplina}  -  {self.email}'
    
class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    id_professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    horario = models.TimeField()

    def __str__(self):
        return f'{self.nome}  -  {self.id_professor.nome}  -  {self.horario}'
    
class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=5)
    curso = models.CharField(max_length=100)
    id_turma = models.ForeignKey('Turma', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome}  -  {self.matricula}  -  {self.curso}'