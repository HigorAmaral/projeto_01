from django.contrib import admin


from django.contrib import admin
from .models import  Professor, Turma, Aluno


admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Aluno)