from django.urls import path
from django.contrib.auth import views as auth_views  # Importar vistas genéricas de autenticación
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    
    # Funciones relacionadas con los tips
    path('create_tip/', views.create_tip, name='create_tip'),
    path('tips/<int:tip_id>/upvote/', views.upvote_tip, name='upvote_tip'),
    path('tips/<int:tip_id>/downvote/', views.downvote_tip, name='downvote_tip'),
    path('tips/<int:tip_id>/delete/', views.delete_tip, name='delete_tip'),
    
    # Registro de nuevos usuarios
    path("register/", views.register, name="register"),
    
    # Login y Logout
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),  # Plantilla en la raíz del directorio templates
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]