from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .models import Tip, CustomUser
from .forms import TipForm, CustomUserCreationForm


# Vista para la página de inicio (Home)
def home(request):
    try:
        tips = Tip.objects.select_related('author').all()
    except Exception as e:
        tips = []  # Si ocurre un error, se pasa una lista vacía
        messages.error(request, f"An error occurred while loading tips: {str(e)}")

    return render(request, 'home.html', {'tips': tips})


# Vista para iniciar sesión (Login)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Vista para registrar un usuario nuevo (Register)
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda al usuario
            # Especifica el backend de autenticación al iniciar sesión
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, f'Welcome, {user.username}! Your account has been created successfully.')
            return redirect('home')  # Redirige al home
        else:
            print(form.errors)  # Imprime los errores del formulario en la consola
            messages.error(request, 'There was an error in your registration form. Please try again.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


# Vista para cerrar sesión (Logout)
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')


# Vista para crear un nuevo tip (Create Tip)
@login_required
def create_tip(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            try:
                tip = form.save(commit=False)
                tip.author = request.user
                tip.save()
                # Agrega una etiqueta específica al mensaje
                messages.success(request, 'Tip created successfully!', extra_tags='tip_creation')
                return redirect('home')
            except Exception as e:
                messages.error(request, f"An error occurred while creating the tip: {str(e)}", extra_tags='tip_creation')
        else:
            messages.error(request, 'Form is invalid. Please correct the errors.', extra_tags='tip_creation')
    else:
        form = TipForm()
    return render(request, 'create_tip.html', {'form': form})


# Vista para manejar los votos positivos (Upvote)
@login_required
def upvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    try:
        tip.upvote(request.user)
        messages.success(request, 'You upvoted the tip!')
    except PermissionDenied as e:
        messages.error(request, str(e))
    return redirect('home')


# Vista para manejar los votos negativos (Downvote)
@login_required
def downvote_tip(request, tip_id):
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
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user != tip.author and not request.user.is_superuser:
        raise PermissionDenied("You don't have permission to delete this tip.")
    try:
        # Ajustar la reputación del autor eliminando la influencia de los votos
        upvotes_count = tip.upvotes.count()
        downvotes_count = tip.downvotes.count()
        tip.author.update_reputation(delta_upvotes=-upvotes_count, delta_downvotes=-downvotes_count)

        # Eliminar el tip
        tip.delete()
        messages.success(request, 'Tip deleted successfully.')
    except Exception as e:
        messages.error(request, f"An error occurred while deleting the tip: {str(e)}")
    return redirect('home')


# Vista para listar usuarios con email y reputación
@login_required
def users_list(request):
    users = CustomUser.objects.all().order_by('-reputation')
    return render(request, 'tips/users_list.html', {'users': users})


# Vista para listar todos los tips
def tips_list(request):
    try:
        tips = Tip.objects.all()
        # Asegurarse de que la reputación del autor esté actualizada
        for tip in tips:
            tip.author.update_reputation(delta_upvotes=tip.upvotes.count(), delta_downvotes=tip.downvotes.count())
    except Exception as e:
        tips = []
        messages.error(request, f"An error occurred while loading the tips list: {str(e)}")

    return render(request, 'tips/tips_list.html', {'tips': tips})


# Vista personalizada para errores 404 (Página no encontrada)
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


# Clase personalizada para recuperación de contraseñas con simulación y redirección automática
class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.txt'
    html_email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['simulation_enabled'] = True  # Asegúrate de pasar esta variable al contexto
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        # Obtener el usuario asociado al formulario
        user_email = form.cleaned_data.get('email')
        try:
            user = User.objects.get(email=user_email)

            # Generar el enlace de restablecimiento
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_url = self.request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )

            # Redirigir automáticamente al enlace generado
            return redirect(reset_url)
        except User.DoesNotExist:
            messages.error(self.request, "No user found with the provided email address.")
            return redirect('password_reset')

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        try:
            context['protocol'] = 'https' if not settings.DEBUG else 'http'
            context['domain'] = settings.DOMAIN

            subject = render_to_string(subject_template_name, context).strip()
            text_content = render_to_string(email_template_name, context)
            html_content = render_to_string(html_email_template_name, context) if html_email_template_name else None

            msg = EmailMultiAlternatives(
                subject,
                text_content,
                from_email,
                [to_email]
            )
            if html_content:
                msg.attach_alternative(html_content, "text/html")
            msg.send()
        except Exception as e:
            messages.error(context['request'], f"Failed to send email: {str(e)}")