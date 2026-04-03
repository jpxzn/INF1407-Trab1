from django.contrib import admin

from GymControl.models import Aluno
from GymControl.models import Treino
from GymControl.models import Exercicio
from GymControl.models import TreinoExercicio

admin.site.register(Aluno)
admin.site.register(Treino)
admin.site.register(Exercicio)
admin.site.register(TreinoExercicio)
