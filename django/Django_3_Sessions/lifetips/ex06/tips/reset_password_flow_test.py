from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.http import HttpResponse
from django.utils.encoding import force_bytes


# Función para enviar un correo de restablecimiento de contraseña
def send_reset_email(request, user_email):
    try:
        user = User.objects.get(email=user_email)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_link = f"http://127.0.0.1:8000/reset/{uid}/{token}/"

        send_mail(
            subject='Restablece tu contraseña - Life Pro Tips',
            html_message=f"""
            <html>
            <body>
                <p>Haz clic en el botón para restablecer tu contraseña:</p>
                <a href="{reset_link}">Restablecer Contraseña</a>
            </body>
            </html>
            """,
            from_email='lifetipsdjango@gmail.com',
            recipient_list=[user_email],
            fail_silently=False,
        )
        return HttpResponse(f"Correo enviado a {user_email}")
    except User.DoesNotExist:
        return HttpResponse("Usuario no encontrado", status=404)


# Clase de pruebas para el flujo de restablecimiento de contraseña
class ResetPasswordFlowTest(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='oldpassword'
        )
        self.reset_email_url = reverse('send_reset_email', args=[self.user.email])
        self.reset_password_url_template = '/reset/{uidb64}/{token}/'

    def test_send_reset_email(self):
        # Enviar solicitud de restablecimiento de contraseña
        response = self.client.get(self.reset_email_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            f"Se ha enviado un correo a <strong>{self.user.email}</strong>",
            response.content.decode()
        )

    def test_reset_password_with_valid_token(self):
        # Generar un uid y un token válidos
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)

        # Enviar solicitud POST con nueva contraseña
        reset_password_url = self.reset_password_url_template.format(uidb64=uid, token=token)
        response = self.client.post(reset_password_url, {
            'new_password': 'newpassword123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Contraseña restablecida correctamente.")

        # Verificar que la contraseña se haya actualizado
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpassword123'))

    def test_reset_password_with_invalid_token(self):
        # Generar un uid válido pero un token inválido
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        invalid_token = 'invalid-token'

        # Intentar restablecer la contraseña con un token inválido
        reset_password_url = self.reset_password_url_template.format(uidb64=uid, token=invalid_token)
        response = self.client.post(reset_password_url, {
            'new_password': 'newpassword123'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "El enlace no es válido o ha expirado.")

    def test_reset_password_with_invalid_uid(self):
        # Generar un uid inválido y un token válido
        invalid_uid = urlsafe_base64_encode(force_bytes(9999))  # ID de usuario no existente
        token = default_token_generator.make_token(self.user)

        # Intentar restablecer la contraseña con un uid inválido
        reset_password_url = self.reset_password_url_template.format(uidb64=invalid_uid, token=token)
        response = self.client.post(reset_password_url, {
            'new_password': 'newpassword123'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "Algo salió mal al restablecer la contraseña.")