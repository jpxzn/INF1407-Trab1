from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from .models import Treino, Aluno
from .forms import CustomUserCreationForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'GymControl/home.html')
    
class UserLoginView(LoginView):
    template_name = 'GymControl/login.html'

class CadastroView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'GymControl/cadastro.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Aluno.objects.create(user=user)
            return redirect('GymControl:login')

        return render(request, 'GymControl/cadastro.html', {'form': form})

class TreinosView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            aluno = Aluno.objects.get(user=request.user)
            treinos = Treino.objects.filter(aluno=aluno)
        except Aluno.DoesNotExist:
            treinos = []

        return render(request, 'GymControl/treinos.html', {
            'treinos': treinos
        })
    
class AvaliacaoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'GymControl/avaliacao.html')