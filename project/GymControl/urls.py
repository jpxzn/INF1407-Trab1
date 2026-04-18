from django.urls.conf import path
from django.urls import reverse_lazy
from .views import *
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = "GymControl"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(
        template_name='GymControl/password_reset.html',
        email_template_name='GymControl/password_reset_email.html',
        success_url=reverse_lazy('GymControl:password_reset_done')),
        name='password_reset'),
    path('password-reset/done/',PasswordResetDoneView.as_view(
        template_name='GymControl/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='GymControl/password_reset_confirm.html',
        success_url=reverse_lazy('GymControl:password_reset_complete')),
        name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='GymControl/password_reset_complete.html'), 
        name='password_reset_complete'),
    path('treinos/', TreinosView.as_view(), name='treinos'),
    path('treinos/aluno/<int:id>/', TreinosAlunoView.as_view(), name='treinosAluno'),
    path('treinos/aluno/<int:aluno_id>/criar/', CriarTreinoView.as_view(), name='criarTreino'),
    path('treinos/<int:treino_id>/editar/', EditarTreinoView.as_view(), name='editarTreino'),
    path('treinos/<int:treino_id>/deletar/', DeletarTreinoView.as_view(), name='deletarTreino'),
    path('treinos/<int:id>/', ExerciciosTreinoView.as_view(), name='exerciciosTreino'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),
]