from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms



def login(request):
    form = LoginForms(request.POST or None)
    return render(request, 'usuarios/login.html', {'form' : form})


def cadastro(request):
    form = CadastroForms(request.POST or None)
    return render(request, 'usuarios/cadastro.html', {'form' : form})
