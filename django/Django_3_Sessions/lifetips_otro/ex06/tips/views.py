from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from .forms import TipForm, CustomUserCreationForm
from .models import Tip
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import PasswordResetView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Vista para la página de inicio (Home)
def home(request):
    tips = Tip.objects.select_related('author').all()  # Optimiza las consultas
    print("Tips for template:", tips)  # Diagnóstico
    try:
        return render(request, 'home.html', {'tips': tips})
    except Exception as e:
        print("Error rendering template:", str(e))  # Diagnóstico
        raise e

# Vista para el inicio de sesión (Login)
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            print("Form errors:", form.errors)  # Diagnóstico para revisar errores en consola
    return render(request, 'login.html', {'form': form})

# Vista para el registro de usuarios (Register)
def register(request):
    from .forms import CustomUserCreationForm  # Importación dentro de la función
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created successfully.')
            return redirect('home')
        else:
            messages.error(request, 'There was an error in your registration form. Please try again.')
            print("Form errors:", form.errors)  # Diagnóstico para revisar errores en consola
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
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            messages.success(request, 'Tip created successfully!')
            return redirect('home')
    else:
        form = TipForm()
    return render(request, 'create_tip.html', {'form': form})

# Vista para manejar los "upvotes" de un tip
@login_required
def upvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)

    # Si el usuario ya ha realizado un upvote, lo elimina
    if request.user in tip.upvotes.all():
        tip.upvotes.remove(request.user)
        tip.author.reputation -= 5
        messages.info(request, "You have removed your upvote.")
    else:
        # Agregar un nuevo upvote
        tip.upvotes.add(request.user)
        tip.author.reputation += 5
        messages.success(request, "You have upvoted the tip!")

        # Si el usuario ya había hecho un downvote, lo elimina
        if request.user in tip.downvotes.all():
            tip.downvotes.remove(request.user)
            tip.author.reputation += 2  # Recupera la reputación perdida
            messages.info(request, "Your previous downvote has been removed.")

    # Guardar los cambios en la reputación del autor
    tip.author.save()
    return redirect('home')

# Vista para manejar los "downvotes" de un tip
@login_required
def downvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)

    # Verificar si el usuario tiene suficiente reputación para downvote
    if not request.user.can_downvote():
        messages.error(request, "You don't have enough reputation to downvote.")
        return redirect('home')

    # Si el usuario ya ha realizado un downvote, lo elimina
    if request.user in tip.downvotes.all():
        tip.downvotes.remove(request.user)
        tip.author.reputation += 2
        messages.info(request, "You have removed your downvote.")
    else:
        # Agregar un nuevo downvote
        tip.downvotes.add(request.user)
        tip.author.reputation -= 2
        messages.success(request, "You have downvoted the tip!")

        # Si el usuario ya había hecho un upvote, lo elimina
        if request.user in tip.upvotes.all():
            tip.upvotes.remove(request.user)
            tip.author.reputation -= 5  # Restaura la reputación ganada por el upvote
            messages.info(request, "Your previous upvote has been removed.")

    # Guardar los cambios en la reputación del autor
    tip.author.save()
    return redirect('home')

# Vista para eliminar un tip
@login_required
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    if not request.user.can_delete_tips():
        raise PermissionDenied("You don't have permission to delete this tip.")  # Lanza excepción

    tip.delete()
    messages.success(request, "The tip has been deleted successfully.")
    return redirect('home')

# Vista para listar todos los tips
def tips_list(request):
    tips = Tip.objects.all()  # Obtén todos los tips
    return render(request, 'tips/tips_list.html', {'tips': tips})

# Vista para recuperación de contraseñas (Password Reset)
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    send_mail(
                        subject="Password Reset Requested",
                        message="Click the link below to reset your password.",
                        from_email=None,
                        recipient_list=[user.email]
                    )
                messages.success(request, "An email has been sent with instructions to reset your password.")
                return redirect('login')
            else:
                messages.error(request, "No user is associated with this email address.")
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})

# Vista personalizada para 404
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.txt'  # Para texto plano (opcional)
    html_email_template_name = 'registration/password_reset_email.html'  # Para HTML
    subject_template_name = 'registration/password_reset_subject.txt'  # Asunto del correo

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        # Agregar el dominio y protocolo al contexto
        context['protocol'] = 'https' if not settings.DEBUG else 'http'
        context['domain'] = settings.DOMAIN  # Define el dominio en settings.py o .env

        # Renderizar las plantillas para texto plano y HTML
        subject = render_to_string(subject_template_name, context).strip()
        text_content = render_to_string(email_template_name, context)
        html_content = render_to_string(html_email_template_name, context) if html_email_template_name else None

        # Enviar el correo
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            from_email,
            [to_email]
        )
        if html_content:
            msg.attach_alternative(html_content, "text/html")
        msg.send()