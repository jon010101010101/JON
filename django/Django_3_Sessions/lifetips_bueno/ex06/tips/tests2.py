from django.test import TestCase
from django.contrib.auth import get_user_model
from tips.models import Tip

CustomUser = get_user_model()


class TipVoteTestCase(TestCase):
    def setUp(self):
        """
        Configuración inicial para las pruebas:
        - Creamos usuarios: user1, user2, low_rep_user y superuser.
        - Creamos un tip de prueba.
        """
        self.user1 = CustomUser.objects.create_user(username="user1", reputation=5, password="pass")
        self.user2 = CustomUser.objects.create_user(username="user2", reputation=20, password="pass")
        self.low_rep_user = CustomUser.objects.create_user(username="low_rep_user", reputation=0, password="pass")
        self.superuser = CustomUser.objects.create_superuser(username="admin", password="pass")
        self.tip = Tip.objects.create(author=self.user1, content="Sample Tip")

    def run_test(self, description, func):
        """Ejecuta una prueba y muestra un ✔️ o ❌ dependiendo del resultado."""
        try:
            func()
            print(f"✔️ {description}")
        except AssertionError as e:
            print(f"❌ {description}\n    {e}")

    def test_all(self):
        """Ejecuta todas las pruebas."""
        self.run_test("Reputación inicial correcta", self.test_initial_reputation)
        self.run_test("Incremento de reputación por upvote", self.test_upvote_reputation)
        self.run_test("Reducción de reputación por downvote", self.test_downvote_reputation)
        self.run_test("Ajuste de reputación al eliminar un tip", self.test_delete_tip_reputation)
        self.run_test("Reputación puede ser negativa", self.test_negative_reputation)
        self.run_test("Combinación de votos actualiza correctamente la reputación", self.test_combination_of_votes)
        self.run_test("Permisos: Usuarios con baja reputación no pueden hacer downvotes", self.test_downvote_permission_low_reputation)
        self.run_test("Permisos: Usuarios con alta reputación pueden hacer downvotes", self.test_downvote_permission_high_reputation)
        self.run_test("Permisos: Usuarios con baja reputación no pueden eliminar tips", self.test_delete_permission_low_reputation)
        self.run_test("Permisos: Ganar reputación restaura permisos", self.test_reputation_gain_restores_permissions)
        self.run_test("Permisos: Perder reputación revoca permisos", self.test_reputation_loss_removes_permissions)
        self.run_test("Superusuario tiene siempre permisos", self.test_superuser_permissions)

    # -----------------------------------------------
    # Métodos de prueba individuales
    # -----------------------------------------------

    def test_initial_reputation(self):
        """Verificar que un nuevo usuario tiene la reputación inicial esperada."""
        self.assertEqual(self.low_rep_user.reputation, 0)

    def test_upvote_reputation(self):
        """Verificar que los upvotes aumentan la reputación del autor del tip."""
        self.tip.add_upvote(self.user2)
        self.assertEqual(self.tip.author.reputation, 10)  # 5 original + 5 por el upvote

    def test_downvote_reputation(self):
        """Verificar que los downvotes disminuyen la reputación del autor del tip."""
        self.tip.add_downvote(self.user2)
        self.assertEqual(self.tip.author.reputation, 3)  # 5 original - 2 por el downvote

    def test_delete_tip_reputation(self):
        """Verificar que al eliminar un tip, la reputación del autor se restaura."""
        self.tip.add_upvote(self.user2)
        self.tip.delete(force_delete=True)
        self.assertEqual(self.user1.reputation, 5)  # Reputación inicial restaurada

    def test_negative_reputation(self):
        """Verificar que la reputación de un usuario puede ser negativa."""
        self.tip.add_downvote(self.user2)
        self.tip.add_downvote(self.user2)  # Segundo downvote no debería duplicar el efecto
        self.assertEqual(self.tip.author.reputation, 3)  # 5 original - 2 (solo un downvote permitido)

    def test_combination_of_votes(self):
        """Verificar que la reputación se actualiza correctamente con combinaciones de votos."""
        self.tip.add_upvote(self.user2)
        self.tip.add_downvote(self.user2)
        self.assertEqual(self.tip.upvotes.count(), 0)
        self.assertEqual(self.tip.downvotes.count(), 1)
        self.assertEqual(self.tip.author.reputation, 3)  # 5 original + 5 - 5 - 2

    def test_downvote_permission_low_reputation(self):
        """Verificar que los usuarios con baja reputación no pueden hacer downvotes."""
        result = self.tip.add_downvote(self.low_rep_user)
        self.assertFalse(result)
        self.assertEqual(self.tip.downvotes.count(), 0)

    def test_downvote_permission_high_reputation(self):
        """Verificar que los usuarios con alta reputación pueden hacer downvotes."""
        result = self.tip.add_downvote(self.user2)
        self.assertTrue(result)
        self.assertEqual(self.tip.downvotes.count(), 1)

    def test_delete_permission_low_reputation(self):
        """Verificar que los usuarios con baja reputación no pueden eliminar tips."""
        with self.assertRaises(PermissionError):
            self.tip.delete()

    def test_reputation_gain_restores_permissions(self):
        """Verificar que ganar reputación restaura permisos."""
        self.user1.update_reputation(10)  # Incrementa reputación a 15
        self.assertTrue(self.user1.has_perm('tips.can_downvote_tip'))

    def test_reputation_loss_removes_permissions(self):
        """Verificar que perder reputación revoca permisos."""
        self.user2.reputation = 30
        self.user2.save()
        self.user2.reputation = 10
        self.user2.save()
        with self.assertRaises(PermissionError):
            self.tip.delete()

    def test_superuser_permissions(self):
        """Verificar que el superusuario tiene permisos para todas las operaciones."""
        self.assertTrue(self.superuser.has_perm('tips.can_downvote_tip'))
        self.assertTrue(self.superuser.has_perm('tips.can_delete_tip'))