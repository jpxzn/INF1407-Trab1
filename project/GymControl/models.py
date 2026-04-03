from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    altura = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def __str__(self):
        return self.user.username

class Treino(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} - {self.aluno}'
    
class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    link_video = models.URLField(blank=True)
    musculo_trabalhado = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class TreinoExercicio(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)

    qtd_series = models.IntegerField()
    qtd_repeticoes = models.IntegerField()

    def __str__(self):
        return f'{self.exercicio} - {self.treino}'