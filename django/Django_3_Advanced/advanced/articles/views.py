from django.views.generic import (
    ListView, DetailView, CreateView, RedirectView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from .models import Article, UserFavouriteArticle
from .forms import ArticleForm
from django.shortcuts import redirect


# Mixin para login en menú de todas las vistas
class LoginMenuMixin:
    error_message = None

    def post(self, request, *args, **kwargs):
        # Solo procesa el login si el POST viene del menú (campo oculto login_menu)
        if 'username' in request.POST and 'password' in request.POST and 'login_menu' in request.POST:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect(request.path)
            else:
                self.error_message = _("Invalid username or password.")
            return self.get(request, *args, **kwargs)
        # Si es un POST normal (por ejemplo, register), deja que el CreateView lo gestione
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error_message'] = getattr(self, 'error_message', None)
        return context

class ArticleListView(LoginMenuMixin, ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created']

class ArticleDetailView(LoginMenuMixin, DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        article = self.get_object()
        context['is_favourite'] = False
        if user.is_authenticated:
            context['is_favourite'] = UserFavouriteArticle.objects.filter(user=user, article=article).exists()
        return context

class PublicationsListView(LoginMenuMixin, LoginRequiredMixin, ListView):
    model = Article
    template_name = 'articles/publications_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user).order_by('-created')

class FavouritesListView(LoginMenuMixin, LoginRequiredMixin, ListView):
    model = UserFavouriteArticle
    template_name = 'articles/favourites_list.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(user=self.request.user)

class PublishArticleView(LoginMenuMixin, LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/publish.html'
    success_url = reverse_lazy('publications')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RegisterView(LoginMenuMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'articles/register.html'
    success_url = reverse_lazy('articles')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('articles')
        return super().dispatch(request, *args, **kwargs)

class AddFavouriteView(LoginMenuMixin, LoginRequiredMixin, CreateView):
    model = UserFavouriteArticle
    fields = []
    template_name = 'articles/add_favourite.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article_id = self.kwargs['pk']
        # Evita duplicados:
        if UserFavouriteArticle.objects.filter(user=form.instance.user, article=form.instance.article).exists():
            return redirect('already-favourite')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('favourite-added')

class HomeRedirectView(RedirectView):
    pattern_name = 'articles'
