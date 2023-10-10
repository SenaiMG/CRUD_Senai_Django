from django.shortcuts import render, redirect
from .models import Aluno
# Create your views here.

def index(request):
    alunos = Aluno.objects.all()
    return render(request, "index.html", {'alunos':alunos})

def create(request):
    Aluno.objects.create(nome=request.POST['nome'], idade=int(request.POST['idade']))
    alunos = Aluno.objects.all()
    return redirect('index')

def edit(request, id):
    aluno = Aluno.objects.get(pk=id)
    return render(request, "editar.html",{'aluno':aluno})

def update(request, id):
    aluno = Aluno.objects.get(pk=id)
    aluno.nome = request.POST['nome']
    aluno.idade = request.POST['idade']
    aluno.save()
    return redirect('index')

def delete(request, id):
    aluno = Aluno.objects.get(pk=id)
    aluno.delete()
    return redirect('index')