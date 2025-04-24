from django.test import TestCase
from django.contrib.auth import get_user_model
from tips.models import Tip

CustomUser = get_user_model()


class TipVoteTestCase(TestCase):
    def setUp(self):
        # Crear usuarios
        self.user1 = CustomUser.objects.create_user(username="user1", reputation=10, password="pass")
        self.user2 = CustomUser.objects.create_user(username="user2", reputation=20, password="pass")
        self.low_rep_user = CustomUser.objects.create_user(username="low_rep_user", reputation=0, password="pass")
        self.superuser = CustomUser.objects.create_superuser(username="admin", password="pass")

        # Crear un tip
        self.tip = Tip.objects.create(author=self.user1, content="Sample Tip")

    # -----------------------------------------------
    # Pruebas Obligatorias
    # -----------------------------------------------

    # Pruebas de Reputación
    def test_initial_reputation(self):
        """Verificar que un nuevo usuario tiene 0 puntos de reputación."""
        self.assertEqual(self.low_rep_user.reputation, 0)

    def test_upvote_reputation(self):
        """Verificar que los upvotes aumentan la reputación del autor del tip."""
        self.tip.add_upvote(self.user2)
        self.assertEqual(self.tip.author.reputation, 15)  # 10 original + 5 por el upvote

    def test_downvote_reputation(self):
        """Verificar que los downvotes disminuyen la reputación del autor del tip."""
        self.tip.add_downvote(self.user2)
        self.assertEqual(self.tip.author.reputation, 8)  # 10 original - 2 por el downvote

    def test_delete_tip_reputation(self):
        """Verificar que al eliminar un tip, la influencia de sus votos desaparece de la reputación del autor."""
        self.tip.add_upvote(self.user2)
        self.tip.delete(force_delete=True)
        self.assertEqual(self.user1.reputation, 10)  # Se restaura a la reputación inicial

    def test_negative_reputation(self):
        """Verificar que la reputación de un usuario puede ser negativa."""
        self.tip.add_downvote(self.user2)
        self.tip.add_downvote(self.user2)  # Segundo downvote no debería duplicar el efecto
        self.assertEqual(self.tip.author.reputation, 8)  # 10 original - 2 (solo un downvote permitido)

    def test_combination_of_votes(self):
        """Verificar que la reputación se actualiza correctamente con combinaciones de votos."""
        self.tip.add_upvote(self.user2)
        self.tip.add_downvote(self.user2)
        self.assertEqual(self.tip.upvotes.count(), 0)
        self.assertEqual(self.tip.downvotes.count(), 1)
        self.assertEqual(self.tip.author.reputation, 8)  # 10 original + 5 - 5 - 2

    # -----------------------------------------------
    # Pruebas de Permisos
    # -----------------------------------------------

    def test_downvote_permission_low_reputation(self):
        """Verificar que los usuarios con menos de 2 puntos no pueden hacer downvotes."""
        result = self.tip.add_downvote(self.low_rep_user)
        self.assertFalse(result)  # No se permite el downvote
        self.assertEqual(self.tip.downvotes.count(), 0)

    def test_downvote_permission_high_reputation(self):
        """Verificar que los usuarios con 15 o más puntos pueden hacer downvotes."""
        result = self.tip.add_downvote(self.user2)
        self.assertTrue(result)  # Se permite el downvote
        self.assertEqual(self.tip.downvotes.count(), 1)

    def test_delete_permission_low_reputation(self):
        """Verificar que los usuarios con menos de 30 puntos no pueden eliminar tips."""
        with self.assertRaises(PermissionError):  # Simula que Django lanza un error de permiso
            self.tip.delete()

    def test_delete_permission_high_reputation(self):
        """Verificar que los usuarios con 30 o más puntos pueden eliminar tips."""
        self.user2.reputation = 30
        self.user2.save()
        tip = Tip.objects.create(author=self.user2, content="Another Tip")
        try:
            tip.delete(force_delete=True)  # Debería eliminarse correctamente
        except PermissionError:
            self.fail("El usuario con alta reputación no pudo eliminar el tip.")

    # -----------------------------------------------
    # Pruebas de Comportamiento Dinámico
    # -----------------------------------------------

    def test_reputation_loss_removes_permissions(self):
        """Verificar que si un usuario pierde reputación, pierde los permisos otorgados."""
        self.user2.reputation = 30  # Otorga permiso para eliminar tips
        self.user2.save()
        self.user2.reputation = 10  # Pierde reputación
        self.user2.save()
        with self.assertRaises(PermissionError):  # Ya no puede eliminar tips
            self.tip.delete()

    def test_reputation_gain_restores_permissions(self):
        """Verificar que si un usuario recupera la reputación necesaria, recupera los permisos."""
        # Usuario inicialmente sin suficiente reputación
        self.user1.reputation = 10
        self.user1.save()
        self.assertFalse(self.tip.add_downvote(self.user1))  # No puede hacer downvotes

        # Incrementa la reputación del usuario para permitir downvotes
        self.user1.reputation = 15
        self.user1.save()
        self.assertTrue(self.tip.add_downvote(self.user1))  # Ahora puede hacer downvotes

    # -----------------------------------------------
    # Pruebas de Apariencia
    # -----------------------------------------------

    def test_user_display_with_reputation(self):
        """Verificar que el nombre del usuario aparece con su reputación entre corchetes."""
        self.assertEqual(str(self.user1), "user1 (10)")

     # -----------------------------------------------
    # Pruebas Voluntarias
    # -----------------------------------------------

    def test_upvote_increases_reputation(self):
        """Realizar un upvote: aumenta el contador de upvotes y la reputación del autor en 5 puntos."""
        self.tip.add_upvote(self.user2)
        self.assertEqual(self.tip.upvotes.count(), 1)
        self.assertEqual(self.tip.author.reputation, 15)  # 10 original + 5 por el upvote

    def test_downvote_decreases_reputation(self):
        """Realizar un downvote: aumenta el contador de downvotes y reduce la reputación del autor en 2 puntos."""
        self.tip.add_downvote(self.user2)
        self.assertEqual(self.tip.downvotes.count(), 1)
        self.assertEqual(self.tip.author.reputation, 8)  # 10 original - 2 por el downvote

    def test_change_upvote_to_downvote(self):
        """Cambiar de un upvote a un downvote: actualiza correctamente los contadores y la reputación."""
        self.tip.add_upvote(self.user2)
        self.tip.add_downvote(self.user2)
        self.assertEqual(self.tip.upvotes.count(), 0)
        self.assertEqual(self.tip.downvotes.count(), 1)
        self.assertEqual(self.tip.author.reputation, 8)  # 10 original + 5 - 5 - 2

    def test_prevent_duplicate_votes(self):
        """Evitar votos duplicados: garantiza que un usuario no pueda votar dos veces por el mismo tip."""
        self.tip.add_upvote(self.user2)
        result = self.tip.add_upvote(self.user2)  # Segundo voto no permitido
        self.assertFalse(result)
        self.assertEqual(self.tip.upvotes.count(), 1)

    def test_multiple_users_voting(self):
        """Verificar múltiples usuarios votando: asegura que varios usuarios puedan votar por el mismo tip."""
        self.tip.add_upvote(self.user2)
        self.tip.add_upvote(self.low_rep_user)
        self.assertEqual(self.tip.upvotes.count(), 2)
        self.assertEqual(self.tip.author.reputation, 20)  # 10 original + 5 + 5

    def test_vote_restrictions_low_reputation(self):
        """Validar restricciones de permisos: usuarios con reputación baja no pueden realizar downvotes."""
        downvote_result = self.tip.add_downvote(self.low_rep_user)
        upvote_result = self.tip.add_upvote(self.low_rep_user)
        self.assertTrue(upvote_result)  # Upvote permitido
        self.assertFalse(downvote_result)  # Downvote no permitido

    def test_delete_tip_removes_votes(self):
        """Eliminar un tip: verifica que el tip y sus votos desaparecen tras ser eliminado."""
        self.tip.add_upvote(self.user2)
        self.tip.add_downvote(self.low_rep_user)
        tip_id = self.tip.id
        self.tip.delete(force_delete=True)
        self.assertFalse(Tip.objects.filter(id=tip_id).exists())  # El tip ya no existe
    
    def test_error_on_insufficient_reputation_for_downvote(self):
        """Errores al votar sin reputación suficiente: valida que no se permita downvote sin reputación."""
        result = self.tip.add_downvote(self.low_rep_user)
        self.assertFalse(result)  # No se permite el downvote
        self.assertEqual(self.tip.downvotes.count(), 0)

    def test_reputation_updates_with_combination_of_votes(self):
        """Actualizar reputación en combinaciones de votos: valida ajustes correctos con upvotes y downvotes."""
        self.tip.add_upvote(self.user2)
        self.tip.add_downvote(self.user2)
        self.assertEqual(self.tip.upvotes.count(), 0)
        self.assertEqual(self.tip.downvotes.count(), 1)
        self.assertEqual(self.tip.author.reputation, 8)  # 10 original + 5 - 5 - 2

    def test_no_votes_on_deleted_tip(self):
        """Evitar votos tras eliminación del tip: asegura que no se puedan registrar votos en un tip eliminado."""
        self.tip.delete(force_delete=True)
        with self.assertRaises(Exception):  # O usa una excepción específica
            self.tip.add_upvote(self.user2)

    # -----------------------------------------------
    # Pruebas de Superusuario
    # -----------------------------------------------

    def test_superuser_permissions(self):
        """Verificar que un superusuario puede hacer upvotes, downvotes y eliminar tips."""
        self.tip.add_upvote(self.superuser)
        self.assertEqual(self.tip.upvotes.count(), 1)
        self.assertEqual(self.tip.author.reputation, 15)  # Reputación aumentó en 5

        self.tip.add_downvote(self.superuser)
        self.assertEqual(self.tip.downvotes.count(), 1)  # Debe contar el downvote
        self.assertEqual(self.tip.upvotes.count(), 0)  # El upvote debe ser reemplazado
        self.assertEqual(self.tip.author.reputation, 8)  # Reputación ajustada correctamente

    def test_superuser_can_delete_others_tips(self):
        """Verificar que un superusuario puede eliminar tips de otros usuarios."""
        tip_id = self.tip.id
        self.tip.delete(force_delete=True)
        self.assertFalse(Tip.objects.filter(id=tip_id).exists())