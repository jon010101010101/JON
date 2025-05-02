from django.test import TestCase
from tips.models import CustomUser, Tip


class PruebasSistemaReputacion(TestCase):
    """
    Pruebas para el sistema de reputación y permisos.
    """

    test_results = []  # Mover test_results a un atributo de clase

    def setUp(self):
        """Configurar datos iniciales para los casos de prueba."""
        self.user1 = CustomUser.objects.create_user(username="Usuario1", reputation=0)
        self.user2 = CustomUser.objects.create_user(username="Usuario2", reputation=15)
        self.user3 = CustomUser.objects.create_user(username="Usuario3", reputation=30)
        self.tip = Tip.objects.create(author=self.user1, content="Este es un tip.")

    def print_test_details(self, description, before, action, after, passed):
        """
        Imprime los detalles de cada prueba y almacena los resultados.
        """
        status = "PASSED ✅" if passed else "FAILED ❌"
        print(f"\n🔍 {description}")
        print(f"    Antes: {before}")
        print(f"    Acción: {action}")
        print(f"    Después: {after}")
        print(f"    Resultado: {status}\n")
        PruebasSistemaReputacion.test_results.append((description, passed))

    def test_01_reputacion_inicial(self):
        """01: Verificar que los nuevos usuarios comiencen con 0 de reputación."""
        description = "Test 01: Verificar que la reputación inicial del usuario sea 0."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Comprobar el valor inicial."
        try:
            self.assertEqual(self.user1.reputation, 0)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_02_upvote_aumenta_reputacion(self):
        """02: Verificar que los upvotes aumenten la reputación del autor."""
        description = "Test 02: Verificar que un upvote aumenta la reputación del autor."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Dar un upvote al tip."
        try:
            self.tip.upvote(self.user2)
            self.assertEqual(self.user1.reputation, 5)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_03_downvote_disminuye_reputacion(self):
        """03: Verificar que los downvotes disminuyan la reputación del autor."""
        description = "Test 03: Verificar que un downvote disminuye la reputación del autor."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Dar un downvote al tip."
        try:
            self.tip.downvote(self.user2)
            self.assertEqual(self.user1.reputation, -2)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_04_permiso_para_downvote(self):
        """04: Verificar que los usuarios desbloqueen el permiso de downvote con 15 puntos de reputación."""
        description = "Test 04: Verificar que los usuarios desbloqueen el permiso de downvote con 15 puntos de reputación."
        before = f"Reputación del usuario: {self.user2.reputation}"
        action = "Comprobar si puede dar un downvote."
        try:
            self.assertTrue(self.user2.can_downvote)
            passed = True
        except AssertionError:
            passed = False
        after = f"¿Puede dar downvote?: {self.user2.can_downvote}"
        self.print_test_details(description, before, action, after, passed)

    def test_05_permiso_para_eliminar_tip(self):
        """05: Verificar que los usuarios desbloqueen el permiso de eliminar tips con 30 puntos de reputación."""
        description = "Test 05: Verificar que los usuarios desbloqueen el permiso de eliminar tips con 30 puntos de reputación."
        before = f"Reputación del usuario: {self.user3.reputation}"
        action = "Comprobar si puede eliminar un tip."
        try:
            self.assertTrue(self.user3.can_delete_tips)
            passed = True
        except AssertionError:
            passed = False
        after = f"¿Puede eliminar tips?: {self.user3.can_delete_tips}"
        self.print_test_details(description, before, action, after, passed)

    def test_06_eliminar_tip_elimina_influencia_reputacion(self):
        """06: Verificar que al eliminar un tip se elimine su influencia en la reputación."""
        description = "Test 06: Verificar que al eliminar un tip se elimine su influencia en la reputación."
        before = f"Reputación inicial del autor: {self.user1.reputation}"
        action = "Dar un upvote al tip y luego eliminarlo."
        try:
            self.tip.upvote(self.user2)
            self.tip.delete(user=self.user1)
            self.assertEqual(self.user1.reputation, 0)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final del autor: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_07_no_se_permite_self_upvote(self):
        """07: Verificar que los usuarios no puedan dar upvote a sus propios tips."""
        description = "Test 07: Verificar que los usuarios no puedan dar upvote a sus propios tips."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Intentar dar un upvote a un tip propio."
        try:
            with self.assertRaises(PermissionError):
                self.tip.upvote(self.user1)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_08_no_se_permite_self_downvote(self):
        """08: Verificar que los usuarios no puedan dar downvote a sus propios tips."""
        description = "Test 08: Verificar que los usuarios no puedan dar downvote a sus propios tips."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Intentar dar un downvote a un tip propio."
        try:
            with self.assertRaises(PermissionError):
                self.tip.downvote(self.user1)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_09_no_se_puede_dar_upvote_dos_veces(self):
        """09: Verificar que los usuarios no puedan dar upvote al mismo tip varias veces."""
        description = "Test 09: Verificar que los usuarios no puedan dar upvote al mismo tip varias veces."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Intentar dar un segundo upvote al mismo tip."
        try:
            self.tip.upvote(self.user2)
            with self.assertRaises(PermissionError):
                self.tip.upvote(self.user2)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_10_no_se_puede_dar_downvote_dos_veces(self):
        """10: Verificar que los usuarios no puedan dar downvote al mismo tip varias veces."""
        description = "Test 10: Verificar que los usuarios no puedan dar downvote al mismo tip varias veces."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Intentar dar un segundo downvote al mismo tip."
        try:
            self.tip.downvote(self.user2)
            with self.assertRaises(PermissionError):
                self.tip.downvote(self.user2)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_11_upvotes_multiples_de_usuarios_diferentes(self):
        """11: Verificar que un tip reciba la reputación correcta con múltiples upvotes."""
        description = "Test 11: Verificar que un tip reciba la reputación correcta con múltiples upvotes."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Dar upvotes al tip desde varios usuarios."
        try:
            self.tip.upvote(self.user2)
            self.tip.upvote(self.user3)
            self.assertEqual(self.user1.reputation, 10)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_12_downvotes_multiples_de_usuarios_diferentes(self):
        """12: Verificar que un tip reciba la reputación correcta con múltiples downvotes."""
        description = "Test 12: Verificar que un tip reciba la reputación correcta con múltiples downvotes."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Dar downvotes al tip desde varios usuarios."
        try:
            self.tip.downvote(self.user2)
            self.tip.downvote(self.user3)
            self.assertEqual(self.user1.reputation, -4)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_13_calculo_reputacion_tip(self):
        """13: Verificar que la reputación se calcule correctamente después de votos mixtos."""
        description = "Test 13: Verificar que la reputación se calcule correctamente después de votos mixtos."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Dar votos mixtos al tip."
        try:
            self.tip.upvote(self.user2)
            self.tip.downvote(self.user3)
            self.assertEqual(self.user1.reputation, 3)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_14_reputacion_no_puede_ser_negativa(self):
        """14: Verificar que la reputación no pueda bajar de un umbral determinado."""
        description = "Test 14: Verificar que la reputación no pueda bajar de un umbral determinado (-20)."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Intentar reducir la reputación por debajo del límite con múltiples usuarios."
        try:
            # Creamos usuarios adicionales para simular múltiples downvotes
            extra_users = [
                CustomUser.objects.create_user(username=f"UsuarioExtra{i}", reputation=0)
                for i in range(10)
            ]
            for user in extra_users:
                self.tip.downvote(user)

            self.assertGreaterEqual(self.user1.reputation, -20)  # La reputación no debe bajar de -20
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    def test_15_no_autor_no_puede_eliminar_tip(self):
        """15: Verificar que solo el autor o un administrador puedan eliminar un tip."""
        description = "Test 15: Verificar que solo el autor o un administrador puedan eliminar un tip."
        before = "Intento de eliminación por un usuario no autorizado."
        action = "Eliminar el tip con un usuario no autorizado."
        try:
            with self.assertRaises(PermissionError):
                self.tip.delete(user=self.user2)
            passed = True
        except AssertionError:
            passed = False
        after = "El tip no fue eliminado."
        self.print_test_details(description, before, action, after, passed)

    def test_16_admin_puede_eliminar_cualquier_tip(self):
        """16: Verificar que un usuario administrador pueda eliminar cualquier tip."""
        description = "Test 16: Verificar que un usuario administrador pueda eliminar cualquier tip."
        before = "Intento de eliminación por un administrador."
        action = "Eliminar el tip con un usuario administrador."
        admin = CustomUser.objects.create_user(username="Admin", reputation=50, is_superuser=True)
        try:
            self.tip.delete(user=admin)
            passed = True
        except AssertionError:
            passed = False
        after = "El tip fue eliminado exitosamente."
        self.print_test_details(description, before, action, after, passed)

    def test_17_representacion_usuario(self):
        """17: Verificar que la representación en cadena del usuario incluya su reputación."""
        description = "Test 17: Verificar que la representación en cadena del usuario incluya su reputación."
        before = f"Reputación inicial del usuario: {self.user1.reputation}"
        action = "Mostrar la representación del usuario."
        try:
            self.assertEqual(str(self.user1), "Usuario1 (0 rep)")
            passed = True
        except AssertionError:
            passed = False
        after = f"Representación final: {str(self.user1)}"
        self.print_test_details(description, before, action, after, passed)

    @classmethod
    def tearDownClass(cls):
        """Imprimir un resumen al final de todas las pruebas."""
        super().tearDownClass()
        print("\nResumen Final:")
        total_tests = len(cls.test_results)
        passed_tests = sum(1 for _, passed in cls.test_results if passed)
        failed_tests = total_tests - passed_tests

        for description, passed in cls.test_results:
            status = "PASSED ✅" if passed else "FAILED ❌"
            print(f"  {description}: {status}")

        if failed_tests == 0:
            print(f"\n✅ {total_tests} pruebas pasaron exitosamente.\n")
        else:
            print(f"\n❌ {failed_tests} de {total_tests} pruebas fallaron.\n")