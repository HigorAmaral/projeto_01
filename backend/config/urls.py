from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alunos.views import ProfessorViewSet
from alunos.views import TurmaViewSet
from alunos.views import AlunoViewSet

router = DefaultRouter()
router.register( 'professor', ProfessorViewSet)
router.register( 'turma', TurmaViewSet)
router.register( 'aluno', AlunoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]