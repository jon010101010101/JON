from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import RegisterForm, LoginForm, TipForm
from .models import Tip
from django.conf import settings
import random
import time

def home(request):
    """
    Muestra la página principal con la lista de tips y el formulario para crear uno nuevo.
    Si el usuario no está autenticado, le asigna un nombre anónimo temporal.
    """
    tips = Tip.objects.select_related('author').order_by('-date')
    tip_form = None
    error = None

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
                error = "Please correct the errors below."
        else:
            tip_form = TipForm()
        return render(request, 'home.html', {
            'username': username,
            'is_authenticated': True,
            'tips': tips,
            'tip_form': tip_form,
            'error': error,
            'user': request.user,  # Para usar en el template
        })
    else:
        # Asignar nombre anónimo temporal si no está autenticado
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
    """
    Permite a un usuario registrarse. Si ya está autenticado, lo redirige al home.
    """
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
    """
    Permite a un usuario iniciar sesión. Si ya está autenticado, lo redirige al home.
    """
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
    """
    Cierra la sesión del usuario y lo redirige al home.
    """
    logout(request)
    return redirect('home')

@login_required
def upvote_tip(request, tip_id):
    """
    Permite al usuario dar upvote a un tip.
    Si ya lo ha hecho, lo quita; si no, lo añade y elimina el downvote si existía.
    """
    tip = get_object_or_404(Tip, id=tip_id)
    user = request.user
    if user in tip.upvoted_by.all():
        tip.upvoted_by.remove(user)
    else:
        tip.upvoted_by.add(user)
        tip.downvoted_by.remove(user)
    return redirect('home')

@login_required
def downvote_tip(request, tip_id):
    """
    Permite al usuario downvotear un tip si es el autor o tiene el permiso especial.
    Si no tiene permiso, muestra un mensaje de error amigable y redirige al home.
    """
    tip = get_object_or_404(Tip, id=tip_id)
    # Comprobar si el usuario es el autor o tiene el permiso personalizado
    if request.user == tip.author or request.user.has_perm('tips.can_downvote_tip'):
        user = request.user
        # Alternar el downvote: si ya lo hizo, lo quita; si no, lo añade y elimina el upvote
        if user in tip.downvoted_by.all():
            tip.downvoted_by.remove(user)
        else:
            tip.downvoted_by.add(user)
            tip.upvoted_by.remove(user)
        tip.save()
        return redirect('home')
    else:
        # Mensaje de error amigable si no tiene permiso
        messages.error(request, "You do not have permission to downvote this tip.")
        return redirect('home')

@login_required
def delete_tip(request, tip_id):
    """
    Permite eliminar un tip si el usuario es el autor o tiene el permiso especial.
    Si no tiene permiso, muestra un mensaje de error amigable y redirige al home.
    """
    tip = get_object_or_404(Tip, id=tip_id)
    # Comprobar si el usuario es el autor o tiene el permiso personalizado
    if request.user == tip.author or request.user.has_perm('tips.can_delete_tip'):
        tip.delete()
        return redirect('home')
    else:
        # Mensaje de error amigable si no tiene permiso
        messages.error(request, "You do not have permission to delete this tip.")
        return redirect('home')
