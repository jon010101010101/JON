from django.urls import path
from .views import (
    ArticleListView, ArticleDetailView, PublicationsListView, FavouritesListView,
    PublishArticleView, RegisterView, AddFavouriteView, HomeRedirectView
)
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', HomeRedirectView.as_view(), name='home'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('publications/', PublicationsListView.as_view(), name='publications'),
    path('favourites/', FavouritesListView.as_view(), name='favourites'),
    path('publish/', PublishArticleView.as_view(), name='publish'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='articles/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='articles'), name='logout'),
    path('articles/<int:pk>/add_favourite/', AddFavouriteView.as_view(), name='add-favourite'),
    # Confirmaciones tras añadir a favoritos
    path('favourite-added/', TemplateView.as_view(template_name='articles/favourite_added.html'), name='favourite-added'),
    path('already-favourite/', TemplateView.as_view(template_name='articles/already_favourite.html'), name='already-favourite'),
]
