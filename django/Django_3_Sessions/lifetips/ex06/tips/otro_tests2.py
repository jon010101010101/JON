from django.test import TestCase
from tips.models import CustomUser, Tip


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
        """01: Verificar que los nuevos usuarios comiencen con 0 de reputación."""
        self.assertEqual(self.user1.reputation, 0)

    def test_02_upvote_aumenta_reputacion(self):
        """02: Verificar que los upvotes aumenten la reputación del autor."""
        self.tip.upvote(self.user2)
        self.assertEqual(self.user1.reputation, 5)

    def test_03_downvote_disminuye_reputacion(self):
        """03: Verificar que los downvotes disminuyan la reputación del autor."""
        self.tip.downvote(self.user2)
        self.assertEqual(self.user1.reputation, -2)

    def test_04_permiso_para_downvote(self):
        """04: Verificar que los usuarios desbloqueen el permiso de downvote con 15 puntos de reputación."""
        self.assertTrue(self.user2.can_downvote)

    def test_05_permiso_para_eliminar_tip(self):
        """05: Verificar que los usuarios desbloqueen el permiso de eliminar tips con 30 puntos de reputación."""
        self.assertTrue(self.user3.can_delete_tips)

    def test_06_eliminar_tip_elimina_influencia_reputacion(self):
        """06: Verificar que al eliminar un tip se elimine su influencia en la reputación."""
        self.tip.upvote(self.user2)
        self.tip.delete(user=self.user1)
        self.assertEqual(self.user1.reputation, 0)

    def test_07_no_se_permite_self_upvote(self):
        """07: Verificar que los usuarios no puedan dar upvote a sus propios tips."""
        with self.assertRaises(PermissionError):
            self.tip.upvote(self.user1)

    def test_08_no_se_permite_self_downvote(self):
        """08: Verificar que los usuarios no puedan dar downvote a sus propios tips."""
        with self.assertRaises(PermissionError):
            self.tip.downvote(self.user1)

    def test_09_no_se_puede_dar_upvote_dos_veces(self):
        """09: Verificar que los usuarios no puedan dar upvote al mismo tip varias veces."""
        self.tip.upvote(self.user2)
        with self.assertRaises(PermissionError):
            self.tip.upvote(self.user2)

    def test_10_no_se_puede_dar_downvote_dos_veces(self):
        """10: Verificar que los usuarios no puedan dar downvote al mismo tip varias veces."""
        self.tip.downvote(self.user2)
        with self.assertRaises(PermissionError):
            self.tip.downvote(self.user2)

    def test_11_upvotes_multiples_de_usuarios_diferentes(self):
        """11: Verificar que un tip reciba la reputación correcta con múltiples upvotes."""
        self.tip.upvote(self.user2)
        self.tip.upvote(self.user3)
        self.assertEqual(self.user1.reputation, 10)

    def test_12_downvotes_multiples_de_usuarios_diferentes(self):
        """12: Verificar que un tip reciba la reputación correcta con múltiples downvotes."""
        self.tip.downvote(self.user2)
        self.tip.downvote(self.user3)
        self.assertEqual(self.user1.reputation, -4)

    def test_13_calculo_reputacion_tip(self):
        """13: Verificar que la reputación se calcule correctamente después de votos mixtos."""
        self.tip.upvote(self.user2)  # +5
        self.tip.downvote(self.user3)  # -2
        self.assertEqual(self.user1.reputation, 3)

    def test_14_reputacion_no_puede_ser_negativa(self):
        """14: Verificar que la reputación no pueda bajar de un umbral determinado."""
        usuarios_extra = [
            CustomUser.objects.create_user(username=f"UsuarioExtra{i}", reputation=0)
            for i in range(1, 11)  # Crear 10 usuarios adicionales
        ]

        for usuario in usuarios_extra:
            self.tip.downvote(usuario)

        self.user1.refresh_from_db()
        self.assertEqual(self.user1.reputation, -20)

    def test_15_no_autor_no_puede_eliminar_tip(self):
        """15: Verificar que solo el autor o un administrador puedan eliminar un tip."""
        with self.assertRaises(PermissionError):
            self.tip.delete(user=self.user2)
        self.tip.delete(user=self.user1)
        self.assertFalse(Tip.objects.filter(id=self.tip.id).exists())

    def test_16_admin_puede_eliminar_cualquier_tip(self):
        """16: Verificar que un usuario administrador pueda eliminar cualquier tip."""
        usuario_admin = CustomUser.objects.create_user(username="Admin", reputation=50, is_superuser=True)
        self.tip.delete(user=usuario_admin)
        self.assertFalse(Tip.objects.filter(id=self.tip.id).exists())

    def test_17_representacion_usuario(self):
        """17: Verificar que la representación en cadena del usuario incluya su reputación."""
        self.user1.reputation = 10
        self.user1.save()
        self.assertEqual(str(self.user1), "Usuario1 (10 rep)")