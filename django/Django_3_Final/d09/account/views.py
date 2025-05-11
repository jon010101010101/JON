from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Article, UserFavouriteArticle
from django.contrib.auth.models import User

# Vista principal de cuenta (puedes mejorar el template después)
def account_view(request):
    if request.user.is_authenticated:
        return render(request, 'account/account.html', {'user': request.user})
    else:
        form = AuthenticationForm()
        return render(request, 'account/account.html', {'form': form})

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

def article_list(request):
    # Lógica básica para mostrar artículos
    articles = Article.objects.all().order_by('-created')
    if request.method == 'POST' and 'login_menu' in request.POST:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('articles')
        else:
            return render(request, 'account/articles.html', {
                'articles': articles,
                'form': form,
                'login_error': "Invalid username or password."
            })
    return render(request, 'account/articles.html', {'articles': articles})

@login_required
def publications(request):
    # Artículos publicados por el usuario autenticado
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

def logout_view(request):
    logout(request)
    return redirect('articles')

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
    from django.shortcuts import render
    return render(request, 'account/prueba.html')
