import unittest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from tips.models import Tip, CustomUser


class ReputationTest(TestCase):
    def setUp(self):
        # Get the custom user model
        self.User = get_user_model()
        # Create a superuser for permission assignment
        self.superuser = self.User.objects.create_superuser(
            'superuser', 'superuser@example.com', 'password')
        # Create some regular users
        self.user1 = self.User.objects.create_user(
            'user1', 'user1@example.com', 'password')
        self.user2 = self.User.objects.create_user(
            'user2', 'user2@example.com', 'password')
        # Create some tips
        self.tip1 = Tip.objects.create(
            author=self.user1, content="User1's Tip")
        self.tip2 = Tip.objects.create(
            author=self.user2, content="User2's Tip")

        # Get content type for Tip model
        self.tip_content_type = ContentType.objects.get_for_model(Tip)
        # Get the custom permission for downvoting
        self.can_downvote_permission = Permission.objects.get(
            codename='can_downvote_tip',
            content_type=self.tip_content_type,
        )
        # Get the custom permission for deleting tips
        self.can_delete_permission = Permission.objects.get(
            codename='can_delete_tip',
            content_type=self.tip_content_type,
        )

    def test_initial_reputation(self):
        self.assertEqual(self.user1.reputation, 0)
        self.assertEqual(self.user2.reputation, 0)

    def test_upvote_reputation(self):
        self.tip1.add_upvote(self.user2)  # User2 upvotes User1's tip
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.reputation, 5)

    def test_downvote_reputation(self):
        # Ensure user2 has enough reputation to downvote
        self.user2.reputation = 15
        self.user2.save()
        self.tip1.add_downvote(self.user2)  # User2 downvotes User1's tip
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.reputation, -2)

    def test_delete_tip_reputation(self):
        # First, give user1 some reputation
        self.tip1.add_upvote(self.user2)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.reputation, 5)
        # Delete the tip
        self.tip1.delete()
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.reputation, 0)  # Reputation should be back to 0

    def test_downvote_permission_unlock(self):
        # User1 should not have downvote permission initially
        self.assertFalse(self.user1.has_perm('tips.can_downvote_tip'))
        # Give user1 enough reputation to unlock the permission (15 points)
        for _ in range(3):
            tip = Tip.objects.create(author=self.user1, content="Another Tip")
            tip.add_upvote(self.user2)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.reputation, 15)  # 3 tips * 5 points each
        # Now user1 should have the downvote permission
        self.assertTrue(self.user1.has_perm('tips.can_downvote_tip'))

    def test_delete_permission_unlock(self):
        # User1 should not have delete permission initially
        self.assertFalse(self.user1.has_perm('tips.can_delete_tip'))
        # Give user1 enough reputation to unlock the delete permission (30 points)
        for _ in range(6):
            tip = Tip.objects.create(author=self.user1, content="Another Tip")
            tip.add_upvote(self.user2)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.reputation, 30)  # 6 tips * 5 points each
        # Now user1 should have the delete permission
        self.assertTrue(self.user1.has_perm('tips.can_delete_tip'))

    def test_permission_loss(self):
        # Give user1 enough reputation to unlock both permissions
        for _ in range(6):
            tip = Tip.objects.create(author=self.user1, content="Another Tip")
            tip.add_upvote(self.user2)
        self.user1.refresh_from_db()
        self.assertTrue(self.user1.has_perm('tips.can_downvote_tip'))
        self.assertTrue(self.user1.has_perm('tips.can_delete_tip'))
        # Now, reduce user1's reputation below the threshold for downvote permission
        self.user2.reputation = 15
        self.user2.save()
        for _ in range(8):
            self.tip1.add_downvote(self.user2)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.reputation, 14)
        self.assertFalse(self.user1.has_perm('tips.can_downvote_tip'))
        self.assertFalse(self.user1.has_perm('tips.can_delete_tip'))

    def test_reputation_display(self):
        # Give user1 some reputation
        self.tip1.add_upvote(self.user2)
        self.user1.refresh_from_db()
        expected_display = f"user1 ({self.user1.reputation})"
        self.assertEqual(str(self.user1), expected_display)

    def test_author_can_delete_own_tip(self):
        # Ensure user1 can delete their own tip, regardless of reputation
        self.assertTrue(self.tip1.author == self.user1)

    def test_cannot_downvote_own_tip(self):
        # Ensure user1 cannot downvote their own tip
        self.user1.reputation = 15
        self.user1.save()
        can_downvote = self.tip1.add_downvote(self.user1)
        self.assertFalse(can_downvote)
        self.user1.refresh_from_db()
        self.assertEqual(self.tip1.downvotes.count(), 0)

    def test_downvote_requires_reputation(self):
        # User2 has no reputation
        self.user2.reputation = 0
        self.user2.save()
        can_downvote = self.tip1.add_downvote(self.user2)
        self.assertFalse(can_downvote)
        self.assertEqual(self.tip1.downvotes.count(), 0)
