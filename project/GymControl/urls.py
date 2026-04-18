from django.urls.conf import path
from django.contrib.auth.views import LogoutView
from .views import *
app_name = "GymControl"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('treinos/', TreinosView.as_view(), name='treinos'),
    path('treinos/aluno/<int:id>/', TreinosAlunoView.as_view(), name='treinosAluno'),
    path('treinos/aluno/<int:aluno_id>/criar/', CriarTreinoView.as_view(), name='criarTreino'),
    path('treinos/<int:treino_id>/editar/', EditarTreinoView.as_view(), name='editarTreino'),
    path('treinos/<int:treino_id>/deletar/', DeletarTreinoView.as_view(), name='deletarTreino'),
    path('treinos/<int:id>/', ExerciciosTreinoView.as_view(), name='exerciciosTreino'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),
]