from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, Http404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from tips.forms import TipForm
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from tips.models import CustomUser, Tip
from django.utils.timezone import now
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()


# Página principal (home)
def home(request):
    tips = Tip.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'tips': tips})

# Registro de usuario
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login de usuario
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Logout de usuario
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

# Perfil de usuario
@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

# Edición de perfil
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

# Cambio de contraseña desde el perfil
@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomSetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Your password was updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = CustomSetPasswordForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

# Lista de tips
class TipListView(ListView):
    model = Tip
    template_name = 'tips/tip_list.html'
    context_object_name = 'tips'
    ordering = ['-created_at']

# Detalle de un tip
class TipDetailView(DetailView):
    model = Tip
    template_name = 'tips/tip_detail.html'
    context_object_name = 'tip'

# Crear un nuevo tip
class TipCreateView(LoginRequiredMixin, CreateView):
    model = Tip
    form_class = TipForm
    template_name = 'tips/tip_form.html'
    success_url = reverse_lazy('tip_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Tip created successfully.")
        return super().form_valid(form)

# Editar un tip existente
class TipUpdateView(LoginRequiredMixin, UpdateView):
    model = Tip
    form_class = TipForm
    template_name = 'tips/tip_form.html'
    success_url = reverse_lazy('tip_list')

    def get_queryset(self):
        return Tip.objects.filter(author=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Tip updated successfully.")
        return super().form_valid(form)

# Eliminar un tip
class TipDeleteView(LoginRequiredMixin, DeleteView):
    model = Tip
    template_name = 'tips/tip_confirm_delete.html'
    success_url = reverse_lazy('tip_list')

    def get_queryset(self):
        return Tip.objects.filter(author=self.request.user)

# Vista para manejar los votos negativos (Downvote)
@login_required
def downvote_tip(request, tip_id):
    """
    Permite a un usuario autenticado emitir un voto negativo en un tip.
    """
    tip = get_object_or_404(Tip, id=tip_id)
    try:
        tip.downvote(request.user)
        messages.success(request, 'You downvoted the tip!')
    except PermissionDenied as e:
        messages.error(request, str(e))
    return redirect('home')

# Vista para eliminar un tip (Delete Tip)
@login_required
def delete_tip(request, tip_id):
    """
    Permite a un usuario autenticado eliminar su propio tip.
    Si no es el autor o un superusuario, se lanza una excepción.
    """
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user != tip.author and not request.user.is_superuser:
        raise PermissionDenied("You don't have permission to delete this tip.")
    try:
        upvotes_count = tip.upvotes.count()
        downvotes_count = tip.downvotes.count()
        tip.author.update_reputation(delta_upvotes=-upvotes_count, delta_downvotes=-downvotes_count)
        tip.delete()
        messages.success(request, 'Tip deleted successfully.')
    except Exception as e:
        messages.error(request, f"An error occurred while deleting the tip: {str(e)}")
    return redirect('home')

# Vista para listar usuarios con email y reputación
@login_required
def users_list(request):
    """
    Muestra una lista de usuarios ordenados por reputación en orden descendente.
    """
    users = User.objects.all().order_by('-reputation')
    return render(request, 'tips/users_list.html', {'users': users})

# Vista para listar todos los tips
def tips_list(request):
    """
    Muestra una lista de todos los tips disponibles.
    """
    try:
        tips = Tip.objects.all()
        for tip in tips:
            tip.author.update_reputation(delta_upvotes=tip.upvotes.count(), delta_downvotes=tip.downvotes.count())
    except Exception as e:
        tips = []
        messages.error(request, f"An error occurred while loading the tips list: {str(e)}")
    return render(request, 'tips/tips_list.html', {'tips': tips})

# Vista personalizada para errores 404 (Página no encontrada)
def custom_404_view(request, exception):
    """
    Vista personalizada para manejar errores 404.
    """
    return render(request, '404.html', status=404)

# --------------------------
# Password Reset con Simulación
# --------------------------

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

class CustomPasswordResetView(PasswordResetView):
    """
    Clase personalizada para manejar el flujo de restablecimiento de contraseñas.
    """
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.txt'
    html_email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = '/password_reset/done/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Cambia esto a True/False según quieras mostrar el botón de simulación
        context['simulation_enabled'] = getattr(settings, 'EMAIL_BACKEND', '').endswith('console.EmailBackend')
        context['simulated_reset_link'] = self.request.session.get('simulated_reset_link', '')
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data["email"]
        user = User.objects.filter(email__iexact=email, is_active=True).first()
        if user:
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = self.request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
            )
            self.request.session['simulated_reset_link'] = reset_link
        return response

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['simulation_enabled'] = getattr(settings, 'EMAIL_BACKEND', '').endswith('console.EmailBackend')
        context['simulated_reset_link'] = self.request.session.get('simulated_reset_link', '')
        return context

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['simulation_enabled'] = getattr(settings, 'EMAIL_BACKEND', '').endswith('console.EmailBackend')
        uidb64 = self.kwargs.get('uidb64')
        token = self.kwargs.get('token')
        if uidb64 and token:
            context['simulated_reset_link'] = self.request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
            )
        else:
            context['simulated_reset_link'] = ''
        return context

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

