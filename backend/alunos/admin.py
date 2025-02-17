from django.contrib import admin


from django.contrib import admin
from .models import Estado, Cidade, Aluno


admin.site.register(Estado)
admin.site.register(Aluno)
admin.site.register(Cidade)
