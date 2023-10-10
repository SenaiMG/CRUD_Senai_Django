from django.shortcuts import render
from .models import Aluno
# Create your views here.

def index(request):
    alunos = Aluno.objects.all()
    return render(request, "index.html", {'alunos':alunos})

def create(request):
    Aluno.objects.create(nome=request.POST['nome'], idade=int(request.POST['idade']))
    alunos = Aluno.objects.all()
    return render(request, "index.html", {'alunos':alunos})