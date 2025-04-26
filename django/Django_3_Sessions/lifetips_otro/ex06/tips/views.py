from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Tip, CustomUser
from .forms import TipForm, CustomUserCreationForm

# Vista para la página de inicio (Home)
def home(request):
    tips = Tip.objects.select_related('author').all()
    return render(request, 'home.html', {'tips': tips, 'form': TipForm()})

# Vista para el inicio de sesión (Login)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Te has conectado correctamente.")
            return redirect('home')
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Vista para el registro de usuarios (Register)
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}! Tu cuenta ha sido creada con éxito.')
            return redirect('home')
        else:
            messages.error(request, 'Hubo un error en tu formulario de registro. Por favor, inténtalo de nuevo.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Vista para cerrar sesión (Logout)
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('home')

# Vista para crear un nuevo tip (Create Tip)
@login_required
def create_tip(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            messages.success(request, '¡Tip creado correctamente!')
            return redirect('home')
    else:
        form = TipForm()
    return render(request, 'create_tip.html', {'form': form})

@login_required
def upvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    tip.add_upvote(request.user)
    return redirect('home')

@login_required
def downvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    try:
        tip.add_downvote(request.user)
    except PermissionDenied:
        messages.error(request, "No tienes permiso para votar negativo este tip.")
    return redirect('home')

@login_required
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user != tip.author and not request.user.has_perm('tips.can_delete_tip'):
        raise PermissionDenied("No tienes permiso para eliminar este tip.")

    tip.delete()
    messages.success(request, "El tip ha sido eliminado correctamente.")
    return redirect('home')
