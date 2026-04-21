from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from .views import (
    HomeView,
    UserLoginView,
    CadastroView,
    TreinosView,
    TreinosAlunoView,
    CriarTreinoView,
    EditarTreinoView,
    DeletarTreinoView,
    ExerciciosTreinoAdminView,
    CriarExercicioTreinoView,
    EditarExercicioTreinoView,
    DeletarExercicioTreinoView,
    ExerciciosTreinoView,
    AvaliacaoView,
)

app_name = "GymControl"

# ------------------ AUTENTICAÇÃO ------------------
auth_patterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("cadastro/", CadastroView.as_view(), name="cadastro"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

# ------------------ RESET DE SENHA ------------------
password_patterns = [
    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="GymControl/user/auth/password_reset.html",
            email_template_name="GymControl/user/auth/password_reset_email.html",
            success_url=reverse_lazy("GymControl:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(
            template_name="GymControl/user/auth/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="GymControl/user/auth/password_reset_confirm.html",
            success_url=reverse_lazy("GymControl:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="GymControl/user/auth/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]

# ------------------ TREINOS ------------------
treinos_patterns = [
    path("treinos/", TreinosView.as_view(), name="treinos"),
    path("treinos/aluno/<int:id>/", TreinosAlunoView.as_view(), name="treinosAluno"),
    path("treinos/aluno/<int:aluno_id>/criar/", CriarTreinoView.as_view(), name="criarTreino"),
    path("treinos/<int:treino_id>/editar/", EditarTreinoView.as_view(), name="editarTreino"),
    path("treinos/<int:treino_id>/deletar/", DeletarTreinoView.as_view(), name="deletarTreino"),
]

# ------------------ EXERCÍCIOS (ADMIN) ------------------
exercicios_admin_patterns = [
    path(
        "treinos/<int:treino_id>/exercicios/",
        ExerciciosTreinoAdminView.as_view(),
        name="exerciciosTreinoAdmin",
    ),
    path(
        "treinos/<int:treino_id>/exercicios/criar/",
        CriarExercicioTreinoView.as_view(),
        name="criarExercicioTreino",
    ),
    path(
        "treinos/exercicio/<int:treino_exercicio_id>/editar/",
        EditarExercicioTreinoView.as_view(),
        name="editarExercicioTreino",
    ),
    path(
        "treinos/exercicio/<int:treino_exercicio_id>/deletar/",
        DeletarExercicioTreinoView.as_view(),
        name="deletarExercicioTreino",
    ),
]

# ------------------ EXERCÍCIOS (ALUNO) ------------------
exercicios_patterns = [
    path("treinos/<int:id>/", ExerciciosTreinoView.as_view(), name="exerciciosTreino"),
]

# ------------------ AVALIAÇÃO ------------------
avaliacao_patterns = [
    path("avaliacao/", AvaliacaoView.as_view(), name="avaliacao"),
]

# ------------------ URLS FINAIS ------------------
urlpatterns = [
    *auth_patterns,
    *password_patterns,
    *treinos_patterns,
    *exercicios_admin_patterns,
    *exercicios_patterns,
    *avaliacao_patterns,
]