# --------------------------
# Vistas auxiliares y de búsqueda
# --------------------------

from django.db.models import Count

# Búsqueda de tips por palabra clave
def search_tips(request):
    """
    Permite buscar tips por contenido o autor.
    """
    query = request.GET.get('q', '')
    tips = Tip.objects.all()
    if query:
        tips = tips.filter(
            Q(content__icontains=query) |
            Q(author__username__icontains=query)
        )
    return render(request, 'tips/search_results.html', {'tips': tips, 'query': query})

# Vista para mostrar el ranking de usuarios por reputación
def user_ranking(request):
    """
    Muestra el ranking de usuarios por reputación.
    """
    users = CustomUser.objects.all().order_by('-reputation')
    return render(request, 'tips/user_ranking.html', {'users': users})

# Vista para mostrar el historial de votos de un usuario (opcional)
@login_required
def vote_history(request):
    """
    Muestra el historial de votos realizados por el usuario.
    """
    user = request.user
    upvoted_tips = Tip.objects.filter(upvotes=user)
    downvoted_tips = Tip.objects.filter(downvotes=user)
    return render(request, 'tips/vote_history.html', {
        'upvoted_tips': upvoted_tips,
        'downvoted_tips': downvoted_tips,
    })

# Vista para mostrar detalles de reputación de un usuario (opcional)
def user_reputation_detail(request, user_id):
    """
    Muestra el detalle de la reputación de un usuario.
    """
    user = get_object_or_404(CustomUser, id=user_id)
    tips = Tip.objects.filter(author=user)
    return render(request, 'tips/user_reputation_detail.html', {'profile_user': user, 'tips': tips})

# Vista para mostrar todos los tips de un usuario
def user_tips(request, user_id):
    """
    Muestra todos los tips de un usuario específico.
    """
    user = get_object_or_404(CustomUser, id=user_id)
    tips = Tip.objects.filter(author=user)
    return render(request, 'tips/user_tips.html', {'profile_user': user, 'tips': tips})

# Vista para mostrar estadísticas generales (opcional)
def stats(request):
    """
    Muestra estadísticas generales del sistema.
    """
    total_users = CustomUser.objects.count()
    total_tips = Tip.objects.count()
    total_upvotes = sum(tip.upvotes.count() for tip in Tip.objects.all())
    total_downvotes = sum(tip.downvotes.count() for tip in Tip.objects.all())
    return render(request, 'tips/stats.html', {
        'total_users': total_users,
        'total_tips': total_tips,
        'total_upvotes': total_upvotes,
        'total_downvotes': total_downvotes,
    })

