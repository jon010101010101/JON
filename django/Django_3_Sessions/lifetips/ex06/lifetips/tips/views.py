from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Tip
from .forms import TipForm, RegistrationForm, LoginForm


def home(request):
    tips = Tip.objects.all()
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            return redirect('home')
    else:
        form = TipForm()
    return render(request, 'home.html', {'tips': tips, 'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
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
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def upvote_tip(request, tip_id):
    tip = Tip.objects.get(pk=tip_id)
    tip.upvoted_by.add(request.user)
    return redirect('home')


@login_required
def downvote_tip(request, tip_id):
    tip = Tip.objects.get(pk=tip_id)
    tip.downvoted_by.add(request.user)
    return redirect('home')


@login_required
def delete_tip(request, tip_id):
    tip = Tip.objects.get(pk=tip_id)
    if tip.author == request.user or request.user.has_perm('tips.delete_tip'):
        tip.delete()
    return redirect('home')
