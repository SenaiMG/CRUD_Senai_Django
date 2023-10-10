from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100),
    idade = models.IntegerField("Idade"),
    