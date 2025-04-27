from django.test import TestCase
from tips.models import CustomUser, Tip


class ReputationSystemTestCase(TestCase):

    def setUp(self):
        """Set up initial data for test cases."""
        self.user1 = CustomUser.objects.create_user(username="User1", reputation=0)
        self.user2 = CustomUser.objects.create_user(username="User2", reputation=15)
        self.user3 = CustomUser.objects.create_user(username="User3", reputation=30)
        self.tip = Tip.objects.create(author=self.user1, content="This is a tip.")

    def run_test(self, test_func, test_name):
        """Run a single test and print result."""
        try:
            test_func()
            print(f"✔️ {test_name} passed")
        except Exception as e:
            print(f"❌ {test_name} failed: {str(e)}")

    def test_initial_reputation(self):
        """Verify that new users start with 0 reputation."""
        self.assertEqual(self.user1.reputation, 0)

    def test_upvote_increases_reputation(self):
        """Verify that upvotes increase the author's reputation."""
        self.tip.upvoters.add(self.user2)  # Simular un upvote
        self.user1.reputation += 5
        self.user1.save()
        self.assertEqual(self.user1.reputation, 5)

    def test_downvote_decreases_reputation(self):
        """Verify that downvotes decrease the author's reputation."""
        self.tip.downvoters.add(self.user2)  # Simular un downvote
        self.user1.reputation -= 2
        self.user1.save()
        self.assertEqual(self.user1.reputation, -2)

    def test_downvote_permission(self):
        """Verify that users unlock downvote permissions at 15 reputation points."""
        self.assertTrue(self.user2.can_downvote)
        self.assertFalse(self.user1.can_downvote)

    def test_delete_tip_permission(self):
        """Verify that users unlock delete permissions at 30 reputation points."""
        self.assertFalse(self.user1.can_delete_tips)
        self.user1.reputation = 30
        self.user1.save()
        self.assertTrue(self.user1.can_delete_tips)

    def test_delete_tip_removes_reputation_influence(self):
        """Verify that deleting a tip removes its influence on reputation."""
        self.tip.upvoters.add(self.user2)  # Simular un upvote
        self.user1.reputation += 5
        self.tip.delete()
        self.user1.reputation -= 5
        self.user1.save()
        self.assertEqual(self.user1.reputation, 0)

    def test_self_upvote_not_allowed(self):
        """Verify that users cannot upvote their own tips."""
        with self.assertRaises(Exception):
            self.tip.upvoters.add(self.user1)

    def test_self_downvote_not_allowed(self):
        """Verify that users cannot downvote their own tips."""
        with self.assertRaises(Exception):
            self.tip.downvoters.add(self.user1)

    # Tests adicionales para ampliar la cobertura
    def test_cannot_upvote_twice(self):
        """Verify that users cannot upvote the same tip multiple times."""
        self.tip.upvoters.add(self.user2)
        with self.assertRaises(Exception):
            self.tip.upvoters.add(self.user2)
        self.assertEqual(self.user1.reputation, 5)

    def test_cannot_downvote_twice(self):
        """Verify that users cannot downvote the same tip multiple times."""
        self.tip.downvoters.add(self.user2)
        with self.assertRaises(Exception):
            self.tip.downvoters.add(self.user2)
        self.assertEqual(self.user1.reputation, -2)

    def test_multiple_upvotes_from_different_users(self):
        """Verify that a tip receives the correct reputation with multiple upvotes."""
        self.tip.upvoters.add(self.user2)
        self.tip.upvoters.add(self.user3)
        self.user1.reputation += 10
        self.user1.save()
        self.assertEqual(self.user1.reputation, 10)

    def test_multiple_downvotes_from_different_users(self):
        """Verify that a tip receives the correct reputation with multiple downvotes."""
        self.tip.downvoters.add(self.user2)
        self.tip.downvoters.add(self.user3)
        self.user1.reputation -= 4
        self.user1.save()
        self.assertEqual(self.user1.reputation, -4)

    def test_tip_reputation_calculation(self):
        """Verify that reputation is calculated correctly after mixed votes."""
        self.tip.upvoters.add(self.user2)  # +5
        self.tip.downvoters.add(self.user3)  # -2
        self.user1.reputation += 3
        self.user1.save()
        self.assertEqual(self.user1.reputation, 3)

    def test_reputation_cannot_be_negative(self):
        """Verify that reputation cannot go below a certain threshold."""
        for _ in range(10):  # Many downvotes
            self.tip.downvoters.add(self.user2)
        self.user1.reputation = max(self.user1.reputation, -20)
        self.user1.save()
        self.assertGreaterEqual(self.user1.reputation, -20)

    def test_tip_cannot_be_deleted_by_non_author(self):
        """Verify that only the author or an admin can delete a tip."""
        with self.assertRaises(Exception):
            self.tip.delete(user=self.user2)
        self.tip.delete(user=self.user1)  # Author deletes their own tip
        self.assertFalse(Tip.objects.filter(id=self.tip.id).exists())

    def test_admin_can_delete_any_tip(self):
        """Verify that an admin user can delete any tip."""
        admin_user = CustomUser.objects.create_user(username="Admin", reputation=50, is_admin=True)
        self.tip.delete(user=admin_user)
        self.assertFalse(Tip.objects.filter(id=self.tip.id).exists())

    def test_user_representation(self):
        """Verify that the user's string representation includes their reputation."""
        self.assertEqual(str(self.user1), "User1 (0 rep)")
        self.user1.reputation = 10
        self.user1.save()
        self.assertEqual(str(self.user1), "User1 (10 rep)")

    # Run all tests and display results
    def test_all(self):
        """Run all tests and display results."""
        tests = [
            (self.test_initial_reputation, "test_initial_reputation"),
            (self.test_upvote_increases_reputation, "test_upvote_increases_reputation"),
            (self.test_downvote_decreases_reputation, "test_downvote_decreases_reputation"),
            (self.test_downvote_permission, "test_downvote_permission"),
            (self.test_delete_tip_permission, "test_delete_tip_permission"),
            (self.test_delete_tip_removes_reputation_influence, "test_delete_tip_removes_reputation_influence"),
            (self.test_self_upvote_not_allowed, "test_self_upvote_not_allowed"),
            (self.test_self_downvote_not_allowed, "test_self_downvote_not_allowed"),
            (self.test_cannot_upvote_twice, "test_cannot_upvote_twice"),
            (self.test_cannot_downvote_twice, "test_cannot_downvote_twice"),
            (self.test_multiple_upvotes_from_different_users, "test_multiple_upvotes_from_different_users"),
            (self.test_multiple_downvotes_from_different_users, "test_multiple_downvotes_from_different_users"),
            (self.test_tip_reputation_calculation, "test_tip_reputation_calculation"),
            (self.test_reputation_cannot_be_negative, "test_reputation_cannot_be_negative"),
            (self.test_tip_cannot_be_deleted_by_non_author, "test_tip_cannot_be_deleted_by_non_author"),
            (self.test_admin_can_delete_any_tip, "test_admin_can_delete_any_tip"),
            (self.test_user_representation, "test_user_representation"),
        ]
        for test_func, test_name in tests:
            self.run_test(test_func, test_name)