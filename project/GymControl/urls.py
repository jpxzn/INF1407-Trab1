from django.urls.conf import path
from django.contrib.auth.views import LogoutView
from .views import HomeView, TreinosView, AvaliacaoView, UserLoginView, CadastroView

app_name = "GymControl"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('treinos/', TreinosView.as_view(), name='treinos'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),
]