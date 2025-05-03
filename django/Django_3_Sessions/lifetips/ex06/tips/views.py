from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model  # Cambio aquí
from django.contrib.auth.views import PasswordResetView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.http import HttpResponse
from .models import Tip, CustomUser
from .forms import TipForm, CustomUserCreationForm
from django.utils.timezone import now

# Usar el modelo de usuario personalizado
User = get_user_model()  # Cambio aquí

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
    users = User.objects.all().order_by('-reputation')  # Cambio aquí
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
        for user in form.get_users(form.cleaned_data["email"]):
            # Actualizar el campo para forzar un nuevo token
            user.last_password_reset_request = now()
            user.save()

            # Generar un nuevo token para el usuario
            token = default_token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"http://127.0.0.1:8000/reset/{uidb64}/{token}/"

            # Enviar el correo con el enlace generado
            self.send_reset_email(user, reset_link)

        messages.success(self.request, "Si el email existe, se ha enviado un correo de recuperación.")
        return redirect('password_reset_done')

    def send_reset_email(self, user, reset_link):
        subject = "Reset your password"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = user.email
        text_content = f"Use this link to reset your password: {reset_link}"
        html_content = f"<p>Use this link to reset your password:</p><p><a href='{reset_link}'>{reset_link}</a></p>"

        try:
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except Exception as e:
            messages.error(self.request, f"Failed to send email: {str(e)}")


# Vista personalizada para manejar el restablecimiento de contraseñas
def reset_password(request, uidb64, token):
    try:
        # Decodificar el UID y obtener el usuario
        user_id = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=user_id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return HttpResponse("El enlace no es válido o ha expirado.", status=400)

    # Validar el token
    if not default_token_generator.check_token(user, token):
        return HttpResponse("El enlace no es válido o ha expirado.", status=400)

    # Lógica de restablecimiento de contraseña
    if request.method == 'POST':
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if new_password1 != new_password2:
            return HttpResponse("Las contraseñas no coinciden.", status=400)

        user.set_password(new_password1)
        user.save()
        return redirect('password_reset_complete')

    return render(request, 'registration/password_reset_confirm.html', {'uidb64': uidb64, 'token': token})