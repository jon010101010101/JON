import os
import logging
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
    PasswordResetForm,
)
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseForbidden
from django.db.models import Count, Q
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.utils.timezone import now
from .models import Tip, CustomUser
from .forms import TipForm, CustomUserCreationForm
from django.utils.http import urlsafe_base64_decode
from .forms import CustomPasswordResetForm


logger = logging.getLogger(__name__)

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

# Vista de edición de perfil
@login_required
def profile_edit(request):
    if request.method == 'POST':
        user = request.user
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        if new_username:
            user.username = new_username
        if new_email:
            user.email = new_email
        user.save()
        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('profile_edit')
    return render(request, 'profile_edit.html')

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
    user = request.user
    try:
        tip.upvote(user)
        messages.success(request, 'You have upvoted this tip!')
    except PermissionDenied as e:
        messages.error(request, str(e))
    return redirect('home')

@login_required
def downvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    user = request.user

    # Only allow downvote if user has permission (15+ rep or is superuser)
    if not user.can_downvote and not user.is_superuser:
        messages.error(request, "You need at least 15 reputation points to downvote tips.")
        return redirect('home')

    try:
        tip.downvote(user)
        messages.success(request, 'You have downvoted this tip!')
    except PermissionDenied as e:
        messages.error(request, str(e))
    return redirect('home')


@login_required
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    user = request.user

    # Permitir que el superusuario borre cualquier tip
    if not user.is_superuser and tip.author != user:
        raise PermissionDenied("You don't have permission to delete this tip.")

    try:
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
    template_name = 'registration/password_reset.html'
    form_class = CustomPasswordResetForm
    email_template_name = 'registration/password_reset_email.txt'
    html_email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = '/tips/password_reset_done/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        action = request.POST.get('action')

        if not form.is_valid():
            # Si hay errores de validación, los muestra en el template
            print("Errores del formulario:", form.errors)
            return self.render_to_response(self.get_context_data(form=form))

        email = form.cleaned_data['email']
        user = User.objects.get(email=email)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_link = request.build_absolute_uri(
            reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
        )

        if action == 'real':
            # Usa el flujo estándar de Django para enviar el email real
            return super().post(request, *args, **kwargs)
        elif action == 'simulado':
            # Genera el email simulado y lo muestra en el template
            context = self.get_context_data(form=form)
            context['simulated_email'] = {
                'to': user.email,
                'reset_link': reset_link,
                'username': user.username,
            }
            return self.render_to_response(context)
        else:
            # Por defecto, vuelve a mostrar el formulario
            return self.render_to_response(self.get_context_data(form=form))


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

def custom_password_reset(request):
    simulated_reset_url = None
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=False,
                email_template_name="registration/password_reset_email.html",
            )
            # Solo para desarrollo: extraer el enlace del email en consola
            if settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend':
                # No se puede extraer automáticamente de la consola,
                # pero puedes mostrar un mensaje indicando que revises la consola.
                simulated_reset_url = "Consulta la consola para ver el enlace de restablecimiento."
            # Si usas filebased backend, puedes extraer el enlace del archivo:
            elif settings.EMAIL_BACKEND == 'django.core.mail.backends.filebased.EmailBackend':
                import glob
                files = sorted(
                    glob.glob(os.path.join(settings.EMAIL_FILE_PATH, '*')),
                    key=os.path.getmtime
                )
                if files:
                    with open(files[-1]) as f:
                        for line in f:
                            if '/reset/' in line:
                                simulated_reset_url = line.strip()
                                break
            return render(request, "registration/password_reset_done.html", {
                "simulated_reset_url": simulated_reset_url,
            })
    else:
        form = PasswordResetForm()
    return render(request, "registration/password_reset.html", {
        "form": form,
    })