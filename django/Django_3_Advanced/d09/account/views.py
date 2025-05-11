from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.utils import timezone
from .models import Article, UserFavouriteArticle
from django import forms

def truncate_synopsis(s, length=20):
    return s if len(s) <= length else s[:length-3] + '...'

def ago(dt):
    delta = timezone.now() - dt
    weeks = delta.days // 7
    days = delta.days % 7
    parts = []
    if weeks:
        parts.append(_("%(count)d week%(plural)s") % {'count': weeks, 'plural': 's' if weeks != 1 else ''})
    if days:
        parts.append(_("%(count)d day%(plural)s") % {'count': days, 'plural': 's' if days != 1 else ''})
    if not parts:
        return _("today")
    return ", ".join(parts) + _(" ago")

def home(request):
    return redirect('articles')

def articles(request):
    error = None
    login_form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and 'login_menu' in request.POST:
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('articles')
        else:
            error = _("Invalid username or password.")
    articles = Article.objects.all().order_by('-created')
    context = {
        'articles': articles,
        'login_form': login_form,
        'error': error,
        'user': request.user,
        'LANGUAGE_CODE': request.LANGUAGE_CODE,
        'truncate_synopsis': truncate_synopsis,
        'ago': ago,
    }
    return render(request, 'articles/article_list.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required
def favourites(request):
    favs = UserFavouriteArticle.objects.filter(user=request.user)
    return render(request, 'articles/favourites_list.html', {'favourites': favs})

@login_required
def add_favourite(request, pk):
    article = get_object_or_404(Article, pk=pk)
    fav, created = UserFavouriteArticle.objects.get_or_create(user=request.user, article=article)
    if not created:
        return redirect('already-favourite')
    return redirect('favourite-added')

@login_required
def favourite_added(request):
    return render(request, 'articles/favourite_added.html')

@login_required
def already_favourite(request):
    return render(request, 'articles/already_favourite.html')

@login_required
def publications(request):
    pubs = Article.objects.filter(author=request.user)
    return render(request, 'articles/publications_list.html', {'publications': pubs})

@login_required
def publish(request):
    if request.method == "POST":
        title = request.POST.get('title')
        synopsis = request.POST.get('synopsis')
        content = request.POST.get('content')
        if title and synopsis and content:
            Article.objects.create(
                title=title,
                author=request.user,
                synopsis=synopsis,
                content=content
            )
            return redirect('publications')
    return render(request, 'articles/publish.html')

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('articles')
    return render(request, 'articles/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('articles')
