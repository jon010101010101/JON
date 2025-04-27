from django.test import TestCase
from tips.models import CustomUser, Tip


class ReputationSystemTestCase(TestCase):
    """
    Pruebas para el sistema de reputación y permisos.
    """

    def setUp(self):
        """Set up initial data for test cases."""
        self.user1 = CustomUser.objects.create_user(username="User1", reputation=0)
        self.user2 = CustomUser.objects.create_user(username="User2", reputation=15)
        self.user3 = CustomUser.objects.create_user(username="User3", reputation=30)
        self.tip = Tip.objects.create(author=self.user1, content="This is a tip.")

    def test_01_initial_reputation(self):
        """Verify that new users start with 0 reputation."""
        self.assertEqual(self.user1.reputation, 0)

    def test_02_upvote_increases_reputation(self):
        """Verify that upvotes increase the author's reputation."""
        self.tip.upvote(self.user2)
        self.assertEqual(self.user1.reputation, 5)

    def test_03_downvote_decreases_reputation(self):
        """Verify that downvotes decrease the author's reputation."""
        self.tip.downvote(self.user2)
        self.assertEqual(self.user1.reputation, -2)

    def test_04_downvote_permission(self):
        """Verify that users unlock downvote permissions at 15 reputation points."""
        self.assertTrue(self.user2.can_downvote)

    def test_05_delete_tip_permission(self):
        """Verify that users unlock delete permissions at 30 reputation points."""
        self.assertTrue(self.user3.can_delete_tips)

    def test_06_delete_tip_removes_reputation_influence(self):
        """Verify that deleting a tip removes its influence on reputation."""
        self.tip.upvote(self.user2)
        self.tip.delete(user=self.user1)
        self.assertEqual(self.user1.reputation, 0)

    def test_07_self_upvote_not_allowed(self):
        """Verify that users cannot upvote their own tips."""
        with self.assertRaises(PermissionError):
            self.tip.upvote(self.user1)

    def test_08_self_downvote_not_allowed(self):
        """Verify that users cannot downvote their own tips."""
        with self.assertRaises(PermissionError):
            self.tip.downvote(self.user1)

    def test_09_cannot_upvote_twice(self):
        """Verify that users cannot upvote the same tip multiple times."""
        self.tip.upvote(self.user2)
        with self.assertRaises(PermissionError):
            self.tip.upvote(self.user2)

    def test_10_cannot_downvote_twice(self):
        """Verify that users cannot downvote the same tip multiple times."""
        self.tip.downvote(self.user2)
        with self.assertRaises(PermissionError):
            self.tip.downvote(self.user2)

    def test_11_multiple_upvotes_from_different_users(self):
        """Verify that a tip receives the correct reputation with multiple upvotes."""
        self.tip.upvote(self.user2)
        self.tip.upvote(self.user3)
        self.assertEqual(self.user1.reputation, 10)

    def test_12_multiple_downvotes_from_different_users(self):
        """Verify that a tip receives the correct reputation with multiple downvotes."""
        self.tip.downvote(self.user2)
        self.tip.downvote(self.user3)
        self.assertEqual(self.user1.reputation, -4)

    def test_13_tip_reputation_calculation(self):
        """Verify that reputation is calculated correctly after mixed votes."""
        self.tip.upvote(self.user2)  # +5
        self.tip.downvote(self.user3)  # -2
        self.assertEqual(self.user1.reputation, 3)

    def test_14_reputation_cannot_be_negative(self):
        """Verify that reputation cannot go below a certain threshold."""
        # Crear usuarios adicionales para realizar downvotes
        extra_users = [
            CustomUser.objects.create_user(username=f"ExtraUser{i}", reputation=0)
            for i in range(1, 11)  # Crear 10 usuarios adicionales
        ]

        # Aplicar downvotes al Tip para reducir la reputación del autor
        for user in extra_users:
            self.tip.downvote(user)

        # Refrescar la reputación del autor después de aplicar todos los downvotes
        self.user1.refresh_from_db()

        # Verificar que la reputación no baje de -20
        self.assertEqual(self.user1.reputation, -20)

    def test_15_tip_cannot_be_deleted_by_non_author(self):
        """Verify that only the author or an admin can delete a tip."""
        with self.assertRaises(PermissionError):
            self.tip.delete(user=self.user2)
        self.tip.delete(user=self.user1)  # Author deletes their own tip
        self.assertFalse(Tip.objects.filter(id=self.tip.id).exists())

    def test_16_admin_can_delete_any_tip(self):
        """Verify that an admin user can delete any tip."""
        admin_user = CustomUser.objects.create_user(username="Admin", reputation=50, is_superuser=True)
        self.tip.delete(user=admin_user)
        self.assertFalse(Tip.objects.filter(id=self.tip.id).exists())

    def test_17_user_representation(self):
        """Verify that the user's string representation includes their reputation."""
        self.user1.reputation = 10
        self.user1.save()
        self.assertEqual(str(self.user1), "User1 (10 rep)")