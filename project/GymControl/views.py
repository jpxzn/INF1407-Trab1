from django.shortcuts import render
from django.views.generic.base import View

from GymControl.models import Aluno

class TesteView(View):
    def get(self, request, *args, **kwargs):
        aluno = Aluno.objects.all()
        contexto = { 'alunos': aluno, }
        return render(
            request,
            'GymControl/teste.html',
            contexto
        )
