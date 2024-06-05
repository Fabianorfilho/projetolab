from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        sobrenome = request.POST.get('sobrenome')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        email = request.POST.get('email')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6 :
            messages.add_message(request, constants.ERROR, 'A senha deve ter no mínimo 6 caracteres')
            return redirect('/usuarios/cadastro')
        try:
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=sobrenome,
                username=username,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
        except:
            messages.add_message(request, constants.ERROR, '500')
            return redirect('/usuarios/cadastro')
        
        return redirect('/usuarios/cadastro')
    
    
def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = None
        try:
            user= User.objects.get(email=email)
        except User.DoesNotExist:
            pass
        
        if user and user.check_password(senha):
            user = authenticate(request, username=user.username, password=senha)
            if user:
                login(request, user)
                return redirect('/exames/solicitar_exames/')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha invalidos')
            return redirect('/usuarios/login')

def reset_senha(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Um e-mail foi enviado com instruções para redefinir sua senha.')
            return redirect('login')
        else:
            messages.error(request, 'Ocorreu um erro. Por favor, tente novamente.')
    else:
        form = PasswordResetForm()
    return render(request, 'resetsenha.html', {'form': form})

class ResetSenhaView(PasswordResetView):
    template_name = 'resetsenha.html'
    success_url = 'login'
    form_class = PasswordResetForm
    
def reset_senha(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)  # pass the request to the save method
            messages.success(request, 'Um e-mail foi enviado com instruções para redefinir sua senha.')
            return redirect('login')
        else:
            messages.error(request, 'Ocorreu um erro. Por favor, tente novamente.')
    else:
        form = PasswordResetForm()
    return render(request, 'resetsenha.html', {'form': form})