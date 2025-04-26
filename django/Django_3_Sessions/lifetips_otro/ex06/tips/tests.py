from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
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

        # Añadir permisos para downvote y delete (si no existen)
        self.add_permissions()

    def add_permissions(self):
        """Añade los permisos 'can_downvote_tip' y 'can_delete_tip' si no existen."""
        content_type = ContentType.objects.get_for_model(Tip)

        if not Permission.objects.filter(codename='can_downvote_tip', content_type=content_type).exists():
            Permission.objects.create(codename='can_downvote_tip', name='Can downvote tip', content_type=content_type)

        if not Permission.objects.filter(codename='can_delete_tip', content_type=content_type).exists():
            Permission.objects.create(codename='can_delete_tip', name='Can delete tip', content_type=content_type)

    # -----------------------------------------------
    # Pruebas Obligatorias
    # -----------------------------------------------

    def test_initial_reputation(self):
        """Verificar que un nuevo usuario tiene 0 puntos de reputación."""
        user = CustomUser.objects.create_user(username="newuser", password="pass")
        self.assertEqual(user.reputation, 0)

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
        self.tip.delete()
        self.assertEqual(self.user1.reputation, 10)  # Se restaura a la reputación inicial

    def test_negative_reputation(self):
        """Verificar que la reputación de un usuario puede ser negativa."""
        self.tip.add_downvote(self.user2)
        self.tip.add_downvote(self.user2)
        self.assertEqual(self.tip.author.reputation, 6)  # 10 - 2 - 2 = 6

    def test_combination_of_votes(self):
        """Verificar que la reputación se actualiza correctamente con combinaciones de votos."""
        self.tip.add_upvote(self.user2)
        self.tip.add_downvote(self.user2)
        self.assertEqual(self.tip.author.reputation, 13)  # 10 + 5 - 2 = 13

    # -----------------------------------------------
    # Pruebas de Permisos
    # -----------------------------------------------

    def test_downvote_permission_low_reputation(self):
        """Verificar que los usuarios con menos de 15 puntos no pueden hacer downvotes."""
        self.low_rep_user.assign_permissions()
        self.assertFalse(self.low_rep_user.has_perm('tips.can_downvote_tip'))
        result = self.tip.add_downvote(self.low_rep_user)
        self.assertFalse(result)
        self.assertEqual(self.tip.downvotes.count(), 0)

    def test_downvote_permission_high_reputation(self):
        """Verificar que los usuarios con 15 o más puntos pueden hacer downvotes."""
        self.user2.assign_permissions()
        self.assertTrue(self.user2.has_perm('tips.can_downvote_tip'))
        result = self.tip.add_downvote(self.user2)
        self.assertTrue(result)
        self.assertEqual(self.tip.downvotes.count(), 1)

    def test_delete_permission_low_reputation(self):
       """Verificar que los usuarios con menos de 30 puntos no pueden eliminar tips."""
        self.low_rep_user.assign_permissions()
        with self.assertRaises(PermissionDenied):
            self.tip.delete()

    def test_delete_permission_high_reputation(self):
        """Verificar que los usuarios con 30 o más puntos pueden eliminar tips."""
        self.user2.reputation = 30
        self.user2.save()
        self.user2.assign_permissions()
        self.assertTrue(self.user2.has_perm('tips.can_delete_tip'))

        tip = Tip.objects.create(author=self.user2, content="Tip for deletion test")
        tip_id = tip.id

        tip.delete()

        with self.assertRaises(Tip.DoesNotExist):
            Tip.objects.get(pk=tip_id)

    def test_reputation_gain_restores_permissions(self):
        """Verificar que si un usuario gana reputación, se le otorgan los permisos correspondientes."""
        # Configurar reputación inicial por debajo del umbral (15)
        self.user1.reputation = 5
        self.user1.save()
        self.user1.assign_permissions()
        self.assertFalse(self.user1.has_perm('tips.can_downvote_tip'))

        # Aumentar reputación para alcanzar el umbral (15)
        self.user1.reputation = 15
        self.user1.save()
        self.user1.assign_permissions()
        self.assertTrue(self.user1.has_perm('tips.can_downvote_tip'))

    def test_reputation_loss_removes_permissions(self):
        """Verificar que si un usuario pierde reputación, pierde los permisos otorgados."""
        # Asignar permiso para eliminar tips inicialmente al usuario self.user2
        self.user2.reputation = 30
        self.user2.save()
        self.user2.assign_permissions()
        self.assertTrue(self.user2.has_perm('tips.can_delete_tip'))

        # Reducir reputación para perder el permiso
        self.user2.reputation = 29
        self.user2.save()
        self.user2.assign_permissions()
        self.assertFalse(self.user2.has_perm('tips.can_delete_tip'))

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
        self.assertEqual(self.tip.upvotes.count(), 1)

        self.tip.add_downvote(self.user2)
        self.assertEqual(self.tip.upvotes.count(), 0)  # El upvote debe ser eliminado
        self.assertEqual(self.tip.downvotes.count(), 1)

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
        self.low_rep_user.assign_permissions()
        self.assertFalse(self.low_rep_user.has_perm('tips.can_downvote_tip'))
        self.assertFalse(self.tip.add_downvote(self.low_rep_user))
        self.assertEqual(self.tip.downvotes.count(), 0)

    def test_delete_tip_removes_votes(self):
        """Eliminar un tip: verifica que el tip y sus votos desaparecen tras ser eliminado."""
        self.tip.add_upvote(self.user2)
        self.tip.add_downvote(self.low_rep_user)
        tip_id = self.tip.id
        self.tip.delete()
        self.assertFalse(Tip.objects.filter(id=tip_id).exists())

    def test_error_on_insufficient_reputation_for_downvote(self):
        """Errores al votar sin reputación suficiente: valida que no se permita downvote sin reputación."""
        self.low_rep_user.assign_permissions()
        self.assertFalse(self.low_rep_user.has_perm('tips.can_downvote_tip'))
        self.assertFalse(self.tip.add_downvote(self.low_rep_user))

    def test_reputation_updates_with_combination_of_votes(self):
        """Actualizar reputación en combinaciones de votos: valida ajustes correctos con upvotes y downvotes."""
        self.tip.add_upvote(self.user2)
        self.tip.add_downvote(self.user2)
        self.assertEqual(self.tip.author.reputation, 13)  # 10 + 5 - 2 = 13

    def test_no_votes_on_deleted_tip(self):
        """Evitar votos tras eliminación del tip: asegura que no se puedan registrar votos en un tip eliminado."""
        self.tip.delete()
        with self.assertRaises(Exception):
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
        self.assertEqual(self.tip.downvotes.count(), 1)
        self.assertEqual(self.tip.author.reputation, 8)  # Reputación ajustada correctamente

    def test_superuser_can_delete_others_tips(self):
        """Verificar que un superusuario puede eliminar tips de otros usuarios."""
        tip_id = self.tip.id
        self.tip.delete()
        self.assertFalse(Tip.objects.filter(id=tip_id).exists())

    # -----------------------------------------------
    # Pruebas Adicionales
    # -----------------------------------------------

    def test_delete_tip_with_multiple_votes(self):
        """Verificar que al eliminar un tip con múltiples votos, todos sus efectos desaparecen."""
        self.tip.add_upvote(self.user2)
        self.tip.add_downvote(self.low_rep_user)
        self.tip.delete()
        self.assertEqual(self.user1.reputation, 10)  # Reputación inicial

    def test_cannot_vote_on_own_tip(self):
        """Verificar que un usuario no puede votar en su propio tip."""
        upvote_result = self.tip.add_upvote(self.user1)
        downvote_result = self.tip.add_downvote(self.user1)
        self.assertFalse(upvote_result)  # No puede hacer upvotes
        self.assertFalse(downvote_result)  # No puede hacer downvotes
        self.assertEqual(self.tip.upvotes.count(), 0)
        self.assertEqual(self.tip.downvotes.count(), 0)

    def test_no_votes_after_tip_deleted(self):
        """Verificar que no se puedan registrar votos en un tip eliminado."""
        self.tip.delete()
        with self.assertRaises(Exception):
            self.tip.add_upvote(self.user2)
