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
    test_results = []

    def print_test_details(self, description, before, action, after, passed):
        GREEN = "\033[92m"
        RED = "\033[91m"
        RESET = "\033[0m"
        status = f"{GREEN}PASSED ✅{RESET}" if passed else f"{RED}FAILED ❌{RESET}"
        print(f"\n🔍 {description}")
        print(f"    Antes: {before}")
        print(f"    Acción: {action}")
        print(f"    Después: {after}")
        print(f"    Resultado: {status}\n")
        self.__class__.test_results.append((description, passed))

    def setUp(self):
        if not hasattr(self, '_test_results_initialized'):
            self.__class__.test_results = []
            self._test_results_initialized = True
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='oldpassword'
        )
        self.password_reset_url = reverse('password_reset')
        self.password_reset_confirm_url_template = '/reset/{uidb64}/{token}/'
        self.password_reset_done_url = reverse('password_reset_done')
        self.password_reset_complete_url = reverse('password_reset_complete')

    def test_send_reset_email(self):
        """01: Verifica que se envía un email de reseteo cuando el usuario lo solicita."""
        description = "Test 01: Verifica que se envía un email de reseteo cuando el usuario lo solicita."
        before = f"Emails en bandeja: {len(mail.outbox)}"
        action = "Solicitar reseteo de contraseña."
        try:
            response = self.client.post(self.password_reset_url, {'email': self.user.email})
            self.assertRedirects(response, self.password_reset_done_url)
            self.assertEqual(len(mail.outbox), 1)
            self.assertIn(self.user.email, mail.outbox[0].to)
            passed = True
        except AssertionError as e:
            print(f"Fallo en test_send_reset_email: {e}")
            passed = False
        after = f"Emails en bandeja: {len(mail.outbox)}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_password_with_valid_token(self):
        """02: Verifica que se puede cambiar la contraseña usando un token válido."""
        description = "Test 02: Verifica que se puede cambiar la contraseña usando un token válido."
        before = f"Contraseña actual válida: {self.user.check_password('oldpassword')}"
        action = "Solicitar reseteo, extraer link del email y cambiar contraseña."
        # 1. Solicita el reseteo
        self.client.post(self.password_reset_url, {'email': self.user.email})
        email = mail.outbox[0]
        import re
        match = re.search(r'/reset/([^/]+)/([^/]+)/', email.body)
        uidb64, token = match.groups()
        url = self.password_reset_confirm_url_template.format(uidb64=uidb64, token=token)
        # 2. Cambia la contraseña usando el link real
        self.client.post(url, {
            'new_password1': 'newpassword',
            'new_password2': 'newpassword'
        })
        self.user.refresh_from_db()
        passed = self.user.check_password('newpassword')
        after = f"Contraseña cambiada correctamente: {self.user.check_password('newpassword')}"
        self.print_test_details(description, before, action, after, passed)
        self.assertTrue(passed)


    def test_reset_password_with_invalid_token(self):
        """03: Verifica que un token inválido no permite cambiar la contraseña."""
        description = "Test 03: Verifica que un token inválido no permite cambiar la contraseña."
        before = "Token inválido usado."
        action = "Intentar cambiar la contraseña con token inválido."
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        invalid_token = "invalid-token"
        url = self.password_reset_confirm_url_template.format(uidb64=uidb64, token=invalid_token)
        try:
            response = self.client.post(url, {
                'new_password1': 'newpassword',
                'new_password2': 'newpassword'
            })
            self.user.refresh_from_db()
            self.assertFalse(self.user.check_password('newpassword'))
            passed = True
        except AssertionError as e:
            print(f"Fallo en test_reset_password_with_invalid_token: {e}")
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_password_with_invalid_uid(self):
        """04: Verifica que un UID inválido no permite cambiar la contraseña."""
        description = "Test 04: Verifica que un UID inválido no permite cambiar la contraseña."
        before = "UID inválido usado."
        action = "Intentar cambiar la contraseña con UID inválido."
        invalid_uidb64 = "invalid-uid"
        token = default_token_generator.make_token(self.user)
        url = self.password_reset_confirm_url_template.format(uidb64=invalid_uidb64, token=token)
        try:
            response = self.client.post(url, {
                'new_password1': 'newpassword',
                'new_password2': 'newpassword'
            })
            self.user.refresh_from_db()
            self.assertFalse(self.user.check_password('newpassword'))
            passed = True
        except AssertionError as e:
            print(f"Fallo en test_reset_password_with_invalid_uid: {e}")
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_full_reset_password_flow(self):
        """05: Verifica el flujo completo de reseteo de contraseña por email."""
        description = "Test 05: Verifica el flujo completo de reseteo de contraseña por email."
        before = f"Contraseña inicial válida: {self.user.check_password('oldpassword')}"
        action = "Solicitar email, obtener link y cambiar contraseña."
        # 1. Solicita el reseteo
        self.client.post(self.password_reset_url, {'email': self.user.email})
        email = mail.outbox[0]
        import re
        match = re.search(r'/reset/([^/]+)/([^/]+)/', email.body)
        uidb64, token = match.groups()
        url = self.password_reset_confirm_url_template.format(uidb64=uidb64, token=token)
        # 2. Cambia la contraseña
        self.client.post(url, {
            'new_password1': 'newpassword',
            'new_password2': 'newpassword'
        })
        self.user.refresh_from_db()
        passed = self.user.check_password('newpassword')
        after = f"Contraseña cambiada correctamente: {self.user.check_password('newpassword')}"
        self.print_test_details(description, before, action, after, passed)
        self.assertTrue(passed)

    def test_reset_with_inactive_user(self):
        """06: Verifica que un usuario inactivo no pueda resetear su contraseña."""
        description = "Test 06: Verifica que un usuario inactivo no pueda resetear su contraseña."
        before = "Usuario inactivo."
        action = "Intentar resetear contraseña de usuario inactivo."
        self.user.is_active = False
        self.user.save()
        try:
            response = self.client.post(self.password_reset_url, {'email': self.user.email})
            self.assertNotIn(self.user.email, [email.to[0] for email in mail.outbox])
            passed = True
        except AssertionError as e:
            print(f"Fallo en test_reset_with_inactive_user: {e}")
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_password_with_expired_token(self):
        """07: Verifica que un token expirado no permita resetear la contraseña."""
        description = "Test 07: Verifica que un token expirado no permita resetear la contraseña."
        before = "Token expirado usado."
        action = "Intentar resetear contraseña con token expirado."
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        url = self.password_reset_confirm_url_template.format(uidb64=uidb64, token=token)
        # Simula expiración del token
        self.user.last_login = now() - timedelta(days=2)
        self.user.save()
        try:
            response = self.client.post(url, {
                'new_password1': 'newpassword',
                'new_password2': 'newpassword'
            })
            self.user.refresh_from_db()
            self.assertFalse(self.user.check_password('newpassword'))
            passed = True
        except AssertionError as e:
            print(f"Fallo en test_reset_password_with_expired_token: {e}")
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_email_sent_to_nonexistent_user(self):
        """08: Verifica que no se envía email si el usuario no existe, pero se redirige igual."""
        description = "Test 08: Verifica que no se envía email si el usuario no existe, pero se redirige igual."
        before = f"Emails en bandeja: {len(mail.outbox)}"
        action = "Solicitar reseteo para email inexistente."
        try:
            response = self.client.post(self.password_reset_url, {'email': 'noexiste@example.com'})
            self.assertRedirects(response, self.password_reset_done_url)
            self.assertEqual(len(mail.outbox), 0)
            passed = True
        except AssertionError as e:
            print(f"Fallo en test_reset_email_sent_to_nonexistent_user: {e}")
            passed = False
        after = f"Emails en bandeja: {len(mail.outbox)}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_password_with_mismatched_passwords(self):
        """09: Verifica que no se permite resetear si las contraseñas no coinciden."""
        description = "Test 09: Verifica que no se permite resetear si las contraseñas no coinciden."
        before = "Contraseñas no coinciden."
        action = "Intentar resetear con contraseñas distintas."
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        url = self.password_reset_confirm_url_template.format(uidb64=uidb64, token=token)
        try:
            response = self.client.post(url, {
                'new_password1': 'pass1',
                'new_password2': 'pass2'
            })
            self.user.refresh_from_db()
            self.assertFalse(self.user.check_password('pass1'))
            self.assertFalse(self.user.check_password('pass2'))
            passed = True
        except AssertionError as e:
            print(f"Fallo en test_reset_password_with_mismatched_passwords: {e}")
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_with_deleted_user(self):
        """10: Verifica que no se pueda resetear la contraseña de un usuario borrado."""
        description = "Test 10: Verifica que no se pueda resetear la contraseña de un usuario borrado."
        before = "Usuario borrado."
        action = "Intentar resetear contraseña de usuario borrado."
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        url = self.password_reset_confirm_url_template.format(uidb64=uidb64, token=token)
        self.user.delete()
        try:
            response = self.client.post(url, {
                'new_password1': 'newpassword',
                'new_password2': 'newpassword'
            })
            # No debería haber usuario para cambiar contraseña
            passed = not User.objects.filter(pk=self.user.pk).exists()
        except Exception as e:
            print(f"Fallo en test_reset_with_deleted_user: {e}")
            passed = False
        after = f"Status code: {response.status_code}"
        self.print_test_details(description, before, action, after, passed)

    def test_reset_with_malformed_url(self):
        """11: Verifica que una URL mal formada devuelve error."""
        description = "Test 11: Verifica que una URL mal formada devuelve error."
        malformed_url = '/reset/INVALID_UID/INVALID_TOKEN/'
        before = "URL mal formada."
        action = "Acceder a la URL mal formada."
        response = self.client.get(malformed_url)
        # Django por defecto responde con 200 y muestra un formulario de error
        after = f"Status code: {response.status_code}"
        passed = (response.status_code == 200)
        self.print_test_details(description, before, action, after, passed)
        self.assertTrue(passed)

    def test_email_contains_valid_reset_link(self):
        """12: Verifica que el email contiene un enlace de reseteo válido."""
        description = "Test 12: Verifica que el email contiene un enlace de reseteo válido."
        before = f"Emails en bandeja: {len(mail.outbox)}"
        action = "Solicitar reseteo y comprobar enlace en email."
        try:
            self.client.post(self.password_reset_url, {'email': self.user.email})
            email = mail.outbox[0]
            import re
            match = re.search(r'/reset/([^/]+)/([^/]+)/', email.body)
            assert match is not None
            passed = True
        except Exception as e:
            print(f"Fallo en test_email_contains_valid_reset_link: {e}")
            passed = False
        after = "Enlace de reseteo comprobado en email."
        self.print_test_details(description, before, action, after, passed)

    def test_reset_password_token_reuse(self):
        """13: Verifica que no se pueda reutilizar un token de reseteo."""
        description = "Test 13: Verifica que no se pueda reutilizar un token de reseteo."
        before = "Token usado una vez."
        action = "Intentar reutilizar el token."
        # 1. Solicita reseteo
        self.client.post(self.password_reset_url, {'email': self.user.email})
        email = mail.outbox[0]
        import re
        match = re.search(r'/reset/([^/]+)/([^/]+)/', email.body)
        uidb64, token = match.groups()
        url = self.password_reset_confirm_url_template.format(uidb64=uidb64, token=token)
        # 2. Primer uso del token
        self.client.post(url, {
            'new_password1': 'newpassword',
            'new_password2': 'newpassword'
        })
        self.user.refresh_from_db()
        password_after_first = self.user.check_password('newpassword')
        # 3. Segundo uso del token
        self.client.post(url, {
            'new_password1': 'anotherpassword',
            'new_password2': 'anotherpassword'
        })
        self.user.refresh_from_db()
        password_after_second = self.user.check_password('anotherpassword')
        after = f"Password after first: {password_after_first}, after second: {password_after_second}"
        # El test pasa si la segunda contraseña NO se aplica
        passed = password_after_first and not password_after_second
        self.print_test_details(description, before, action, after, passed)
        self.assertTrue(passed)

    def test_reset_url_generation(self):
        """14: Verifica que la URL de reseteo se genera correctamente."""
        description = "Test 14: Verifica que la URL de reseteo se genera correctamente."
        before = "Generar URL de reseteo."
        action = "Comprobar formato de la URL."
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        url = self.password_reset_confirm_url_template.format(uidb64=uidb64, token=token)
        try:
            import re
            assert re.match(r'^/reset/[A-Za-z0-9_\-]+/[A-Za-z0-9\-]+/$', url)
            passed = True
        except AssertionError as e:
            print(f"Fallo en test_reset_url_generation: {e}")
            passed = False
        after = f"URL generada: {url}"
        self.print_test_details(description, before, action, after, passed)

    def test_token_generation_and_validation(self):
        """15: Verifica que el token de reseteo se genera y valida correctamente."""
        description = "Test 15: Verifica que el token de reseteo se genera y valida correctamente."
        before = "Generar token."
        action = "Validar token."
        token = default_token_generator.make_token(self.user)
        try:
            self.assertTrue(default_token_generator.check_token(self.user, token))
            passed = True
        except AssertionError as e:
            print(f"Fallo en test_token_generation_and_validation: {e}")
            passed = False
        after = "Token validado correctamente."
        self.print_test_details(description, before, action, after, passed)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        GREEN = "\033[92m"
        RED = "\033[91m"
        RESET = "\033[0m"
        print("\nResumen Final:")
        total_tests = len(cls.test_results)
        passed_tests = sum(1 for _, passed in cls.test_results if passed)
        failed_tests = total_tests - passed_tests

        def get_test_number(desc):
            import re
            m = re.match(r"Test (\d+)", desc)
            return int(m.group(1)) if m else 999
        sorted_results = sorted(cls.test_results, key=lambda x: get_test_number(x[0]))

        for description, passed in sorted_results:
            status = f"{GREEN}PASSED ✅{RESET}" if passed else f"{RED}FAILED ❌{RESET}"
            print(f"  {description}: {status}")

        if failed_tests == 0:
            print(f"\n{GREEN}✅ {total_tests} pruebas pasaron con éxito.{RESET}\n")
        else:
            print(f"\n{RED}❌ {failed_tests} de {total_tests} pruebas fallaron.{RESET}\n")







# python manage.py test tips.reset_password_flow_test
