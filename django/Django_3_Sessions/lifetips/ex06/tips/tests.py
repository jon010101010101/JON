from django.test import TestCase
from .models import CustomUser, Tip


class ReputationSystemTestCase(TestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(username="User1", reputation=0)
        self.user2 = CustomUser.objects.create_user(username="User2", reputation=15)
        self.user3 = CustomUser.objects.create_user(username="User3", reputation=30)
        self.tip = Tip.objects.create(author=self.user1, content="This is a tip.")

    # Tests básicos para verificar el cumplimiento del enunciado
    def test_initial_reputation(self):
        """Verify that new users start with 0 reputation."""
        self.assertEqual(self.user1.reputation, 0)

    def test_upvote_increases_reputation(self):
        """Verify that upvotes increase the author's reputation."""
        self.tip.add_upvote(self.user2)
        self.assertEqual(self.user1.reputation, 5)

    def test_downvote_decreases_reputation(self):
        """Verify that downvotes decrease the author's reputation."""
        self.tip.add_downvote(self.user2)
        self.assertEqual(self.user1.reputation, -2)

    def test_downvote_permission(self):
        """Verify that users unlock downvote permissions at 15 reputation points."""
        self.assertTrue(self.user2.can_downvote())
        self.assertFalse(self.user1.can_downvote())

    def test_delete_tip_permission(self):
        """Verify that users unlock delete permissions at 30 reputation points."""
        self.assertFalse(self.user1.can_delete_tips())
        self.user1.reputation = 30
        self.user1.save()
        self.assertTrue(self.user1.can_delete_tips())

    def test_delete_tip_removes_reputation_influence(self):
        """Verify that deleting a tip removes its influence on reputation."""
        self.tip.add_upvote(self.user2)  # +5 reputation
        self.tip.delete()
        self.assertEqual(self.user1.reputation, 0)

    def test_self_upvote_not_allowed(self):
        """Verify that users cannot upvote their own tips."""
        with self.assertRaises(PermissionError):
            self.tip.add_upvote(self.user1)

    def test_self_downvote_not_allowed(self):
        """Verify that users cannot downvote their own tips."""
        with self.assertRaises(PermissionError):
            self.tip.add_downvote(self.user1)

    # Tests adicionales para ampliar la cobertura
    def test_cannot_upvote_twice(self):
        """Verify that users cannot upvote the same tip multiple times."""
        self.tip.add_upvote(self.user2)
        with self.assertRaises(PermissionError):
            self.tip.add_upvote(self.user2)
        self.assertEqual(self.user1.reputation, 5)

    def test_cannot_downvote_twice(self):
        """Verify that users cannot downvote the same tip multiple times."""
        self.tip.add_downvote(self.user2)
        with self.assertRaises(PermissionError):
            self.tip.add_downvote(self.user2)
        self.assertEqual(self.user1.reputation, -2)

    def test_multiple_upvotes_from_different_users(self):
        """Verify that a tip receives the correct reputation with multiple upvotes."""
        self.tip.add_upvote(self.user2)
        self.tip.add_upvote(self.user3)
        self.assertEqual(self.user1.reputation, 10)

    def test_multiple_downvotes_from_different_users(self):
        """Verify that a tip receives the correct reputation with multiple downvotes."""
        self.tip.add_downvote(self.user2)
        self.tip.add_downvote(self.user3)
        self.assertEqual(self.user1.reputation, -4)

    def test_tip_reputation_calculation(self):
        """Verify that reputation is calculated correctly after mixed votes."""
        self.tip.add_upvote(self.user2)  # +5
        self.tip.add_downvote(self.user3)  # -2
        self.assertEqual(self.user1.reputation, 3)

    def test_reputation_cannot_be_negative(self):
        """Verify that reputation cannot go below a certain threshold."""
        for _ in range(10):  # Many downvotes
            self.tip.add_downvote(self.user2)
        self.assertGreaterEqual(self.user1.reputation, -20)  # Assuming a lower limit of -20

    def test_tip_cannot_be_deleted_by_non_author(self):
        """Verify that only the author or an admin can delete a tip."""
        with self.assertRaises(PermissionError):
            self.tip.delete(user=self.user2)  # Assuming delete takes a `user` parameter
        self.tip.delete(user=self.user1)  # Author deletes their own tip
        self.assertFalse(Tip.objects.filter(id=self.tip.id).exists())

    def test_admin_can_delete_any_tip(self):
        """Verify that an admin user can delete any tip."""
        admin_user = CustomUser.objects.create_user(username="Admin", reputation=50, is_admin=True)
        self.tip.delete(user=admin_user)
        self.assertFalse(Tip.objects.filter(id=self.tip.id).exists())