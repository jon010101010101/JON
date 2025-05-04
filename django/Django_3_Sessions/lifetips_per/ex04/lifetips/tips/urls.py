from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),         # Página principal: muestra tips y formulario si logueado
    path('register/', views.register, name='register'),  # Registro de usuario
    path('login/', views.login_view, name='login'),      # Login de usuario
    path('logout/', views.logout_view, name='logout'),   # Logout de usuario
    path('upvote/<int:tip_id>/', views.upvote_tip, name='upvote_tip'),
    path('downvote/<int:tip_id>/', views.downvote_tip, name='downvote_tip'),
    path('delete/<int:tip_id>/', views.delete_tip, name='delete_tip'),
]
