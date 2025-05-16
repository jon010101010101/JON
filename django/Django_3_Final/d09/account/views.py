from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Article, UserFavouriteArticle
from .forms import ArticleForm
from django.contrib.auth.models import User

# -----------------------------------
# Vistas relacionadas con artículos
# -----------------------------------

# Vista para listar todos los artículos
def article_list(request):
    articles = Article.objects.all().order_by('-created')  # Ordenados por fecha de creación
    return render(request, 'account/article_list.html', {'articles': articles})


# Vista para ver los detalles de un artículo
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'account/article_detail.html', {'article': article})


# Vista para crear un nuevo artículo
@login_required
def publish(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # Asignar el usuario autenticado como autor
            article.save()
            messages.success(request, 'El artículo fue creado con éxito.')
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'account/article_form.html', {'form': form})


# -----------------------------------
# Vistas relacionadas con favoritos
# -----------------------------------

# Vista para listar los artículos favoritos del usuario
@login_required
def favourites(request):
    favourites = UserFavouriteArticle.objects.filter(user=request.user).select_related('article')
    return render(request, 'account/favourite_list.html', {'favourites': favourites})


# Vista para añadir un artículo a favoritos
@login_required
def add_favourite(request, pk):
    article = get_object_or_404(Article, pk=pk)
    favourite, created = UserFavouriteArticle.objects.get_or_create(user=request.user, article=article)
    if created:
        messages.success(request, f'El artículo "{article.title}" fue añadido a tus favoritos.')
    else:
        messages.info(request, f'El artículo "{article.title}" ya está en tus favoritos.')
    return redirect('article_detail', pk=pk)


# Vista para mostrar un mensaje de favorito añadido
@login_required
def favourite_added(request):
    messages.success(request, 'El artículo fue añadido a tus favoritos con éxito.')
    return redirect('favourites')


# Vista para mostrar un mensaje si el artículo ya está en favoritos
@login_required
def already_favourite(request):
    messages.info(request, 'El artículo ya está en tus favoritos.')
    return redirect('favourites')


# -----------------------------------
# Vistas relacionadas con usuarios
# -----------------------------------

# Vista para registrar un nuevo usuario
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, 'Te has registrado con éxito.')
            return redirect('article_list')
    return render(request, 'account/register.html')


# Vista para cerrar sesión
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Cerraste sesión con éxito.')
    return redirect('article_list')


# Vista para manejar el inicio de sesión vía AJAX
def ajax_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'account/ajax_response.html', {'status': 'success', 'message': f'Welcome, {user.username}!'})
        else:
            return render(request, 'account/ajax_response.html', {'status': 'error', 'message': 'Invalid username or password.'})
    return redirect('account')


# Vista para manejar el cierre de sesión vía AJAX
@login_required
def ajax_logout(request):
    logout(request)
    return render(request, 'account/ajax_response.html', {'status': 'success', 'message': 'Has cerrado sesión con éxito.'})


# Vista para mostrar la cuenta del usuario (perfil)
@login_required
def account_view(request):
    return render(request, 'account/account.html', {'user': request.user})


# -----------------------------------
# Vista para mostrar publicaciones (opcional)
# -----------------------------------

# Vista de publicaciones (puede ser personalizada)
def publications(request):
    # Puedes personalizar esta vista para manejar publicaciones específicas
    return render(request, 'account/publications.html')