from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Article, UserFavouriteArticle
from django.contrib.auth.models import User

# Vista principal de cuenta (login)
def account_view(request):
    if request.user.is_authenticated:
        return render(request, 'account/account.html', {'user': request.user})
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('articles')
        else:
            form = AuthenticationForm()
        return render(request, 'account/account.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('articles')

def article_list(request):
    articles = Article.objects.all().order_by('-created')
    return render(request, 'account/articles.html', {'articles': articles})

@login_required
def publications(request):
    articles = Article.objects.filter(author=request.user).order_by('-created')
    return render(request, 'account/publications.html', {'articles': articles})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles')
        else:
            return render(request, 'account/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})

@login_required
def publish(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        synopsis = request.POST.get('synopsis')
        content = request.POST.get('content')
        if title and synopsis and content:
            Article.objects.create(
                title=title,
                synopsis=synopsis,
                content=content,
                author=request.user
            )
            return redirect('articles')
    return render(request, 'account/publish.html')

@login_required
def favourites(request):
    favs = UserFavouriteArticle.objects.filter(user=request.user)
    return render(request, 'account/favourites.html', {'favs': favs})

@login_required
def add_favourite(request, pk):
    article = get_object_or_404(Article, pk=pk)
    fav, created = UserFavouriteArticle.objects.get_or_create(user=request.user, article=article)
    if not created:
        return redirect('already-favourite')
    return redirect('favourite-added')

@login_required
def favourite_added(request):
    return render(request, 'account/favourite_added.html')

@login_required
def already_favourite(request):
    return render(request, 'account/already_favourite.html')

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'account/article_detail.html', {'article': article})

def test_template(request):
    return render(request, 'account/prueba.html')

# Si realmente necesitas AJAX login/logout para algún frontend JS, puedes dejar estas vistas:
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ajax_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return JsonResponse({'success': True, 'username': form.get_user().username})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request'})

@csrf_exempt
def ajax_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': 'Invalid request'})
