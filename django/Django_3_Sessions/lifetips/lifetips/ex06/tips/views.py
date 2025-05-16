import os
import logging
import random
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import (
    authenticate, login, logout, update_session_auth_hash, get_user_model
)
from django.contrib.auth.forms import (
    PasswordChangeForm, PasswordResetForm,
)
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.utils.timezone import now
from .models import Tip, CustomUser
from .forms import CustomPasswordResetForm, CustomAuthenticationForm, TipForm, RegisterForm

User = get_user_model()


def recalculate_all_reputations():
    for user in CustomUser.objects.all():
        tips = Tip.objects.filter(author=user)
        upvotes = sum(tip.upvotes.count() for tip in tips)
        downvotes = sum(tip.downvotes.count() for tip in tips)
        user.reputation = upvotes * 5 - downvotes * 2
        user.save(update_fields=['reputation'])

def home(request):
    recalculate_all_reputations()
    tips = Tip.objects.select_related('author').all()
    context = {
        'tips': tips,
        'anon_name': get_anonymous_username(request) if not request.user.is_authenticated else None
    }
    return render(request, 'ex06/home.html', context)

@login_required
def users_list(request):
    recalculate_all_reputations()
    users = CustomUser.objects.all().order_by('-reputation')
    return render(request, 'tips/users_list.html', {'users': users})

@login_required
def tips_list(request):
    recalculate_all_reputations()
    tips = Tip.objects.all()
    return render(request, 'tips/tips_list.html', {'tips': tips})

def get_anonymous_username(request):
    import time
    chapchap_enabled = getattr(settings, 'CHAPCHAP_ENABLED', True)
    chapchap_names = getattr(settings, 'CHAPCHAP_NAMES', [
         'Alfa', 'Beta', 'Gamma', 'Delta', 'Épsilon',
        'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa'
    ])
    if not chapchap_enabled:
        return None
    now = int(time.time())
    chapchap = request.session.get('chapchap')
    chapchap_time = request.session.get('chapchap_time')
    if not chapchap or not chapchap_time or now - chapchap_time > 42:
        chapchap = random.choice(chapchap_names)
        request.session['chapchap'] = chapchap
        request.session['chapchap_time'] = now
    return chapchap

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
        messages.success(request, "Profile updated successfully.")
        return redirect('profile_edit')
    return render(request, 'profile_edit.html')

def login_view(request):
    failed_attempts = request.session.get('failed_login_attempts', 0)
    show_captcha = getattr(settings, 'CAPTCHA_ENABLED', False)
    error = None

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST, show_captcha=show_captcha)
        if form.is_valid():
            request.session['failed_login_attempts'] = 0
            user = form.get_user()
            if user.is_superuser:
                code = f"{random.randint(100000, 999999)}"
                request.session['2fa_code'] = code
                request.session['2fa_user_id'] = user.id
                send_mail(
                    subject='Your 2FA Code',
                    message=f'Your Life Pro Tips 2FA code is: {code}',
                    from_email='noreply@lifeprotips.com',
                    recipient_list=[user.email],
                )
                return redirect('verify_2fa')
            else:
                login(request, user)
                return redirect('home')
        else:
            request.session['failed_login_attempts'] = failed_attempts + 1
            if form.errors:
                for field in ['username', 'password', 'captcha']:
                    if field in form.errors:
                        error = form.errors[field][0]
                        break
                if not error and form.non_field_errors():
                    error = form.non_field_errors()[0]
            else:
                error = "There was an error. Please try again."
    else:
        form = CustomAuthenticationForm(request, show_captcha=show_captcha)

    return render(request, 'login.html', {'form': form, 'error': error})

def register(request):
    error = None
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            if form.errors:
                for field in ['username', 'password', 'password_confirm', 'email']:
                    if field in form.errors:
                        error = form.errors[field][0]
                        break
                if not error and form.non_field_errors():
                    error = form.non_field_errors()[0]
            else:
                error = "There was an error. Please try again."
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

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
            messages.error(request, 'Form is invalid. Please correct the errors.')
    else:
        form = TipForm()
    return render(request, 'create_tip.html', {'form': form})

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
    if not user.can_downvote and not user.is_superuser and tip.author != user:
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
    if not (user.is_superuser or tip.author == user or (hasattr(user, 'reputation') and user.reputation >= 30)):
        messages.error(request, "No tienes reputación suficiente para borrar este tip.")
        return redirect('home')
    try:
        tip.delete()
        messages.success(request, "Tip successfully erased.")
    except Exception as e:
        messages.error(request, f"An error occurred while deleting the tip: {str(e)}")
    return redirect('home')

def reset_password(request, uidb64, token):
    try:
        user_id = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=user_id)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        return HttpResponse("The link is invalid or has expired.", status=400)

    if not default_token_generator.check_token(user, token):
        return HttpResponse("The link is invalid or has expired.", status=400)

    if request.method == 'POST':
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        if new_password1 != new_password2:
            return HttpResponse("The passwords do not match.", status=400)

        user.set_password(new_password1)
        user.save()
        return redirect('password_reset_complete')

    return render(request, 'registration/password_reset_confirm.html', {'uidb64': uidb64, 'token': token})

def verify_2fa(request):
    error = None
    if request.method == 'POST':
        code = request.POST.get('code')
        if code == request.session.get('2fa_code'):
            user_id = request.session.get('2fa_user_id')
            user = get_object_or_404(get_user_model(), id=user_id)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            request.session.pop('2fa_code', None)
            request.session.pop('2fa_user_id', None)
            return redirect('home')
        else:
            error = "Invalid 2FA code."
    return render(request, 'verify_2fa.html', {'error': error})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile_edit')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

@login_required
def user_reputation_report(request):
    usuarios_info = []
    for user in User.objects.all():
        user_total = 0
        tips = Tip.objects.filter(author=user)
        tips_info = []
        for tip in tips:
            upvoters = tip.upvotes.all()
            downvoters = tip.downvotes.all()
            tip_score = 0
            for u in upvoters:
                tip_score += 5
            for u in downvoters:
                tip_score -= 2
            tips_info.append({
                "tip": tip,
                "upvoters": upvoters,
                "downvoters": downvoters,
                "score": tip_score,
            })
            user_total += tip_score
        permissions = []
        if user_total >= 30:
            permissions.append("Can downvote and delete")
        elif user_total >= 15:
            permissions.append("Can downvote")
        usuarios_info.append({
            "user": user,
            "tips_info": tips_info,
            "reputation": user_total,
            "permissions": permissions,
        })
    return render(request, 'tips/user_reputation_report.html', {'usuarios_info': usuarios_info})

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
            return self.render_to_response(self.get_context_data(form=form))
        email = form.cleaned_data['email']
        user = CustomUser.objects.get(email=email)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_link = request.build_absolute_uri(
            reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
        )
        if action == 'real':
            return super().post(request, *args, **kwargs)
        elif action == 'simulado':
            context = self.get_context_data(form=form)
            context['simulated_email'] = {
                'to': user.email,
                'reset_link': reset_link,
                'username': user.username,
            }
            return self.render_to_response(context)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        for user in form.get_users(form.cleaned_data["email"]):
            user.last_password_reset_request = now()
            user.save()
            token = default_token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"http://127.0.0.1:8000/reset/{uidb64}/{token}/"
            self.send_reset_email(user, reset_link)
        messages.success(self.request, "If the email exists, a recovery email has been sent.")
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

