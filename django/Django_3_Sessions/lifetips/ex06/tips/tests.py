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

        self.can_downvote_permission = Permission.objects.get(codename='can_downvote_tip')
        self.can_delete_permission = Permission.objects.get(codename='can_delete_tip')

        self.tip1 = Tip.objects.create(author=self.user1, content="Tip 1")
        self.tip2 = Tip.objects.create(author=self.user2, content="Tip 2")

    def test_01_initial_reputation(self):
        """Verificar que la reputación inicial es correcta."""
        self.assertEqual(self.user1.reputation, 0)
        self.assertEqual(self.user2.reputation, 15)
        self.assertEqual(self.user3.reputation, 30)

    def test_02_upvote_increases_reputation(self):
        """Verificar que los upvotes aumenten la reputación del autor."""
        self.tip1.add_upvote(self.user2)
        self.assertEqual(self.user1.reputation, 5)

    def test_03_downvote_decreases_reputation(self):
        """Verificar que los downvotes disminuyan la reputación del autor."""
        self.tip1.add_downvote(self.user2)
        self.assertEqual(self.user1.reputation, -2)

    def test_04_user_can_downvote_with_permission(self):
        """Verificar que los usuarios con permiso puedan hacer downvote."""
        self.assertTrue(self.user2.has_perm('tips.can_downvote_tip'))

    def test_05_user_can_delete_with_permission(self):
        """Verificar que los usuarios con permiso puedan eliminar tips."""
        self.assertTrue(self.user3.has_perm('tips.can_delete_tip'))

    def test_06_delete_tip_removes_reputation_effect(self):
        """Verificar que al eliminar un tip se elimine su influencia en la reputación."""
        self.tip1.add_upvote(self.user2)
        self.tip1.delete()
        self.assertEqual(self.user1.reputation, 0)

    def test_07_user_cannot_upvote_own_tip(self):
        """Verificar que los usuarios no puedan dar upvote a sus propios tips."""
        with self.assertRaises(PermissionDenied):
            self.tip1.add_upvote(self.user1)

    def test_08_user_cannot_downvote_own_tip(self):
        """Verificar que los usuarios no puedan dar downvote a sus propios tips."""
        with self.assertRaises(PermissionDenied):
            self.tip1.add_downvote(self.user1)

    def test_09_user_cannot_upvote_twice(self):
        """Verificar que los usuarios no puedan dar upvote al mismo tip más de una vez."""
        self.tip1.add_upvote(self.user2)
        with self.assertRaises(PermissionDenied):
            self.tip1.add_upvote(self.user2)

    def test_10_user_cannot_downvote_twice(self):
        """Verificar que los usuarios no puedan dar downvote al mismo tip más de una vez."""
        self.tip1.add_downvote(self.user2)
        with self.assertRaises(PermissionDenied):
            self.tip1.add_downvote(self.user2)

    def test_11_multiple_upvotes_increase_reputation(self):
        """Verificar que múltiples upvotes aumenten la reputación correctamente."""
        self.tip1.add_upvote(self.user2)
        self.tip1.add_upvote(self.user3)
        self.assertEqual(self.user1.reputation, 10)

    def test_12_multiple_downvotes_decrease_reputation(self):
        """Verificar que múltiples downvotes disminuyan la reputación correctamente."""
        self.tip1.add_downvote(self.user2)
        self.tip1.add_downvote(self.user3)
        self.assertEqual(self.user1.reputation, -4)

    def test_13_mixed_votes_reputation_calculation(self):
        """Verificar que la reputación se calcule correctamente con votos mixtos."""
        self.tip1.add_upvote(self.user2)
        self.tip1.add_downvote(self.user3)
        self.assertEqual(self.user1.reputation, 3)

    def test_14_reputation_does_not_go_below_threshold(self):
        """Verificar que la reputación no baje de un umbral determinado."""
        extra_users = [get_user_model().objects.create_user(username=f'user{i}') for i in range(10)]
        for user in extra_users:
            self.tip1.add_downvote(user)
        self.assertEqual(self.user1.reputation, -20)

    def test_15_non_author_cannot_delete_tip(self):
        """Verificar que solo el autor o un admin puedan eliminar un tip."""
        with self.assertRaises(PermissionDenied):
            self.tip1.delete(user=self.user2)

    def test_16_admin_can_delete_any_tip(self):
        """Verificar que los administradores puedan eliminar cualquier tip."""
        admin = get_user_model().objects.create_superuser(username='admin', password='adminpass')
        self.tip1.delete(user=admin)
        self.assertFalse(Tip.objects.filter(id=self.tip1.id).exists())

    def test_17_user_representation_includes_reputation(self):
        """Verificar que la representación del usuario incluya su reputación."""
        self.user1.reputation = 10
        self.user1.save()
        self.assertEqual(str(self.user1), "user1 (10 rep)")