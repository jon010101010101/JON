import sys
sys.path.insert(0, '/home/jurrutia/sgoinfre/lifetips_git_clone/lifetips/ex06')

from django.test import TestCase
from tips.models import CustomUser, Tip
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model


class PruebasSistemaReputacion(TestCase):
    """
    Pruebas para el sistema de reputación y permisos.
    """
    test_results = []

    def setUp(self):
        """Configurar datos iniciales para los casos de prueba."""
        self.user1 = CustomUser.objects.create_user(username="Usuario1", reputation=0)
        self.user2 = CustomUser.objects.create_user(username="Usuario2", reputation=15)
        self.user3 = CustomUser.objects.create_user(username="Usuario3", reputation=30)
        self.user_sin_reputacion = CustomUser.objects.create_user(username="SinRepu", reputation=0)
        self.admin = CustomUser.objects.create_superuser(username="Admin", password="adminpass", reputation=100)
        self.tip = Tip.objects.create(author=self.user1, content="Este es un tip.")

    def print_test_details(self, description, before, action, after, passed):
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
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Eliminar un tip siendo el autor."
        try:
            self.tip.delete(user=self.user1)
            passed = True
        except PermissionDenied:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)


    def test_07_no_se_permite_self_upvote(self):
        """07: Verificar que los usuarios no puedan dar upvote a sus propios tips."""
        description = "Test 07: Verificar que los usuarios no puedan dar upvote a sus propios tips."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Intentar dar un upvote a un tip propio."
        try:
            with self.assertRaises(PermissionDenied):
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
            with self.assertRaises(PermissionDenied):
                self.tip.downvote(self.user1)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}"
        self.print_test_details(description, before, action, after, passed)


    def test_09_no_se_puede_dar_upvote_dos_veces(self):
        """09: Verificar que los usuarios no puedan dar upvote al mismo tip varias veces."""
        description = "Test 09: Verificar que los usuarios no puedan dar upvote al mismo tip varias veces."
        before = f"Reputación inicial: {self.user2.reputation}"
        action = "Intentar dar upvote dos veces al mismo tip."
        try:
            self.tip.upvote(self.user2)  # Primer upvote (debería funcionar)
            with self.assertRaises(PermissionDenied):
                self.tip.upvote(self.user2)  # Segundo upvote (debe fallar)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user2.reputation}"
        self.print_test_details(description, before, action, after, passed)


    def test_10_no_se_puede_dar_downvote_dos_veces(self):
        """10: Verificar que los usuarios no puedan dar downvote al mismo tip varias veces."""
        description = "Test 10: Verificar que los usuarios no puedan dar downvote al mismo tip varias veces."
        before = f"Reputación inicial: {self.user2.reputation}"
        action = "Intentar dar downvote dos veces al mismo tip."
        try:
            self.tip.downvote(self.user2)  # Primer downvote (debería funcionar)
            with self.assertRaises(PermissionDenied):
                self.tip.downvote(self.user2)  # Segundo downvote (debe fallar)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user2.reputation}"
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

    from django.core.exceptions import PermissionDenied

    def test_14_reputacion_no_puede_ser_negativa(self):
        """14: Verificar que la reputación no pueda bajar de un umbral determinado."""
        description = "Test 14: Verificar que la reputación no pueda bajar de un umbral determinado."
        before = f"Reputación inicial: {self.user_sin_reputacion.reputation}"
        action = "Intentar hacer downvote sin reputación suficiente."
        try:
            with self.assertRaises(PermissionDenied):
                self.tip.downvote(self.user_sin_reputacion)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user_sin_reputacion.reputation}"
        self.print_test_details(description, before, action, after, passed)


    def test_15_no_autor_no_puede_eliminar_tip(self):
        """15: Verificar que solo el autor o un administrador puedan eliminar un tip."""
        description = "Test 15: Verificar que solo el autor o un administrador puedan eliminar un tip."
        before = f"Reputación inicial: {self.user2.reputation}"
        action = "Intentar eliminar un tip siendo un usuario que no es autor ni admin."
        passed = False
        try:
            with self.assertRaises(PermissionDenied):
                self.tip.delete(user=self.user2)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user2.reputation}"
        self.print_test_details(description, before, action, after, passed)



    def test_16_admin_puede_eliminar_cualquier_tip(self):
        """16: Verificar que un usuario administrador pueda eliminar cualquier tip."""
        description = "Test 16: Verificar que un usuario administrador pueda eliminar cualquier tip."
        before = f"Reputación inicial: {self.admin.reputation}"
        action = "Intentar eliminar un tip siendo admin."
        try:
            self.tip.delete(user=self.admin)
            passed = True
        except Exception:
            passed = False
        after = f"Reputación final: {self.admin.reputation}"
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

    def test_18_pierde_permiso_downvote_si_baja_reputacion(self):
        """18: Verificar que el usuario pierde el permiso de downvote si su reputación baja de 15."""
        description = "Test 18: Verificar que el usuario pierde el permiso de downvote si su reputación baja de 15."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Subir reputación a 15, luego bajarla a 13."
        try:
            self.user1.reputation = 15
            self.assertTrue(self.user1.can_downvote)
            self.user1.reputation = 13
            self.assertFalse(self.user1.can_downvote)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}, ¿Puede downvotar?: {self.user1.can_downvote}"
        self.print_test_details(description, before, action, after, passed)

    def test_19_pierde_permiso_delete_si_baja_reputacion(self):
        """19: Verificar que el usuario pierde el permiso de eliminar tips si su reputación baja de 30."""
        description = "Test 19: Verificar que el usuario pierde el permiso de eliminar tips si su reputación baja de 30."
        before = f"Reputación inicial: {self.user1.reputation}"
        action = "Subir reputación a 30, luego bajarla a 28."
        try:
            self.user1.reputation = 30
            self.assertTrue(self.user1.can_delete_tips)
            self.user1.reputation = 28
            self.assertFalse(self.user1.can_delete_tips)
            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {self.user1.reputation}, ¿Puede eliminar tips?: {self.user1.can_delete_tips}"
        self.print_test_details(description, before, action, after, passed)
       
    def test_20_consistencia_reputacion(self):
        """
        Test 20: La reputación del usuario refleja siempre la suma real de los votos de sus tips,
        incluso tras borrar tips o recibir muchos votos. No debe dispararse a valores absurdos.
        """
        from django.contrib.auth import get_user_model
        User = get_user_model()
        description = "Test 20: Verificar que la reputación del usuario refleja siempre la suma real de los votos de sus tips."
        before = "Reputación inicial: 0"
        action = "Votar, borrar tips, crear muchos tips con upvotes, borrar todos los tips."
        try:
            # Crear dos usuarios
            user1 = User.objects.create_user(username='user_global1', password='userpass')
            user2 = User.objects.create_user(username='user_global2', password='userpass')
            # Crear dos tips de user1
            tip1 = Tip.objects.create(title="Tip1", content="Contenido 1", author=user1)
            tip2 = Tip.objects.create(title="Tip2", content="Contenido 2", author=user1)

            # user2 upvota ambos tips de user1
            tip1.upvotes.add(user2)
            tip2.upvotes.add(user2)
            tip1.save()
            tip2.save()
            user1.refresh_from_db()
            self.assertEqual(user1.reputation, 10)  # 2 upvotes x 5

            # user2 downvota tip2 (quita el upvote primero)
            tip2.upvotes.remove(user2)
            tip2.downvotes.add(user2)
            tip2.save()
            user1.refresh_from_db()
            self.assertEqual(user1.reputation, 3)  # 1 upvote (tip1), 1 downvote (tip2): 5 - 2

            # Borra tip1, solo queda tip2 con un downvote
            tip1.delete()
            user1.refresh_from_db()
            self.assertEqual(user1.reputation, -2)  # Solo 1 downvote

            # Borra tip2, ya no tiene tips
            tip2.delete()
            user1.refresh_from_db()
            self.assertEqual(user1.reputation, 0)  # Sin tips

            # Crea 20 tips y les pone 10 upvotes cada uno
            for i in range(20):
                tip = Tip.objects.create(title=f"Tip{i}", content="Muchos votos", author=user1)
                for _ in range(10):
                    voter = User.objects.create_user(username=f"voter{i}_{_}", password="pw")
                    tip.upvotes.add(voter)
                tip.save()
            user1.refresh_from_db()
            self.assertEqual(user1.reputation, 1000)  # 20*10*5

            # Borra todos los tips
            Tip.objects.filter(author=user1).delete()
            user1.refresh_from_db()
            self.assertEqual(user1.reputation, 0)  # Sin tips

            passed = True
        except AssertionError:
            passed = False
        after = f"Reputación final: {user1.reputation}"
        self.print_test_details(description, before, action, after, passed)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        print("\nResumen Final:")
        total_tests = len(cls.test_results)
        passed_tests = sum(1 for _, passed in cls.test_results if passed)
        failed_tests = total_tests - passed_tests

        for description, passed in cls.test_results:
            status = "PASSED ✅" if passed else "FAILED ❌"
            print(f"  {description}: {status}")

        if failed_tests == 0:
            print(f"\n✅ {total_tests} pruebas pasaron con éxito.\n")
        else:
            print(f"\n❌ {failed_tests} de {total_tests} pruebas fallaron.\n")



# python manage.py test tips.prueba
                             

