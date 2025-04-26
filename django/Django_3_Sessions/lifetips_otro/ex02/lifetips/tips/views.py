from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, TipForm
from .models import Tip
from django.conf import settings
import random, time

def home(request):
    tips = Tip.objects.select_related('author').order_by('-date')
    tip_form = None
    error = None  # <-- Añade esto

    if request.user.is_authenticated:
        username = request.user.username
        if request.method == 'POST':
            tip_form = TipForm(request.POST)
            if tip_form.is_valid():
                tip = tip_form.save(commit=False)
                tip.author = request.user
                tip.save()
                return redirect('home')
            else:
                error = "Please correct the errors below."  # <-- Añade esto
        else:
            tip_form = TipForm()
        return render(request, 'home.html', {
            'username': username,
            'is_authenticated': True,
            'tips': tips,
            'tip_form': tip_form,
            'error': error,
        })
    else:
        # Lógica de nombre anónimo (igual que ex01)
        now = time.time()
        anonymous_name = request.session.get('anonymous_name')
        timestamp = request.session.get('anonymous_name_timestamp', 0)
        if not anonymous_name or now - timestamp > 42:
            anonymous_name = random.choice(settings.USERNAME_LIST)
            request.session['anonymous_name'] = anonymous_name
            request.session['anonymous_name_timestamp'] = now
        return render(request, 'home.html', {
            'username': anonymous_name,
            'is_authenticated': False,
            'tips': tips,
        })


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
            error = "Please correct the errors below."
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
                error = "Invalid username or password."
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('home')
