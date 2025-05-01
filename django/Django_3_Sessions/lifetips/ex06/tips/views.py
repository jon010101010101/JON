from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from .models import Tip, CustomUser
from .forms import TipForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Vista para la página de inicio (Home)
def home(request):
    try:
        tips = Tip.objects.select_related('author').all()
    except Exception as e:
        tips = []  # Si ocurre un error, se pasa una lista vacía
        messages.error(request, f"An error occurred while loading tips: {str(e)}")

    return render(request, 'home.html', {'tips': tips})


# Vista para el inicio de sesión (Login)
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


# Vista para el registro de usuarios (Register)
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created successfully.')
            return redirect('home')
        else:
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
                messages.success(request, 'Tip created successfully!')
                return redirect('home')
            except Exception as e:
                messages.error(request, f"An error occurred while creating the tip: {str(e)}")
        else:
            messages.error(request, 'Form is invalid. Please correct the errors.')
    else:
        form = TipForm()
    return render(request, 'create_tip.html', {'form': form})


# Vista para votar por un tip (Vote Tip)
@login_required
def vote_tip(request, tip_id, vote_type):
    try:
        tip = get_object_or_404(Tip, id=tip_id)
        if vote_type == 'upvote':
            tip.upvote(request.user)
            messages.success(request, "You have upvoted the tip.")
        elif vote_type == 'downvote':
            if not request.user.has_perm('tips.can_downvote_tip') and request.user != tip.author:
                raise PermissionDenied("You do not have permission to downvote this tip.")
            tip.downvote(request.user)
            messages.success(request, "You have downvoted the tip.")
        else:
            messages.error(request, "Invalid vote type.")
    except PermissionDenied as pd:
        messages.error(request, f"Permission error: {str(pd)}")
    except Exception as e:
        messages.error(request, f"An error occurred while voting: {str(e)}")
    return redirect('home')


# Vista para eliminar un tip (Delete Tip)
@login_required
def delete_tip(request, tip_id):
    try:
        tip = get_object_or_404(Tip, id=tip_id)
        if request.user != tip.author and not request.user.has_perm('tips.can_delete_tip'):
            raise PermissionDenied("You don't have permission to delete this tip.")

        tip.delete()
        messages.success(request, "The tip has been deleted successfully.")
    except PermissionDenied as pd:
        messages.error(request, f"Permission error: {str(pd)}")
    except Exception as e:
        messages.error(request, f"An error occurred while deleting the tip: {str(e)}")

    return redirect('home')


# Vista para listar todos los tips
def tips_list(request):
    try:
        tips = Tip.objects.all()  # Obtén todos los tips
    except Exception as e:
        tips = []  # Si ocurre un error, se pasa una lista vacía
        messages.error(request, f"An error occurred while loading the tips list: {str(e)}")

    return render(request, 'tips/tips_list.html', {'tips': tips})


# Vista para recuperación de contraseñas (Password Reset)
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                try:
                    for user in associated_users:
                        send_mail(
                            subject="Password Reset Requested",
                            message="Click the link below to reset your password.",
                            from_email=None,
                            recipient_list=[user.email]
                        )
                    messages.success(request, "An email has been sent with instructions to reset your password.")
                    return redirect('login')
                except Exception as e:
                    messages.error(request, f"Failed to send email: {str(e)}")
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})


# Vista personalizada para errores 404 (Página no encontrada)
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


# Clase personalizada para recuperación de contraseñas
class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.txt'  # Para texto plano
    html_email_template_name = 'registration/password_reset_email.html'  # Para HTML
    subject_template_name = 'registration/password_reset_subject.txt'  # Asunto del correo

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