from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_tip, name='create_tip'),
    path('<int:tip_id>/upvote/', views.upvote_tip, name='upvote_tip'),
    path('<int:tip_id>/downvote/', views.downvote_tip, name='downvote_tip'),
    path('<int:tip_id>/delete/', views.delete_tip, name='delete_tip'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
