from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Tip
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Permission

<<<<<<< HEAD
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
=======

class PruebasSistemaReputacion(TestCase):
    """
    Pruebas para el sistema de reputación y permisos.
    """

    def setUp(self):
        """Configurar datos iniciales para los casos de prueba."""
        self.user1 = CustomUser.objects.create_user(username="Usuario1", reputation=0)
        self.user2 = CustomUser.objects.create_user(username="Usuario2", reputation=15)
        self.user3 = CustomUser.objects.create_user(username="Usuario3", reputation=30)
        self.tip = Tip.objects.create(author=self.user1, content="Este es un tip.")

    def test_01_reputacion_inicial(self):
        """Verificar que los nuevos usuarios comiencen con 0 de reputación."""
>>>>>>> aa7cf094 (Remove unused files and clean up project)
        self.assertEqual(self.user1.reputation, 0)
        self.assertEqual(self.user2.reputation, 15)
        self.assertEqual(self.user3.reputation, 30)

<<<<<<< HEAD
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
=======
    def test_02_upvote_aumenta_reputacion(self):
        """Verificar que los upvotes aumenten la reputación del autor."""
        self.tip.upvote(self.user2)
        self.assertEqual(self.user1.reputation, 5)

    def test_03_downvote_disminuye_reputacion(self):
        """Verificar que los downvotes disminuyan la reputación del autor."""
        self.tip.downvote(self.user2)
        self.assertEqual(self.user1.reputation, -2)

    def test_04_permiso_para_downvote(self):
        """Verificar que los usuarios desbloqueen el permiso de downvote con 15 puntos de reputación."""
        self.assertTrue(self.user2.can_downvote)

    def test_05_permiso_para_eliminar_tip(self):
        """Verificar que los usuarios desbloqueen el permiso de eliminar tips con 30 puntos de reputación."""
        self.assertTrue(self.user3.can_delete_tips)

    def test_06_eliminar_tip_elimina_influencia_reputacion(self):
        """Verificar que al eliminar un tip se elimine su influencia en la reputación."""
        self.tip.upvote(self.user2)
        self.tip.delete(user=self.user1)
        self.assertEqual(self.user1.reputation, 0)

    def test_07_no_se_permite_self_upvote(self):
        """Verificar que los usuarios no puedan dar upvote a sus propios tips."""
        with self.assertRaises(PermissionError):
            self.tip.upvote(self.user1)

    def test_08_no_se_permite_self_downvote(self):
        """Verificar que los usuarios no puedan dar downvote a sus propios tips."""
        with self.assertRaises(PermissionError):
            self.tip.downvote(self.user1)

    def test_09_no_se_puede_dar_upvote_dos_veces(self):
        """Verificar que los usuarios no puedan dar upvote al mismo tip varias veces."""
        self.tip.upvote(self.user2)
        with self.assertRaises(PermissionError):
            self.tip.upvote(self.user2)

    def test_10_no_se_puede_dar_downvote_dos_veces(self):
        """Verificar que los usuarios no puedan dar downvote al mismo tip varias veces."""
        self.tip.downvote(self.user2)
        with self.assertRaises(PermissionError):
            self.tip.downvote(self.user2)

    def test_11_upvotes_multiples_de_usuarios_diferentes(self):
        """Verificar que un tip reciba la reputación correcta con múltiples upvotes."""
        self.tip.upvote(self.user2)
        self.tip.upvote(self.user3)
        self.assertEqual(self.user1.reputation, 10)

    def test_12_downvotes_multiples_de_usuarios_diferentes(self):
        """Verificar que un tip reciba la reputación correcta con múltiples downvotes."""
        self.tip.downvote(self.user2)
        self.tip.downvote(self.user3)
        self.assertEqual(self.user1.reputation, -4)

    def test_13_calculo_reputacion_tip(self):
        """Verificar que la reputación se calcule correctamente después de votos mixtos."""
        self.tip.upvote(self.user2)  # +5
        self.tip.downvote(self.user3)  # -2
        self.assertEqual(self.user1.reputation, 3)

    def test_14_reputacion_no_puede_ser_negativa(self):
        """Verificar que la reputación no pueda bajar de un umbral determinado."""
        # Crear usuarios adicionales para realizar downvotes
        usuarios_extra = [
            CustomUser.objects.create_user(username=f"UsuarioExtra{i}", reputation=0)
            for i in range(1, 11)  # Crear 10 usuarios adicionales
        ]

        # Aplicar downvotes al Tip para reducir la reputación del autor
        for usuario in usuarios_extra:
            self.tip.downvote(usuario)

        # Refrescar la reputación del autor después de aplicar todos los downvotes
        self.user1.refresh_from_db()

        # Verificar que la reputación no baje de -20
        self.assertEqual(self.user1.reputation, -20)

    def test_15_no_autor_no_puede_eliminar_tip(self):
        """Verificar que solo el autor o un administrador puedan eliminar un tip."""
        with self.assertRaises(PermissionError):
            self.tip.delete(user=self.user2)
        self.tip.delete(user=self.user1)  # El autor elimina su propio tip
        self.assertFalse(Tip.objects.filter(id=self.tip.id).exists())

    def test_16_admin_puede_eliminar_cualquier_tip(self):
        """Verificar que un usuario administrador pueda eliminar cualquier tip."""
        usuario_admin = CustomUser.objects.create_user(username="Admin", reputation=50, is_superuser=True)
        self.tip.delete(user=usuario_admin)
        self.assertFalse(Tip.objects.filter(id=self.tip.id).exists())

    def test_17_representacion_usuario(self):
        """Verificar que la representación en cadena del usuario incluya su reputación."""
        self.user1.reputation = 10
        self.user1.save()
        self.assertEqual(str(self.user1), "Usuario1 (10 rep)")
>>>>>>> aa7cf094 (Remove unused files and clean up project)
