from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Tip, CustomUser
from .forms import TipForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required


# Vista para la página de inicio (Home)
def home(request):
    tips = Tip.objects.select_related('author').all()
    return render(request, 'home.html', {'tips': tips})


# Vista para el inicio de sesión (Login)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
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
            messages.success(request, f'Welcome, {user.username}! Your account has been created successfully.')
            return redirect('home')
        else:
            messages.error(request, 'There was an error in your registration form. Please try again.')
    else:
        form = CustomUserCreationForm()
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
            tip.author = request.user
            tip.save()
            messages.success(request, 'Tip created successfully!')
            return redirect('home')
    else:
        form = TipForm()
    return render(request, 'create_tip.html', {'form': form})


@login_required
def vote_tip(request, tip_id, vote_type):
    tip = get_object_or_404(Tip, id=tip_id)

    if vote_type == 'upvote':
        tip.add_upvote(request.user)
    elif vote_type == 'downvote':
        if not request.user.has_perm('tips.can_downvote_tip') and request.user != tip.author:
            raise PermissionDenied("You do not have permission to downvote this tip.")
        tip.add_downvote(request.user)

    return redirect('home')


@login_required
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user != tip.author and not request.user.has_perm('tips.can_delete_tip'):
        raise PermissionDenied("You don't have permission to delete this tip.")

    tip.delete()
    messages.success(request, "The tip has been deleted successfully.")
    return redirect('home')

