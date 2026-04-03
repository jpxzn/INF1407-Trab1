from django.urls.conf import path
from GymControl import views

app_name = "GymControl"

urlpatterns = [
    path('teste/', views.TesteView.as_view(), name='teste'),
]