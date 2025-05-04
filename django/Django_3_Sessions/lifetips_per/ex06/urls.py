from django.urls import path
from tips import views

urlpatterns = [
    # Home y autenticación
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Perfil y usuario
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

    # Tips
    path('tips/', views.tips_list, name='tips_list'),
    path('tip/<int:pk>/', views.TipDetailView.as_view(), name='tip_detail'),
    path('tip/new/', views.TipCreateView.as_view(), name='tip_create'),
    path('tip/<int:pk>/edit/', views.TipUpdateView.as_view(), name='tip_edit'),
    path('tip/<int:pk>/delete/', views.TipDeleteView.as_view(), name='tip_delete'),
    path('tip/<int:tip_id>/downvote/', views.downvote_tip, name='downvote_tip'),
    path('tip/<int:tip_id>/delete_tip/', views.delete_tip, name='delete_tip'),

    # Usuarios y ranking
    path('users/', views.users_list, name='users_list'),
    path('user_ranking/', views.user_ranking, name='user_ranking'),
    path('user/<int:user_id>/reputation/', views.user_reputation_detail, name='user_reputation_detail'),
    path('user/<int:user_id>/tips/', views.user_tips, name='user_tips'),

    # Búsqueda y estadísticas
    path('search/', views.search_tips, name='search_tips'),
    path('stats/', views.stats, name='stats'),
    path('vote_history/', views.vote_history, name='vote_history'),

    # Password reset usando las vistas genéricas de Django
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Administración y utilidades extra
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/toggle_user/<int:user_id>/', views.toggle_user_active, name='toggle_user_active'),
    path('admin/reset_reputations/', views.reset_all_reputations, name='reset_all_reputations'),
    path('admin/export_tips_csv/', views.export_tips_csv, name='export_tips_csv'),
    path('admin/logs/', views.view_logs, name='view_logs'),

    # Mantenimiento y errores
    path('maintenance/', views.maintenance, name='maintenance'),
]

# Personalización de la vista 404
handler404 = 'tips.views.custom_404_view'
