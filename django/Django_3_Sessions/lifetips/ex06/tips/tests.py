from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Tip
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Permission

class ReputationTests(TestCase):

    def setUp(self):
        # Crea usuarios con diferentes reputaciones
        self.user1 = get_user_model().objects.create_user(username='user1', password='password1')
        self.user1.reputation = 0
        self.user1.save()

        self.user2 = get_user_model().objects.create_user(username='user2', password='password2')
        self.user2.reputation = 15
        self.user2.save()

        self.user3 = get_user_model().objects.create_user(username='user3', password='password3')
        self.user3.reputation = 30
        self.user3.save()

        # Obtener los permisos
        self.can_downvote_permission = Permission.objects.get(codename='can_downvote_tip')
        self.can_delete_permission = Permission.objects.get(codename='can_delete_tip')

        # Asigna permisos manualmente (necesario si no usas signals en testing)

        # Crea algunos tips
        self.tip1 = Tip.objects.create(author=self.user1, content="Tip 1")
        self.tip2 = Tip.objects.create(author=self.user2, content="Tip 2")
        self.tip3 = Tip.objects.create(author=self.user1, content="Tip 3")

    def test_initial_reputation(self):
        # Verifica que la reputación inicial es correcta
        self.assertEqual(self.user1.reputation, 0)
        self.assertEqual(self.user2.reputation, 15)
        self.assertEqual(self.user3.reputation, 30)

    def test_upvote_downvote(self):
        # Login como user1 (reputación 0)
        self.client.login(username='user1', password='password1')

        # User1 upvotea el tip1
        response = self.client.post(reverse('vote_tip', args=[self.tip1.id, 'upvote']))
        self.assertEqual(response.status_code, 302)
        self.tip1.refresh_from_db()
        self.user1.refresh_from_db()
        self.assertEqual(self.tip1.upvotes.count(), 1)
        self.assertEqual(self.tip1.author.reputation, 5)

    def test_downvote_permission(self):
        # Login como user1 (reputación 0)
        self.client.login(username='user1', password='password1')

        # Intenta downvotear el tip1 y verifica que se deniega el permiso
        response = self.client.post(reverse('vote_tip', args=[self.tip1.id, 'downvote']))
        self.assertEqual(response.status_code, 302)

        # Login como user2 (reputación 15 y con permiso can_downvote)
        self.client.login(username='user2', password='password2')
        self.user2.user_permissions.add(self.can_downvote_permission)
        self.user2.save()

        # Downvotea el tip1 y verifica que se permite la acción
        response = self.client.post(reverse('vote_tip', args=[self.tip1.id, 'downvote']))
        self.assertEqual(response.status_code, 302)
        self.tip1.refresh_from_db()
        self.user1.refresh_from_db()
        self.assertEqual(self.tip1.downvotes.count(), 1)
        self.assertEqual(self.tip1.author.reputation, 3)

    def test_delete_permission(self):
        # Login como user1 (reputación 0, no puede borrar normalmente)
        self.client.login(username='user1', password='password1')

        # Intenta borrar el tip1 y verifica que se deniega el permiso
        response = self.client.post(reverse('delete_tip', args=[self.tip1.id]))
        self.assertEqual(response.status_code, 302)
        # Login como user1 (reputación 0, es el autor del tip)
        self.client.login(username='user1', password='password1')

        # Intenta borrar el tip3 y verifica que se permite la acción
        response = self.client.post(reverse('delete_tip', args=[self.tip3.id]))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Tip.DoesNotExist):
            Tip.objects.get(pk=self.tip3.id)

    def test_delete_reputation_recalculation(self):
        # Creamos un tip
        self.client.login(username='user1', password='password1')
        self.tip4 = Tip.objects.create(author=self.user1, content="Tip 4")

        # User2 upvotea el tip4
        self.client.login(username='user2', password='password2')
        self.user2.user_permissions.add(self.can_downvote_permission)
        self.user2.save()
        response = self.client.post(reverse('vote_tip', args=[self.tip4.id, 'upvote']))
        self.assertEqual(response.status_code, 302)

        self.user1.refresh_from_db()
        self.assertEqual(self.user1.reputation, 5)

        # Borra el tip4
        self.client.login(username='user1', password='password1')
        response = self.client.post(reverse('delete_tip', args=[self.tip4.id]))
        self.assertEqual(response.status_code, 302)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.reputation, 0)
