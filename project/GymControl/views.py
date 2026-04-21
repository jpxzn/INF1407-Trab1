from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from .models import Treino, Aluno, TreinoExercicio
from .forms import CustomUserCreationForm, TreinoForm, TreinoExercicioForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'GymControl/common/home.html')
    
class UserLoginView(LoginView):
    template_name = 'GymControl/user/auth/login.html'

class CadastroView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'GymControl/user/auth/cadastro.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Aluno.objects.create(user=user)
            return redirect('GymControl:login')

        return render(request, 'GymControl/user/auth/cadastro.html', {'form': form})

class TreinosView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            alunos = Aluno.objects.all()
            return render(request, 'GymControl/admin/treino/treinos_admin.html', {
                'alunos': alunos
            })

        aluno = Aluno.objects.get(user=request.user)
        treinos = Treino.objects.filter(aluno=aluno)

        return render(request, 'GymControl/user/treino/treinos.html', {
            'treinos': treinos
        })
    
class ExerciciosTreinoView(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            treino = Treino.objects.get(id=id)
        else:
            aluno = Aluno.objects.get(user=request.user)
            treino = Treino.objects.get(id=id, aluno=aluno)

        exercicios = TreinoExercicio.objects.filter(treino=treino)

        return render(request, 'GymControl/user/treino/exerciciosTreino.html', {
            'treino': treino,
            'exercicios': exercicios
        })

class TreinosAlunoView(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        aluno = get_object_or_404(Aluno, id=id)
        treinos = Treino.objects.filter(aluno=aluno)

        return render(request, 'GymControl/admin/treino/treinosAluno.html', {
            'aluno': aluno,
            'treinos': treinos
        })


class CriarTreinoView(LoginRequiredMixin, View):
    def get(self, request, aluno_id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        aluno = get_object_or_404(Aluno, id=aluno_id)
        form = TreinoForm()

        return render(request, 'GymControl/admin/treino/criarTreino.html', {
            'aluno': aluno,
            'form': form
        })

    def post(self, request, aluno_id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        aluno = get_object_or_404(Aluno, id=aluno_id)
        form = TreinoForm(request.POST)

        if form.is_valid():
            treino = form.save(commit=False)
            treino.aluno = aluno
            treino.save()
            return redirect('GymControl:treinosAluno', id=aluno.id)

        return render(request, 'GymControl/admin/treino/criarTreino.html', {
            'aluno': aluno,
            'form': form
        })


class EditarTreinoView(LoginRequiredMixin, View):
    def get(self, request, treino_id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        treino = get_object_or_404(Treino, id=treino_id)
        form = TreinoForm(instance=treino)

        return render(request, 'GymControl/admin/treino/editarTreino.html', {
            'treino': treino,
            'form': form
        })

    def post(self, request, treino_id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        treino = get_object_or_404(Treino, id=treino_id)
        form = TreinoForm(request.POST, instance=treino)

        if form.is_valid():
            form.save()
            return redirect('GymControl:treinosAluno', id=treino.aluno.id)

        return render(request, 'GymControl/admin/treino/editarTreino.html', {
            'treino': treino,
            'form': form
        })


class DeletarTreinoView(LoginRequiredMixin, View):
    def post(self, request, treino_id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        treino = get_object_or_404(Treino, id=treino_id)
        aluno_id = treino.aluno.id
        treino.delete()

        return redirect('GymControl:treinosAluno', id=aluno_id)
    
class ExerciciosTreinoAdminView(LoginRequiredMixin, View):
    def get(self, request, treino_id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        treino = get_object_or_404(Treino, id=treino_id)
        exercicios = TreinoExercicio.objects.filter(treino=treino)

        return render(request, 'GymControl/admin/treino/exerciciosTreinoAdmin.html', {
            'treino': treino,
            'exercicios': exercicios
        })

class CriarExercicioTreinoView(LoginRequiredMixin, View):
    def get(self, request, treino_id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        treino = get_object_or_404(Treino, id=treino_id)
        form = TreinoExercicioForm()

        return render(request, 'GymControl/admin/treino/criarExercicioTreino.html', {
            'treino': treino,
            'form': form
        })

    def post(self, request, treino_id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        treino = get_object_or_404(Treino, id=treino_id)
        form = TreinoExercicioForm(request.POST)

        if form.is_valid():
            treino_exercicio = form.save(commit=False)
            treino_exercicio.treino = treino
            treino_exercicio.save()
            return redirect('GymControl:exerciciosTreinoAdmin', treino_id=treino.id)

        return render(request, 'GymControl/admin/treino/criarExercicioTreino.html', {
            'treino': treino,
            'form': form
        })
    
class EditarExercicioTreinoView(LoginRequiredMixin, View):
    def get(self, request, treino_exercicio_id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        treino_exercicio = get_object_or_404(TreinoExercicio, id=treino_exercicio_id)
        form = TreinoExercicioForm(instance=treino_exercicio)

        return render(request, 'GymControl/admin/treino/editarExercicioTreino.html', {
            'treino_exercicio': treino_exercicio,
            'treino': treino_exercicio.treino,
            'form': form
        })

    def post(self, request, treino_exercicio_id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        treino_exercicio = get_object_or_404(TreinoExercicio, id=treino_exercicio_id)
        form = TreinoExercicioForm(request.POST, instance=treino_exercicio)

        if form.is_valid():
            form.save()
            return redirect('GymControl:exerciciosTreinoAdmin', treino_id=treino_exercicio.treino.id)

        return render(request, 'GymControl/admin/treino/editarExercicioTreino.html', {
            'treino_exercicio': treino_exercicio,
            'treino': treino_exercicio.treino,
            'form': form
        })
    
class DeletarExercicioTreinoView(LoginRequiredMixin, View):
    def post(self, request, treino_exercicio_id, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return redirect('GymControl:home')

        treino_exercicio = get_object_or_404(TreinoExercicio, id=treino_exercicio_id)
        treino_id = treino_exercicio.treino.id
        treino_exercicio.delete()

        return redirect('GymControl:exerciciosTreinoAdmin', treino_id=treino_id)
class AvaliacaoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'GymControl/user/avaliacao.html')