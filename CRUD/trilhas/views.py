from django.shortcuts import render, redirect
from .models import Aluno
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .forms import LoginForms
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    #if not request.user.is_authenticated:
    #    messages.error(request, 'Usuário não logado')
    #    return redirect('login')
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


#fazer autenticação e login

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')