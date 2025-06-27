from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms(request.POST or None)
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            
            nome = form['username'].value()
            senha = form['password'].value()
            
            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha                
            )
            
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha inválidos!')
                return redirect('login')
            
            # if usuario is not None and usuario.check_password(senha):
            #     return redirect('home')
            # else:
            #     return redirect('login')
    
    return render(request, 'usuarios/login.html', {'form' : form})


def cadastro(request):
    form = CadastroForms(request.POST or None)
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
                       
        if form.is_valid():
            if form['password_1'].value() != form['password_2'].value():
                messages.error(request, 'As senhas devem ser iguais!')
                return redirect('cadastro')
            
            nome = form['username'].value()
            email = form['email'].value()
            senha = form['password_1'].value()
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já cadastrado!')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username = nome,
                email = email,
                password = senha
            )
            usuario.save()
            messages.success(request, f'{nome} cadastrado com sucesso!')
            return redirect('login')
    
    return render(request, 'usuarios/cadastro.html', {'form' : form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('login')