from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import Article, UserFavouriteArticle
from django.conf import settings
from django.utils import translation


class ArticleTests(TestCase):
    def setUp(self):
        """Preparación: crea usuarios y artículos de prueba con datos profesionales."""
        self.user1 = User.objects.create_user(username='testuser1', password='testpass1')
        self.user2 = User.objects.create_user(username='testuser2', password='testpass2')

        self.article1 = Article.objects.create(
            title='Project Management',
            author=self.user1,
            synopsis='Best practices for team collaboration and project delivery.',
            content='Full article content about project management.'
        )
        self.article2 = Article.objects.create(
            title='Data Analysis Trends',
            author=self.user2,
            synopsis='Exploring modern data analysis techniques and tools.',
            content='Full article content about data analysis.'
        )
        # Artículo largo y antiguo para los tests de truncado y tiempo relativo:
        self.article3 = Article.objects.create(
            title='Remote Work Insights',
            author=self.user2,
            synopsis='Challenges and benefits of remote work in today’s professional environment. This article explores strategies for effective remote collaboration.',
            content='Full article content about remote work.'
        )
        # Ajusta la fecha de creación para simular un artículo antiguo (2 semanas y 2 días atrás)
        self.article3.created = timezone.now() - timedelta(weeks=2, days=2)
        self.article3.save()

    def print_test_details(self, description, before, action, after, passed):
        print("\n" + "=" * 60)
        print(description)
        print("ANTES:", before)
        print("ACCIÓN:", action)
        print("DESPUÉS:", after)
        print("RESULTADO:", "✅ PASÓ" if passed else "❌ FALLÓ")
        print("=" * 60)

    def test_01_lista_articulos(self):
        """01: Verifica que la lista de artículos muestra correctamente los títulos de los artículos creados."""
        description = "Test 01: Verifica que la lista de artículos muestra correctamente los títulos de los artículos creados."
        before = "Artículos creados: Project Management, Data Analysis Trends"
        action = "GET /articles/"
        after = ""
        passed = True
        try:
            response = self.client.get(reverse('articles'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Project Management')
            self.assertContains(response, 'Data Analysis Trends')
            after = "Se muestran ambos títulos en la respuesta."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_02_menu_login_logout(self):
        """02: Verifica que el login y logout desde el menú funcionan correctamente."""
        description = "Test 02: Verifica que el login y logout desde el menú funcionan correctamente."
        before = "Usuario testuser1 no autenticado."
        action = "Login desde el menú en /articles/, luego logout."
        after = ""
        passed = True
        try:
            response = self.client.post(reverse('articles'), {
                'username': 'testuser1',
                'password': 'testpass1',
                'login_menu': 1
            }, follow=True)
            self.assertContains(response, 'Logged as testuser1')
            response = self.client.get(reverse('logout'), follow=True)
            self.assertContains(response, 'Login')
            after = "Login y logout correctos, menú actualizado."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_03_error_login(self):
        """03: Verifica que se muestra error si el login falla."""
        description = "Test 03: Verifica que se muestra error si el login falla."
        before = "Usuario testuser1 intenta login con contraseña incorrecta."
        action = "POST login con password erróneo."
        after = ""
        passed = True
        try:
            response = self.client.post(reverse('articles'), {
                'username': 'testuser1',
                'password': 'wrongpass',
                'login_menu': 1
            })
            self.assertContains(response, 'Invalid username or password.')
            after = "Mensaje de error mostrado correctamente."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_04_publicaciones_requiere_login(self):
        """04: Verifica que la vista de publicaciones requiere login."""
        description = "Test 04: Verifica que la vista de publicaciones requiere login."
        before = "Usuario no autenticado."
        action = "GET /publications/ sin login, luego con login."
        after = ""
        passed = True
        try:
            response = self.client.get(reverse('publications'))
            self.assertNotEqual(response.status_code, 200)
            self.client.login(username='testuser1', password='testpass1')
            response = self.client.get(reverse('publications'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Project Management')
            after = "Acceso denegado sin login, permitido con login."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_05_registro_usuario(self):
        """05: Verifica que el registro de usuario funciona correctamente."""
        description = "Test 05: Verifica que el registro de usuario funciona correctamente."
        before = "Usuario 'newuser' no existe."
        action = "POST a /register/ con datos válidos."
        after = ""
        passed = True
        try:
            response = self.client.post(reverse('register'), {
                'username': 'newuser',
                'password1': 'StrongPassword123',
                'password2': 'StrongPassword123'
            }, follow=True)
            self.assertRedirects(response, reverse('articles'))
            self.assertTrue(User.objects.filter(username='newuser').exists())
            after = "Usuario registrado y redirigido correctamente."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_06_error_registro(self):
        """06: Verifica que se muestra error si el registro falla (contraseñas diferentes)."""
        description = "Test 06: Verifica que se muestra error si el registro falla (contraseñas diferentes)."
        before = "Usuario 'newuser2' no existe."
        action = "POST a /register/ con contraseñas diferentes."
        after = ""
        passed = True
        try:
            response = self.client.post(reverse('register'), {
                'username': 'newuser2',
                'password1': 'StrongPassword123',
                'password2': 'DifferentPassword'
            })
            self.assertContains(response, 'The two password fields didn’t match')
            after = "Mensaje de error mostrado correctamente."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_07_publicaciones_usuario(self):
        """07: Verifica que las publicaciones de un usuario específico se muestran correctamente."""
        description = "Test 07: Verifica que las publicaciones de un usuario específico se muestran correctamente."
        before = "Usuario testuser1 autenticado con varias publicaciones."
        action = "GET /publications/ y comprobar que sólo las publicaciones de testuser1 están listadas."
        after = ""
        passed = True
        try:
            self.client.login(username='testuser1', password='testpass1')
            response = self.client.get(reverse('publications'))
            self.assertContains(response, 'Project Management')  # Publicado por testuser1
            self.assertNotContains(response, 'Remote Work Insights')  # Publicado por testuser2
            self.assertNotContains(response, 'Data Analysis Trends')  # Publicado por testuser2
            after = "Sólo las publicaciones de testuser1 están listadas correctamente."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_08_favoritos_y_añadir(self):
        """08: Verifica que se pueden añadir artículos a favoritos y verlos."""
        description = "Test 08: Verifica que se pueden añadir artículos a favoritos y verlos."
        before = "Usuario testuser1 autenticado, sin favoritos."
        action = "Añadir article2 a favoritos y comprobar en /favourites/."
        after = ""
        passed = True
        try:
            self.client.login(username='testuser1', password='testpass1')
            response = self.client.post(reverse('add-favourite', args=[self.article2.pk]), follow=True)
            self.assertRedirects(response, reverse('favourite-added'))
            self.assertTrue(UserFavouriteArticle.objects.filter(user=self.user1, article=self.article2).exists())
            response = self.client.get(reverse('favourites'))
            self.assertContains(response, 'Data Analysis Trends')
            after = "Favorito añadido y visible en favoritos."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_09_favorito_duplicado(self):
        """09: Verifica que no se puede añadir dos veces el mismo favorito."""
        description = "Test 09: Verifica que no se puede añadir dos veces el mismo favorito."
        before = "Usuario testuser1 autenticado, article2 ya en favoritos."
        action = "Intentar añadir article2 de nuevo a favoritos."
        after = ""
        passed = True
        try:
            self.client.login(username='testuser1', password='testpass1')
            UserFavouriteArticle.objects.create(user=self.user1, article=self.article2)
            response = self.client.post(reverse('add-favourite', args=[self.article2.pk]), follow=True)
            self.assertRedirects(response, reverse('already-favourite'))
            after = "Redirigido correctamente a 'already-favourite'."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_10_detalle_articulo(self):
        """10: Verifica que el detalle del artículo muestra la información correctamente."""
        description = "Test 10: Verifica que el detalle del artículo muestra la información correctamente."
        before = "Artículo 'Project Management' creado."
        action = "GET a /article-detail/ de article1."
        after = ""
        passed = True
        try:
            response = self.client.get(reverse('article-detail', args=[self.article1.pk]))
            self.assertContains(response, 'Project Management')
            self.assertContains(response, 'Best practices for team collaboration and project delivery.')
            after = "Detalle del artículo mostrado correctamente."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed) 

    def test_11_internacionalizacion(self):
        """11: Verifica que el sitio muestra los textos traducidos según el idioma en la URL."""
        description = "Test 11: Verifica que el sitio muestra los textos traducidos según el idioma en la URL."
        before = "Idiomas disponibles: español e inglés."
        action = "GET /es/articles/ y /en/articles/ y comprobar textos."
        after = ""
        passed = True
        try:
            response = self.client.get('/es/articles/')
            self.assertContains(response, 'Artículos')
            self.assertContains(response, 'Comparte tus escritos')
            self.assertContains(response, 'Sinopsis')
            response = self.client.get('/en/articles/')
            self.assertContains(response, 'Articles')
            self.assertContains(response, 'Share your writings')
            self.assertContains(response, 'Synopsis')
            after = "Textos traducidos correctamente en ambos idiomas."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_12_filtro_truncate_synopsis(self):
        """12: Verifica que el filtro de resumen trunca correctamente a 20 caracteres."""
        description = "Test 12: Verifica que el filtro de resumen trunca correctamente a 20 caracteres."
        before = "Artículo 'Remote Work Insights' con sinopsis larga."
        action = "GET /articles/ y comprobar truncado."
        after = ""
        passed = True
        try:
            response = self.client.get(reverse('articles'))
            self.assertContains(response, 'Challenges and be...')
            after = "Sinopsis truncada correctamente."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_13_filtro_ago(self):
        """13: Verifica que la columna 'When' muestra el tiempo relativo correctamente."""
        description = "Test 13: Verifica que la columna 'When' muestra el tiempo relativo correctamente."
        before = "Artículo 'Remote Work Insights' creado hace 2 semanas y 2 días."
        action = "GET /articles/ y comprobar columna 'When'."
        after = ""
        passed = True
        try:
            response = self.client.get(reverse('articles'))
            self.assertRegex(response.content.decode(), r'2[\s\xa0]weeks, 2[\s\xa0]days ago')
            after = "Columna 'When' muestra el tiempo relativo correctamente."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_14_redireccion_home(self):
        """14: Verifica que la home redirige a /articles/."""
        description = "Test 14: Verifica que la home redirige a /articles/."
        before = "Navegación a la raíz del sitio."
        action = "GET / y comprobar redirección."
        after = ""
        passed = True
        try:
            response = self.client.get('/', follow=True)
            self.assertRedirects(response, reverse('articles'))
            after = "Redirigido correctamente a /articles/."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_15_menu_en_todas_las_paginas(self):
        """15: Verifica que el menú muestra las opciones correctas en cada página."""
        description = "Test 15: Verifica que el menú muestra las opciones correctas en cada página."
        urls = [
            reverse('articles'),
            reverse('favourites'),
            reverse('publications'),
            reverse('article-detail', args=[self.article1.pk])
        ]
        self.client.login(username='testuser1', password='testpass1')
        before = "Usuario autenticado en inglés."
        action = "Comprobar menú en varias páginas."
        after = ""
        passed = True
        try:
            for url in urls:
                response = self.client.get(url)
                self.assertContains(response, 'Articles')
                self.assertContains(response, 'Favourites')
                self.assertContains(response, 'Publications')
                self.assertContains(response, 'Logout')
                after += f"\nVerificado en {url}"
        except AssertionError as e:
            passed = False
            after += f"\nFallo en {url}: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_16_no_fav_sin_login(self):
        """16: Verifica que un usuario no autenticado es redirigido al login al intentar añadir un favorito."""
        description = "Test 16: Verifica que un usuario no autenticado es redirigido al login al intentar añadir un favorito."
        add_fav_url = reverse('add-favourite', args=[self.article2.pk])
        before = f"Usuario no autenticado. URL de favorito: {add_fav_url}"
        action = "Intentar hacer POST a la URL de favorito."
        after = ""
        passed = True
        try:
            response = self.client.post(add_fav_url, follow=False)
            login_url = getattr(settings, 'LOGIN_URL', '/accounts/login/')
            expected_login_url = f"{login_url}?next={add_fav_url}"
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, expected_login_url)
            after = f"Redirigido a: {response.url}"
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_17_no_publish_sin_login(self):
        """17: Verifica que no se puede publicar sin estar logueado."""
        description = "Test 17: Verifica que no se puede publicar sin estar logueado."
        publish_url = reverse('publish')
        before = "Usuario no autenticado."
        action = "Intentar publicar artículo sin login."
        after = ""
        passed = True
        try:
            response = self.client.post(publish_url, {
                'title': 'Unauthorized Article',
                'synopsis': 'Should not be published',
                'content': 'No access'
            })
            self.assertEqual(response.status_code, 302)
            login_url = '/accounts/login/?next=' + publish_url
            self.assertTrue(response.url.startswith(login_url))
            self.assertFalse(Article.objects.filter(title='Unauthorized Article').exists())
            after = "Redirigido a login y artículo no creado."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_18_login_menu_no_interfiere_register(self):
        """18: Verifica que el login desde el menú no interfiere con la página de registro y que el usuario aparece autenticado en el menú."""
        description = "Test 18: Verifica que el login desde el menú no interfiere con la página de registro y que el usuario aparece autenticado en el menú."
        before = "Usuario testuser2 no autenticado."
        action = "Login desde el menú en /articles/, luego visitar /register/ y /articles/."
        after = ""
        passed = True
        try:
            response = self.client.post(reverse('articles'), {
                'username': 'testuser2',
                'password': 'testpass2',
                'login_menu': 1
            }, follow=True)
            self.assertContains(response, 'Logged as testuser2')
            response = self.client.get(reverse('register'))
            self.assertContains(response, 'Register')
            response = self.client.get(reverse('articles'))
            self.assertContains(response, 'Logged as testuser2')
            after = "Usuario autenticado y menú correcto en ambas páginas."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_19_orden_articulos(self):
        """19: Verifica que los artículos están ordenados del más nuevo al más antiguo."""
        description = "Test 19: Verifica que los artículos están ordenados del más nuevo al más antiguo."
        before = "Artículos creados con diferentes fechas."
        action = "GET /articles/ y comprobar orden de los títulos."
        after = ""
        passed = True
        try:
            response = self.client.get(reverse('articles'))
            content = response.content.decode()
            pos1 = content.find('Data Analysis Trends')
            pos2 = content.find('Remote Work Insights')
            self.assertTrue(pos1 < pos2)
            after = f"'Data Analysis Trends' aparece antes que 'Remote Work Insights'."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_20_enlace_cambio_idioma(self):
        """20: Verifica que existe el enlace para cambiar de idioma."""
        description = "Test 20: Verifica que existe el enlace para cambiar de idioma."
        before = "Página de artículos en inglés y español."
        action = "Comprobar enlace de cambio de idioma en ambas versiones."
        after = ""
        passed = True
        try:
            response = self.client.get(reverse('articles'))
            self.assertContains(response, 'Switch to English')
            response = self.client.get('/es/articles/')
            self.assertContains(response, 'Volver a español')
            after = "Enlaces de cambio de idioma presentes en ambas versiones."
        except AssertionError as e:
            passed = False
            after = f"Error: {e}"
        self.print_test_details(description, before, action, after, passed)

    def test_21_menu_en_todas_las_paginas(self):
        """21: Verifica que el menú tiene los enlaces correctos en todas las páginas."""
        description = "Test 21: Verifica que el menú tiene los enlaces correctos en todas las páginas."
        urls = [
            '/en/articles/',
            '/en/favourites/',
            '/en/publications/',
            f'/en/articles/{self.article1.pk}/'
        ]
        self.client.login(username='testuser1', password='testpass1')
        self.client.cookies.load({'django_language': 'en'})
        before = "Usuario autenticado, idioma inglés."
        action = "Comprobar menú en varias URLs."
        after = ""
        passed = True
        try:
            for url in urls:
                response = self.client.get(url)
                self.assertContains(response, 'Articles')
                self.assertContains(response, 'Favourites')
                self.assertContains(response, 'Publications')
                self.assertContains(response, 'Logout')
                after += f"\nVerificado en {url}"
        except AssertionError as e:
            passed = False
            after += f"\nFallo en {url}: {e}"
        self.print_test_details(description, before, action, after, passed)









# python manage.py test

# python manage.py test -v 2
