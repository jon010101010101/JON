from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import TipForm
from .models import Tip
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Vista para la página de inicio (Home)
def home(request):
    tips = Tip.objects.all()  # Obtiene todos los tips del modelo Tip
    return render(request, 'home.html', {'tips': tips})

# Vista para el inicio de sesión (Login)
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  # Redirige a la página principal después del inicio de sesión
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html', {'form': form})

# Vista para el registro de usuarios (Register)
def register(request):
    form = CustomUserCreationForm(request.POST or None)  # Usa el formulario personalizado
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()  # Guarda el usuario utilizando el modelo personalizado
            login(request, user)  # Inicia sesión automáticamente después del registro
            messages.success(request, f'Welcome, {user.username}! Your account has been created successfully.')
            return redirect('home')  # Redirige a la página principal
        else:
            messages.error(request, 'There was an error in your registration form. Please try again.')
    return render(request, 'register.html', {'form': form})

# Vista para cerrar sesión (Logout)
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

# Vista para crear un nuevo tip (Create Tip)
@login_required
def create_tip(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user  # Asignar el usuario autenticado como autor
            tip.save()
            return redirect('home')  # Redirigir a la página principal
    else:
        form = TipForm()
    return render(request, 'create_tip.html', {'form': form})

# Vista para manejar los "upvotes" de un tip
def upvote_tip(request, tip_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to upvote a tip.")
        return redirect('login')
    
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user not in tip.upvotes.all():  # Evita duplicados
        tip.upvotes.add(request.user)
        tip.author.update_reputation(5)  # Aumenta la reputación del autor
        messages.success(request, "You have upvoted the tip!")
    else:
        messages.info(request, "You have already upvoted this tip.")
    return redirect('home')

# Manejar el downvote de un tip
def downvote_tip(request, tip_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to downvote a tip.")
        return redirect('login')
    
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user in tip.downvotes.all():
        messages.info(request, "You have already downvoted this tip.")
    else:
        try:
            tip.downvote(request.user)
            messages.success(request, "You have downvoted the tip!")
        except PermissionError as e:
            messages.error(request, str(e))
    return redirect('home')

# Eliminar un tip
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    if not request.user.is_authenticated or request.user != tip.author:
        messages.error(request, "You don't have permission to delete this tip.")
        return redirect('home')
    
    # Si el usuario es el autor, eliminar el tip
    tip.delete()
    messages.success(request, "The tip has been deleted successfully.")
    return redirect('home')