@login_required
def stats(request):
    """
    Vista que muestra estadísticas generales del sistema Life Pro Tips.

    Calcula y presenta:
        - Total de usuarios registrados.
        - Total de tips publicados.
        - Total de votos (upvotes + downvotes).
        - Reputación media de los usuarios.
        - Usuario más activo (con más tips publicados) y su cantidad de tips.

    Renderiza el template 'tips/stats.html' con el contexto de estadísticas.
    """
    total_users = CustomUser.objects.count()
    total_tips = Tip.objects.count()
    total_votes = sum(t.upvotes.count() + t.downvotes.count() for t in Tip.objects.all())
    avg_reputation = CustomUser.objects.aggregate(Avg('reputation'))['reputation__avg'] or 0

    # Usuario con más tips publicados
    most_active = CustomUser.objects.annotate(num_tips=Count('tips')).order_by('-num_tips').first()
    most_active_user = most_active if most_active and most_active.num_tips > 0 else None
    most_active_user_tip_count = most_active.num_tips if most_active_user else 0

    context = {
        'total_users': total_users,
        'total_tips': total_tips,
        'total_votes': total_votes,
        'avg_reputation': avg_reputation,
        'most_active_user': most_active_user,
        'most_active_user_tip_count': most_active_user_tip_count,
    }
    return render(request, 'tips/stats.html', context)

@login_required
def vote_history(request):
    """
    Muestra el historial de votos (upvotes y downvotes) realizados por el usuario.
    """
    # Suponiendo que tienes un modelo Vote con campos: user, tip, type ('upvote'/'downvote'), date
    votes = Vote.objects.filter(user=request.user).select_related('tip', 'tip__author').order_by('-date')
    return render(request, 'tips/vote_history.html', {'votes': votes})

# --------------------------
# Vistas administrativas y utilidades extra
# --------------------------

from django.contrib.admin.views.decorators import staff_member_required

# Vista para panel de administración personalizado (opcional)
@staff_member_required
def admin_dashboard(request):
    """
    Panel de administración personalizado para ver estadísticas rápidas.
    """
    total_users = CustomUser.objects.count()
    total_tips = Tip.objects.count()
    total_upvotes = sum(tip.upvotes.count() for tip in Tip.objects.all())
    total_downvotes = sum(tip.downvotes.count() for tip in Tip.objects.all())
    return render(request, 'admin/dashboard.html', {
        'total_users': total_users,
        'total_tips': total_tips,
        'total_upvotes': total_upvotes,
        'total_downvotes': total_downvotes,
    })

# Vista para activar/desactivar usuarios (requiere permisos de staff)
@staff_member_required
def toggle_user_active(request, user_id):
    """
    Activa o desactiva un usuario desde el panel de administración.
    """
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_active = not user.is_active
    user.save()
    messages.success(request, f"User '{user.username}' active status changed.")
    return redirect('user_ranking')

# Vista para resetear la reputación de todos los usuarios (requiere permisos de staff)
@staff_member_required
def reset_all_reputations(request):
    """
    Resetea la reputación de todos los usuarios a 0.
    """
    CustomUser.objects.all().update(reputation=0)
    messages.success(request, "All user reputations have been reset to 0.")
    return redirect('admin_dashboard')

# Vista para exportar tips a CSV (requiere permisos de staff)
import csv
from django.http import StreamingHttpResponse

@staff_member_required
def export_tips_csv(request):
    """
    Exporta todos los tips a un archivo CSV.
    """
    tips = Tip.objects.all()
    response = StreamingHttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="tips.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['ID', 'Author', 'Content', 'Created At', 'Upvotes', 'Downvotes'])
    for tip in tips:
        writer.writerow([
            tip.id,
            tip.author.username,
            tip.content,
            tip.created_at.strftime('%Y-%m-%d %H:%M'),
            tip.upvotes.count(),
            tip.downvotes.count()
        ])
    return response

# Vista para mostrar logs del sistema (opcional, requiere permisos de staff)
@staff_member_required
def view_logs(request):
    """
    Muestra los logs del sistema (requiere configuración de logging).
    """
    import os
    log_path = os.path.join(settings.BASE_DIR, 'logs', 'lifetips.log')
    logs = []
    if os.path.exists(log_path):
        with open(log_path, 'r') as f:
            logs = f.readlines()[-100:]  # Solo las últimas 100 líneas
    return render(request, 'admin/logs.html', {'logs': logs})

# Vista de mantenimiento (opcional)
def maintenance(request):
    """
    Página de mantenimiento temporal.
    """
    return render(request, 'maintenance.html')



