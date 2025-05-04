import random
import time
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm

def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'home.html', {'username': username, 'is_authenticated': True})
    else:
        now = time.time()
        anonymous_name = request.session.get('anonymous_name')
        timestamp = request.session.get('anonymous_name_timestamp', 0)
        if not anonymous_name or now - timestamp > 42:
            anonymous_name = random.choice(settings.USERNAME_LIST)
            request.session['anonymous_name'] = anonymous_name
            request.session['anonymous_name_timestamp'] = now
        return render(request, 'home.html', {'username': anonymous_name, 'is_authenticated': False})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    error = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('home')
        else:
            error = "Por favor corrige los errores abajo."
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'error': error})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error = "Usuario o contraseña incorrectos."
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('home')
