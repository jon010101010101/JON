from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import Article, UserFavouriteArticle
from django.conf import settings

class ArticleTests(TestCase):
    """
    Tests automáticos para comprobar todas las funcionalidades clave del proyecto:
    - Creación y visualización de artículos
    - Registro, login y logout de usuarios
    - Favoritos y publicaciones
    - Internacionalización y menús
    - Filtros personalizados y seguridad de acceso

    Estos tests simulan el comportamiento de un usuario y validan que tu proyecto
    cumple con los requisitos del enunciado y los tests de evaluación.
    """

    def setUp(self):
        """Prepara usuarios y artículos de prueba para los tests."""
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
        self.article3 = Article.objects.create(
            title='Remote Work Insights',
            author=self.user2,
            synopsis='Challenges and benefits of remote work in today’s professional environment. This article explores strategies for effective remote collaboration.',
            content='Full article content about remote work.'
        )
        self.article3.created = timezone.now() - timedelta(weeks=2, days=2)
        self.article3.save()

    def test_01_lista_articulos(self):
        """
        Verifica que la lista de artículos muestra correctamente los títulos de los artículos creados.
        Crea dos artículos y comprueba que ambos aparecen en la respuesta de la vista 'articles'.
        """
        response = self.client.get(reverse('articles'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Project Management')
        self.assertContains(response, 'Data Analysis Trends')

    def test_02_menu_login_logout(self):
        """
        Verifica que el login y logout desde el menú funcionan correctamente.
        Realiza login con un usuario y luego comprueba que aparece el mensaje de usuario autenticado.
        Después realiza logout y comprueba que vuelve a aparecer la opción de login.
        """
        response = self.client.post(reverse('articles'), {
            'username': 'testuser1',
            'password': 'testpass1',
            'login_menu': 1
        }, follow=True)
        self.assertContains(response, 'Logged as testuser1')
        response = self.client.get(reverse('logout'), follow=True)
        self.assertContains(response, 'Login')

    def test_03_error_login(self):
        """
        Verifica que se muestra error si el login falla.
        Intenta hacer login con una contraseña incorrecta y comprueba que aparece el mensaje de error.
        """
        response = self.client.post(reverse('articles'), {
            'username': 'testuser1',
            'password': 'wrongpass',
            'login_menu': 1
        })
        self.assertContains(response, 'Invalid username or password.')

    def test_04_publicaciones_requiere_login(self):
        """
        Verifica que la vista de publicaciones requiere login.
        Intenta acceder a la vista de publicaciones sin autenticación (debe fallar),
        luego accede autenticado y comprueba que funciona y muestra el artículo correspondiente.
        """
        response = self.client.get(reverse('publications'))
        self.assertNotEqual(response.status_code, 200)
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.get(reverse('publications'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Project Management')

    def test_05_registro_usuario(self):
        """
        Verifica que el registro de usuario funciona correctamente.
        Envía un POST con datos válidos y comprueba que el usuario se crea y se redirige a la vista de artículos.
        """
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'StrongPassword123',
            'password2': 'StrongPassword123'
        }, follow=True)
        self.assertRedirects(response, reverse('articles'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_06_error_registro(self):
        """
        Verifica que se muestra error si el registro falla (contraseñas diferentes).
        Envía un POST con contraseñas diferentes y comprueba que aparece el mensaje de error.
        """
        response = self.client.post(reverse('register'), {
            'username': 'newuser2',
            'password1': 'StrongPassword123',
            'password2': 'DifferentPassword'
        })
        self.assertContains(response, 'The two password fields didn’t match')

    def test_07_publicar_articulo(self):
        """
        Verifica que publicar un artículo funciona correctamente.
        Hace login, publica un artículo y comprueba que se crea correctamente.
        """
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.post(reverse('publish'), {
            'title': 'Business Strategy',
            'synopsis': 'Key factors for successful business growth.',
            'content': 'Detailed article content about business strategy.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Article.objects.filter(title='Business Strategy').exists())

    def test_08_favoritos_y_añadir(self):
        """
        Verifica que se pueden añadir artículos a favoritos y verlos.
        Hace login, añade un artículo a favoritos y comprueba que aparece en la lista de favoritos.
        """
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.post(reverse('add-favourite', args=[self.article2.pk]), follow=True)
        self.assertRedirects(response, reverse('favourite-added'))
        self.assertTrue(UserFavouriteArticle.objects.filter(user=self.user1, article=self.article2).exists())
        response = self.client.get(reverse('favourites'))
        self.assertContains(response, 'Data Analysis Trends')

    def test_09_favorito_duplicado(self):
        """
        Verifica que no se puede añadir dos veces el mismo favorito.
        Añade un favorito y luego intenta añadirlo de nuevo, comprobando la redirección.
        """
        self.client.login(username='testuser1', password='testpass1')
        UserFavouriteArticle.objects.create(user=self.user1, article=self.article2)
        response = self.client.post(reverse('add-favourite', args=[self.article2.pk]), follow=True)
        self.assertRedirects(response, reverse('already-favourite'))

    def test_10_detalle_articulo(self):
        """
        Verifica que el detalle del artículo muestra la información correctamente.
        Accede a la vista de detalle y comprueba que se muestran el título y la sinopsis.
        """
        response = self.client.get(reverse('article-detail', args=[self.article1.pk]))
        self.assertContains(response, 'Project Management')
        self.assertContains(response, 'Best practices for team collaboration and project delivery.')

    def test_11_internacionalizacion(self):
        """
        Verifica que el sitio muestra los textos traducidos según el idioma en la URL.
        Comprueba textos en español y en inglés en la vista de artículos.
        """
        response = self.client.get('/es/articles/')
        self.assertContains(response, 'Artículos')  # O el texto traducido que corresponda
        self.assertContains(response, 'Comparte tus escritos')  # Subtítulo en español
        self.assertContains(response, 'Sinopsis')  # Columna de la tabla en español
        response = self.client.get('/en/articles/')
        self.assertContains(response, 'Articles')
        self.assertContains(response, 'Share your writings')
        self.assertContains(response, 'Synopsis')

    def test_12_filtro_truncate_synopsis(self):
        """
        Verifica que el filtro de resumen trunca correctamente a 20 caracteres.
        Comprueba que la sinopsis larga se trunca adecuadamente en la vista de artículos.
        """
        response = self.client.get(reverse('articles'))
        # La sinopsis de 'Remote Work Insights' es larga, así que debe truncarse:
        self.assertContains(response, 'Challenges and be...')

    def test_13_filtro_ago(self):
        """
        Verifica que la columna 'When' muestra el tiempo relativo correctamente.
        Comprueba que aparece el texto adecuado para un artículo antiguo.
        """
        response = self.client.get(reverse('articles'))
        self.assertRegex(response.content.decode(), r'2[\s\xa0]weeks, 2[\s\xa0]days ago')

    def test_14_redireccion_home(self):
        """
        Verifica que la home redirige a /articles/.
        Accede a la raíz del sitio y comprueba la redirección.
        """
        response = self.client.get('/', follow=True)
        self.assertRedirects(response, reverse('articles'))

    def test_15_menu_en_todas_las_paginas(self):
        """
        Verifica que el menú muestra las opciones correctas en cada página.
        Comprueba que el menú contiene los enlaces principales en varias vistas.
        """
        urls = [
            reverse('articles'),
            reverse('favourites'),
            reverse('publications'),
            reverse('article-detail', args=[self.article1.pk])
        ]
        self.client.login(username='testuser1', password='testpass1')
        for url in urls:
            response = self.client.get(url)
            self.assertContains(response, 'Articles')
            self.assertContains(response, 'Favourites')
            self.assertContains(response, 'Publications')
            self.assertContains(response, 'Logout')

    def test_16_no_fav_sin_login(self):
        """
        Verifica que un usuario no autenticado es redirigido al login al intentar añadir un favorito.
        """
        add_fav_url = reverse('add-favourite', args=[self.article2.pk])
        response = self.client.post(add_fav_url, follow=False)
        login_url = getattr(settings, 'LOGIN_URL', '/accounts/login/')
        expected_login_url = f"{login_url}?next={add_fav_url}"
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, expected_login_url)

    def test_17_no_publish_sin_login(self):
        """
        Verifica que no se puede publicar sin estar logueado.
        Intenta publicar sin autenticación y comprueba que hay redirección a login y que no se crea el artículo.
        """
        publish_url = reverse('publish')
        response = self.client.post(publish_url, {
            'title': 'Unauthorized Article',
            'synopsis': 'Should not be published',
            'content': 'No access'
        })
        # Comprueba que hay redirección
        self.assertEqual(response.status_code, 302)
        # Comprueba que redirige a login
        login_url = '/accounts/login/?next=' + publish_url
        self.assertTrue(response.url.startswith(login_url))
        # Comprueba que NO se ha creado el artículo
        self.assertFalse(Article.objects.filter(title='Unauthorized Article').exists())

    def test_18_login_menu_no_interfiere_register(self):
        """
        Verifica que el login desde el menú no interfiere con la página de registro y que el usuario aparece autenticado en el menú.
        """
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

    def test_19_orden_articulos(self):
        """
        Verifica que los artículos están ordenados del más nuevo al más antiguo.
        Comprueba el orden de aparición de los títulos en la respuesta.
        """
        response = self.client.get(reverse('articles'))
        content = response.content.decode()
        pos1 = content.find('Data Analysis Trends')
        pos2 = content.find('Remote Work Insights')
        self.assertTrue(pos1 < pos2)

    def test_20_enlace_cambio_idioma(self):
        """
        Verifica que existe el enlace para cambiar de idioma.
        Comprueba la presencia del enlace en inglés y en español.
        """
        response = self.client.get(reverse('articles'))
        self.assertContains(response, 'Switch to English')
        response = self.client.get('/es/articles/')
        self.assertContains(response, 'Volver a español')

    def test_21_menu_en_todas_las_paginas(self):
        """
        Verifica que el menú tiene los enlaces correctos en todas las páginas.
        Comprueba que el menú contiene los enlaces principales en varias vistas en inglés.
        """
        urls = [
            '/en/articles/',
            '/en/favourites/',
            '/en/publications/',
            f'/en/articles/{self.article1.pk}/'
        ]
        self.client.login(username='testuser1', password='testpass1')
        self.client.cookies.load({'django_language': 'en'})
        for url in urls:
            response = self.client.get(url)
            self.assertContains(response, 'Articles')
            self.assertContains(response, 'Favourites')
            self.assertContains(response, 'Publications')
            self.assertContains(response, 'Logout')




# python runner.py

