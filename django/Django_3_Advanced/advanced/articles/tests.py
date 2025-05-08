from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article, UserFavouriteArticle

class ArticleTests(TestCase):
    def setUp(self):
        """Preparación: crea usuarios y artículos de prueba."""
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user2 = User.objects.create_user(username='batman', password='joker')
        self.article = Article.objects.create(
            title='Test Article',
            author=self.user,
            synopsis='Short synopsis',
            content='Content here'
        )
        self.article2 = Article.objects.create(
            title='I\'m BATMAN',
            author=self.user2,
            synopsis='I\'m REALLY BATMAN',
            content='I AM THE NIGHT'
        )

    def test_01_lista_articulos(self):
        """Prueba 1: Verifica que la lista de artículos muestra los artículos correctamente."""
        response = self.client.get(reverse('articles'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')
        self.assertContains(response, 'I\'m BATMAN')

    def test_02_menu_login_logout(self):
        """Prueba 2: Verifica que el login y logout desde el menú funcionan correctamente."""
        response = self.client.post(reverse('articles'), {
            'username': 'testuser',
            'password': '12345',
            'login_menu': 1
        }, follow=True)
        self.assertContains(response, 'Logged as testuser')
        response = self.client.get(reverse('logout'), follow=True)
        self.assertContains(response, 'Login')

    def test_03_error_login(self):
        """Prueba 3: Verifica que se muestra error si el login falla."""
        response = self.client.post(reverse('articles'), {
            'username': 'testuser',
            'password': 'wrongpass',
            'login_menu': 1
        })
        self.assertContains(response, 'Invalid username or password.')

    def test_04_publicaciones_requiere_login(self):
        """Prueba 4: Verifica que la vista de publicaciones requiere login."""
        response = self.client.get(reverse('publications'))
        self.assertNotEqual(response.status_code, 200)
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('publications'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')

    def test_05_registro_usuario(self):
        """Prueba 5: Verifica que el registro de usuario funciona correctamente."""
        response = self.client.post(reverse('register'), {
            'username': 'nuevo',
            'password1': 'ContraseñaFuerte123',
            'password2': 'ContraseñaFuerte123'
        }, follow=True)
        self.assertRedirects(response, reverse('articles'))
        self.assertTrue(User.objects.filter(username='nuevo').exists())

    def test_06_error_registro(self):
        """Prueba 6: Verifica que se muestra error si el registro falla (contraseñas diferentes)."""
        response = self.client.post(reverse('register'), {
            'username': 'nuevo2',
            'password1': 'ContraseñaFuerte123',
            'password2': 'OtraContraseña'
        })
        self.assertContains(response, 'The two password fields didn’t match')

    def test_07_publicar_articulo(self):
        """Prueba 7: Verifica que publicar un artículo funciona correctamente."""
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('publish'), {
            'title': 'Nuevo Artículo',
            'synopsis': 'Otra sinopsis',
            'content': 'Nuevo contenido'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Article.objects.filter(title='Nuevo Artículo').exists())

    def test_08_favoritos_y_añadir(self):
        """Prueba 8: Verifica que se pueden añadir artículos a favoritos y verlos."""
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('add-favourite', args=[self.article2.pk]), follow=True)
        self.assertRedirects(response, reverse('favourite-added'))
        self.assertTrue(UserFavouriteArticle.objects.filter(user=self.user, article=self.article2).exists())
        response = self.client.get(reverse('favourites'))
        self.assertContains(response, 'I\'m BATMAN')

    def test_09_favorito_duplicado(self):
        """Prueba 9: Verifica que no se puede añadir dos veces el mismo favorito."""
        self.client.login(username='testuser', password='12345')
        UserFavouriteArticle.objects.create(user=self.user, article=self.article2)
        response = self.client.post(reverse('add-favourite', args=[self.article2.pk]), follow=True)
        self.assertRedirects(response, reverse('already-favourite'))

    def test_10_detalle_articulo(self):
        """Prueba 10: Verifica que el detalle del artículo muestra la información correctamente."""
        response = self.client.get(reverse('article-detail', args=[self.article.pk]))
        self.assertContains(response, 'Test Article')
        self.assertContains(response, 'Short synopsis')

    def test_11_internacionalizacion(self):
        """Prueba 11: Verifica que el sitio muestra los textos traducidos según el idioma en la URL."""
        response = self.client.get('/es/articles/')
        self.assertContains(response, 'Artículos')  # O el texto traducido que corresponda


    def test_12_filtro_truncate_synopsis(self):
        """Prueba 12: Verifica que el filtro de resumen trunca correctamente a 20 caracteres."""
        response = self.client.get(reverse('articles'))
        self.assertContains(response, 'After leaving the Jo...')  # Ejemplo de resumen truncado

    def test_13_filtro_ago(self):
        """Prueba 13: Verifica que la columna 'When' muestra el tiempo relativo correctamente."""
        response = self.client.get(reverse('articles'))
        self.assertRegex(response.content.decode(), r'\d+ week')  # Por ejemplo: '1 week, 2 days ago'

    def test_14_redireccion_home(self):
        """Prueba 14: Verifica que la home redirige a /articles/."""
        response = self.client.get('/', follow=True)
        self.assertRedirects(response, reverse('articles'))

    def test_15_menu_en_todas_las_paginas(self):
        """Prueba 15: Verifica que el menú muestra las opciones correctas en cada página."""
        # Sin login
        response = self.client.get(reverse('register'))
        self.assertContains(response, 'Register')
        self.assertContains(response, 'Login')
        # Con login
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('favourites'))
        self.assertContains(response, 'Favourites')
        self.assertContains(response, 'Logout')

    def test_16_no_fav_sin_login(self):
        """Prueba 16: Verifica que no se puede añadir a favoritos sin estar logueado."""
        response = self.client.post(reverse('add-favourite', args=[self.article2.pk]))
        self.assertNotEqual(response.status_code, 200)

    def test_17_no_publish_sin_login(self):
        """Prueba 17: Verifica que no se puede publicar sin estar logueado."""
        response = self.client.post(reverse('publish'), {
            'title': 'Artículo sin login',
            'synopsis': 'Sinopsis',
            'content': 'Contenido'
        })
        self.assertNotEqual(response.status_code, 200)

    def test_18_login_menu_no_interfiere_register(self):
        """Prueba 18: Verifica que el login en menú no interfiere con el registro."""
        # Intentar login incorrecto en menú en /register/
        response = self.client.post(reverse('register'), {
            'username': 'nouser',
            'password': 'wrong',
            'login_menu': 1
        })
        self.assertContains(response, 'Invalid username or password.')
        # Ahora registrar correctamente
        response = self.client.post(reverse('register'), {
            'username': 'nuevo3',
            'password1': 'ContraseñaFuerte123',
            'password2': 'ContraseñaFuerte123'
        }, follow=True)
        self.assertTrue(User.objects.filter(username='nuevo3').exists())

    def test_19_orden_articulos(self):
        """Prueba 19: Verifica que los artículos están ordenados del más nuevo al más antiguo."""
        Article.objects.create(
            title='Más nuevo',
            author=self.user,
            synopsis='Nuevo',
            content='Nuevo contenido'
        )
        response = self.client.get(reverse('articles'))
        content = response.content.decode()
        self.assertTrue(content.index('Más nuevo') < content.index('Test Article'))

    def test_20_enlace_cambio_idioma(self):
        """Prueba 20: Verifica que existe el enlace para cambiar de idioma."""
        response = self.client.get(reverse('articles'))
        self.assertIn('Passer en français', response.content.decode())  # O "Switch to English"

    def test_21_menu_en_todas_las_paginas(self):
        """Prueba 21: Verifica que el menú tiene los enlaces correctos en todas las páginas."""
        urls = [reverse('articles'), reverse('register'), reverse('article-detail', args=[self.article.pk])]
        for url in urls:
            response = self.client.get(url)
            self.assertIn('Articles', response.content.decode())




# python manage.py test
