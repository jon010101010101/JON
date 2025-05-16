from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article, UserFavouriteArticle

class ProjectTests(TestCase):
    """
    Tests obligatorios y opcionales para garantizar el cumplimiento del enunciado y mejorar la verificación del sistema.
    """

    def setUp(self):
        """Prepara los datos iniciales para los tests."""
        self.user1 = User.objects.create_user(username='user1', password='pass1')
        self.user2 = User.objects.create_user(username='user2', password='pass2')
        self.article = Article.objects.create(
            title="Test Article",
            author=self.user1,
            synopsis="This is a test synopsis.",
            content="This is the test content."
        )

    # ========================
    # Tests Obligatorios
    # ========================

    def test_01_ajax_login_logout(self):
        """[1. Obligatorio] Test de login y logout usando AJAX."""
        # Intento de login fallido
        response = self.client.post(reverse('ajax_login'), {'username': 'user1', 'password': 'wrongpass'})
        self.assertContains(response, 'Invalid username or password.', status_code=200)

        # Login exitoso
        response = self.client.post(reverse('ajax_login'), {'username': 'user1', 'password': 'pass1'}, content_type="application/json")
        self.assertContains(response, 'Welcome, user1!', status_code=200)

        # Logout exitoso
        response = self.client.post(reverse('ajax_logout'), content_type="application/json")
        self.assertContains(response, 'You have been logged out.', status_code=200)

    def test_02_article_creation_authenticated(self):
        """[2. Obligatorio] Test de creación de artículos por un usuario autenticado."""
        self.client.login(username='user1', password='pass1')
        response = self.client.post(reverse('article_create'), {
            'title': 'New Article',
            'synopsis': 'New synopsis',
            'content': 'New content'
        })
        self.assertEqual(response.status_code, 302)  # Redirige después de crear
        self.assertTrue(Article.objects.filter(title="New Article").exists())

    def test_03_article_creation_unauthenticated(self):
        """[3. Obligatorio] Test de creación de artículos por un usuario no autenticado."""
        response = self.client.post(reverse('article_create'), {
            'title': 'New Article',
            'synopsis': 'New synopsis',
            'content': 'New content'
        })
        self.assertEqual(response.status_code, 302)  # Redirige al login
        self.assertFalse(Article.objects.filter(title="New Article").exists())

    def test_04_favourite_article(self):
        """[4. Obligatorio] Test de añadir un artículo a favoritos."""
        self.client.login(username='user1', password='pass1')
        response = self.client.get(reverse('add_favourite', args=[self.article.pk]))
        self.assertEqual(response.status_code, 302)  # Redirige después de añadir
        self.assertTrue(UserFavouriteArticle.objects.filter(user=self.user1, article=self.article).exists())

    def test_05_favourite_list(self):
        """[5. Obligatorio] Test de listar artículos favoritos."""
        UserFavouriteArticle.objects.create(user=self.user1, article=self.article)
        self.client.login(username='user1', password='pass1')
        response = self.client.get(reverse('favourite_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Article")  # Verifica que el artículo favorito aparece

    # ========================
    # Tests Opcionales
    # ========================

    def test_06_register_user(self):
        """[6. Opcional] Test de registro de usuario."""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password': 'newpass'
        })
        self.assertEqual(response.status_code, 302)  # Redirige después del registro
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_07_logout_redirect(self):
        """[7. Opcional] Verifica que el logout redirige correctamente."""
        self.client.login(username='user1', password='pass1')
        response = self.client.post(reverse('ajax_logout'), follow=True)  # Sigue el redireccionamiento
        self.assertContains(response, 'Login')  # Verifica el contenido en la página destino

    def test_08_article_list(self):
        """[8. Opcional] Test de vista de lista de artículos."""
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Article")

    def test_09_article_detail(self):
        """[9. Opcional] Test de vista de detalle de un artículo."""
        response = self.client.get(reverse('article_detail', args=[self.article.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the test content.")

    def test_10_duplicate_favourite(self):
        """[10. Opcional] Verifica que no se puede añadir el mismo artículo dos veces a favoritos."""
        UserFavouriteArticle.objects.create(user=self.user1, article=self.article)
        self.client.login(username='user1', password='pass1')
        response = self.client.get(reverse('add_favourite', args=[self.article.pk]))
        self.assertEqual(response.status_code, 302)  # Redirige sin error
        favourites = UserFavouriteArticle.objects.filter(user=self.user1, article=self.article)
        self.assertEqual(favourites.count(), 1)  # Solo debería haber un favorito
        # Verifica el mensaje opcional
        response = self.client.get(reverse('favourite_list'))
        self.assertContains(response, "This article is already in your favourites.")

# python runner.py

