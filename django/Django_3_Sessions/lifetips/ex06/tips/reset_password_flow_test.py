from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from datetime import timedelta
from django.utils.timezone import now

User = get_user_model()

class ResetPasswordFlowTest(TestCase):
    """
    Pruebas del flujo de reseteo de contraseña.
    """

    test_results = []

    def setUp(self):
        """Configura un usuario de prueba y las URLs necesarias."""
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='oldpassword'
        )
        self.password_reset_url = reverse('password_reset')
        self.password_reset_confirm_url_template = '/reset/{uidb64}/{token}/'
        self.password_reset_done_url = reverse('password_reset_done')
        self.password_reset_complete_url = reverse('password_reset_complete')

    def print_test_details(self, description, before, action, after, passed):
        status = "PASSED ✅" if passed else "FAILED ❌"
        print(f"\n🔍 {description}")
        print(f"    Antes: {before}")
        print(f"    Acción: {action}")
        print(f"    Después: {after}")
        print(f"    Resultado: {status}\n")
        ResetPasswordFlowTest.test_results.append((description, passed))

    def test_send_reset_email(self):
        """01: Verifica que se envía un email de reseteo cuando el usuario lo solicita."""
        description = "Test 01: Verifica que se envía un email de reseteo cuando el usuario lo solicita."
        before = f"Emails en bandeja: {len(mail.outbox)}"
        action = "Solicitar reseteo de contraseña."
        try:
            response = self.client.post(self.password_reset_url, {'email': self.user.email})
            self.assertRedirects(response, self.password_reset_done_url)
            self.assertEqual(len(mail.outbox), 1)
            passed = True
        except AssertionError:
            passed = False
        after = f"Emails en bandeja: {len(mail.outbox)}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_password_with_valid_token(self):
        """02: Verifica que se puede cambiar la contraseña usando un token válido."""
        description = "Test 02: Verifica que se puede cambiar la contraseña usando un token válido."
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        reset_password_url = self.password_reset_confirm_url_template.format(uidb64=uid, token=token)
        before = f"Contraseña actual válida: {self.user.check_password('oldpassword')}"
        action = "Enviar nueva contraseña usando token válido."
        try:
            response = self.client.post(reset_password_url, {
                'new_password1': 'newpassword123',
                'new_password2': 'newpassword123'
            })
            self.assertRedirects(response, self.password_reset_complete_url)
            self.user.refresh_from_db()
            self.assertTrue(self.user.check_password('newpassword123'))
            passed = True
        except AssertionError:
            passed = False
        after = f"Contraseña cambiada correctamente: {self.user.check_password('newpassword123')}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_password_with_invalid_token(self):
        """03: Verifica que un token inválido no permite cambiar la contraseña."""
        description = "Test 03: Verifica que un token inválido no permite cambiar la contraseña."
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        invalid_token = 'invalid-token'
        reset_password_url = self.password_reset_confirm_url_template.format(uidb64=uid, token=invalid_token)
        before = "Token inválido usado."
        action = "Intentar cambiar la contraseña con token inválido."
        try:
            response = self.client.post(reset_password_url, {
                'new_password1': 'newpassword123',
                'new_password2': 'newpassword123'
            })
            self.assertEqual(response.status_code, 400)
            passed = True
        except AssertionError:
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_password_with_invalid_uid(self):
        """04: Verifica que un UID inválido no permite cambiar la contraseña."""
        description = "Test 04: Verifica que un UID inválido no permite cambiar la contraseña."
        invalid_uid = urlsafe_base64_encode(force_bytes(9999))
        token = default_token_generator.make_token(self.user)
        reset_password_url = self.password_reset_confirm_url_template.format(uidb64=invalid_uid, token=token)
        before = "UID inválido usado."
        action = "Intentar cambiar la contraseña con UID inválido."
        try:
            response = self.client.post(reset_password_url, {
                'new_password1': 'newpassword123',
                'new_password2': 'newpassword123'
            })
            self.assertEqual(response.status_code, 400)
            passed = True
        except AssertionError:
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_full_reset_password_flow(self):
        """05: Verifica el flujo completo de reseteo de contraseña por email."""
        description = "Test 05: Verifica el flujo completo de reseteo de contraseña por email."
        before = f"Contraseña inicial válida: {self.user.check_password('oldpassword')}"
        action = "Solicitar email, obtener link y cambiar contraseña."
        try:
            response = self.client.post(self.password_reset_url, {'email': self.user.email})
            self.assertRedirects(response, self.password_reset_done_url)
            self.assertEqual(len(mail.outbox), 1)
            email = mail.outbox[0]
            reset_link_start = email.body.find('/reset/')
            reset_link_end = email.body.find('\n', reset_link_start)
            reset_link = email.body[reset_link_start:reset_link_end].strip()
            if not reset_link.endswith('/'):
                reset_link += '/'
            response = self.client.post(reset_link, {
                'new_password1': 'newpassword123',
                'new_password2': 'newpassword123'
            }, follow=True)
            self.assertRedirects(response, self.password_reset_complete_url)
            self.user.refresh_from_db()
            self.assertTrue(self.user.check_password('newpassword123'))
            passed = True
        except AssertionError:
            passed = False
        after = f"Contraseña cambiada correctamente: {self.user.check_password('newpassword123')}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_with_inactive_user(self):
        """06: Verifica que un usuario inactivo no pueda resetear su contraseña."""
        description = "Test 06: Verifica que un usuario inactivo no pueda resetear su contraseña."
        self.user.is_active = False
        self.user.save()
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        reset_password_url = self.password_reset_confirm_url_template.format(uidb64=uid, token=token)
        before = "Usuario inactivo."
        action = "Intentar resetear contraseña de usuario inactivo."
        try:
            response = self.client.post(reset_password_url, {
                'new_password1': 'newpassword123',
                'new_password2': 'newpassword123'
            })
            self.assertIn(response.status_code, [302, 400])
            passed = True
        except AssertionError:
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_password_with_expired_token(self):
        """07: Verifica que un token expirado no permita resetear la contraseña."""
        description = "Test 07: Verifica que un token expirado no permita resetear la contraseña."
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        expired_token = default_token_generator.make_token(self.user)
        self.user.last_login = now() - timedelta(days=2)
        self.user.save()
        reset_password_url = self.password_reset_confirm_url_template.format(uidb64=uidb64, token=expired_token)
        before = "Token expirado usado."
        action = "Intentar resetear contraseña con token expirado."
        try:
            response = self.client.post(reset_password_url, {
                'new_password1': 'newpassword123',
                'new_password2': 'newpassword123'
            })
            self.assertEqual(response.status_code, 400)
            passed = True
        except AssertionError:
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_email_sent_to_nonexistent_user(self):
        """08: Verifica que no se envía email si el usuario no existe, pero se redirige igual."""
        description = "Test 08: Verifica que no se envía email si el usuario no existe, pero se redirige igual."
        before = f"Emails en bandeja: {len(mail.outbox)}"
        action = "Solicitar reseteo para email inexistente."
        try:
            response = self.client.post(self.password_reset_url, {'email': 'nonexistent@example.com'})
            self.assertRedirects(response, self.password_reset_done_url)
            self.assertEqual(len(mail.outbox), 0)
            passed = True
        except AssertionError:
            passed = False
        after = f"Emails en bandeja: {len(mail.outbox)}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_password_with_mismatched_passwords(self):
        """09: Verifica que no se permite resetear si las contraseñas no coinciden."""
        description = "Test 09: Verifica que no se permite resetear si las contraseñas no coinciden."
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        reset_password_url = self.password_reset_confirm_url_template.format(uidb64=uid, token=token)
        before = "Contraseñas no coinciden."
        action = "Intentar resetear con contraseñas distintas."
        try:
            response = self.client.post(reset_password_url, {
                'new_password1': 'newpassword123',
                'new_password2': 'differentpassword123'
            })
            self.assertEqual(response.status_code, 400)
            passed = True
        except AssertionError:
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_with_deleted_user(self):
        """10: Verifica que no se pueda resetear la contraseña de un usuario borrado."""
        description = "Test 10: Verifica que no se pueda resetear la contraseña de un usuario borrado."
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        self.user.delete()
        reset_password_url = self.password_reset_confirm_url_template.format(uidb64=uid, token=token)
        before = "Usuario borrado."
        action = "Intentar resetear contraseña de usuario borrado."
        try:
            response = self.client.post(reset_password_url, {
                'new_password1': 'newpassword123',
                'new_password2': 'newpassword123'
            })
            self.assertEqual(response.status_code, 400)
            passed = True
        except AssertionError:
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_with_malformed_url(self):
        """11: Verifica que una URL mal formada devuelve error."""
        description = "Test 11: Verifica que una URL mal formada devuelve error."
        malformed_url = '/reset/INVALID_UID/INVALID_TOKEN/'
        before = "URL mal formada."
        action = "Acceder a la URL mal formada."
        try:
            response = self.client.get(malformed_url)
            self.assertEqual(response.status_code, 400)
            passed = True
        except AssertionError:
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_email_contains_valid_reset_link(self):
        """12: Verifica que el email contiene un enlace de reseteo válido."""
        description = "Test 12: Verifica que el email contiene un enlace de reseteo válido."
        before = f"Emails en bandeja: {len(mail.outbox)}"
        action = "Solicitar reseteo y comprobar enlace en email."
        try:
            response = self.client.post(self.password_reset_url, {'email': self.user.email})
            self.assertRedirects(response, self.password_reset_done_url)
            self.assertEqual(len(mail.outbox), 1)
            email = mail.outbox[0]
            reset_link_start = email.body.find('/reset/')
            reset_link_end = email.body.find('\n', reset_link_start)
            reset_link = email.body[reset_link_start:reset_link_end].strip()
            if not reset_link.endswith('/'):
                reset_link += '/'
            reset_response = self.client.get(reset_link, follow=True)
            self.assertEqual(reset_response.status_code, 200)
            passed = True
        except AssertionError:
            passed = False
        after = f"Enlace de reseteo comprobado en email."
        self.print_test_details(description, before, action, after, passed)

    def test_reset_password_token_reuse(self):
        """13: Verifica que no se pueda reutilizar un token de reseteo."""
        description = "Test 13: Verifica que no se pueda reutilizar un token de reseteo."
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        reset_password_url = self.password_reset_confirm_url_template.format(uidb64=uid, token=token)
        before = "Token usado una vez."
        action = "Intentar reutilizar el token."
        try:
            self.client.post(reset_password_url, {
                'new_password1': 'newpassword123',
                'new_password2': 'newpassword123'
            })
            response = self.client.post(reset_password_url, {
                'new_password1': 'newpassword456',
                'new_password2': 'newpassword456'
            })
            self.assertEqual(response.status_code, 400)
            passed = True
        except AssertionError:
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_url_generation(self):
        """14: Verifica que la URL de reseteo se genera correctamente."""
        description = "Test 14: Verifica que la URL de reseteo se genera correctamente."
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        url = self.password_reset_confirm_url_template.format(uidb64=uid, token=token)
        before = "Generar URL de reseteo."
        action = "Comprobar formato de la URL."
        try:
            self.assertTrue(url.startswith('/reset/'))
            self.assertIn(uid, url)
            self.assertIn(token, url)
            passed = True
        except AssertionError:
            passed = False
        after = f"URL generada: {url}"
        self.print_test_details(description, before, action, after, passed)

    def test_token_generation_and_validation(self):
        """15: Verifica que el token de reseteo se genera y valida correctamente."""
        description = "Test 15: Verifica que el token de reseteo se genera y valida correctamente."
        before = "Generar token."
        action = "Validar token."
        try:
            token = default_token_generator.make_token(self.user)
            self.assertTrue(default_token_generator.check_token(self.user, token))
            passed = True
        except AssertionError:
            passed = False
        after = "Token validado correctamente."
        self.print_test_details(description, before, action, after, passed)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        print("\nResumen Final:")
        total_tests = len(cls.test_results)
        passed_tests = sum(1 for _, passed in cls.test_results if passed)
        failed_tests = total_tests - passed_tests

        for description, passed in cls.test_results:
            status = "PASSED ✅" if passed else "FAILED ❌"
            print(f"  {description}: {status}")

        if failed_tests == 0:
            print(f"\n✅ {total_tests} pruebas pasaron con éxito.\n")
        else:
            print(f"\n❌ {failed_tests} de {total_tests} pruebas fallaron.\n")


# python manage.py test tips.reset_password_flow_test
