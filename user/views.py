from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from e_commerce.settings import LOGOUT_REDIRECT_URL
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from user.serializer import UserSerializer


def login_view(request):
    pass


def logout_view(request):
    return LOGOUT_REDIRECT_URL


def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.method != 'POST':
        # Exibe o formulário de cadastro em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz login do usuário e o redireciona para a página inicial
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


class UserViewSet(viewsets.ModelViewSet):
    """Define o comportamento da view da API"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #authentication_classes = [BaseAuthentication]
    #permission_classes = [IsAuthenticated]
