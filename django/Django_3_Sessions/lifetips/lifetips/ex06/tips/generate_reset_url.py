import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ex06.settings")
django.setup()

from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse

User = get_user_model()

username = input("Introduce el username del usuario: ")
try:
    user = User.objects.get(username=username)
except User.DoesNotExist:
    print("¡Ese usuario no existe!")
    exit(1)

uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
from tips.views import token_generator  # Usa tu generador personalizado
token = token_generator.make_token(user)
reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})

print("UIDB64:", uidb64)
print("Token:", token)
print("Reset URL (solo path):", reset_url)
print("Reset URL completa (ajusta el dominio):")
print(f"http://127.0.0.1:8000{reset_url}")


# python generate_reset_url.py
