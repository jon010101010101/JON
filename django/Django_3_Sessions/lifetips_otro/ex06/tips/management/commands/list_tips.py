from django.core.management.base import BaseCommand
from tips.models import Tip

class Command(BaseCommand):
    help = "List all tips with their upvotes, downvotes, and author reputation"

    def handle(self, *args, **kwargs):
        tips = Tip.objects.all()
        if not tips:
            self.stdout.write("No tips found.")
            return

        self.stdout.write("Listing all tips with their votes and author reputation:")
        self.stdout.write("-" * 50)

        for tip in tips:
            upvotes_count = tip.upvotes.count()
            downvotes_count = tip.downvotes.count()
            upvoted_by = ", ".join([user.username for user in tip.upvotes.all()])
            downvoted_by = ", ".join([user.username for user in tip.downvotes.all()])

            self.stdout.write(f"Tip ID: {tip.id}")
            self.stdout.write(f"Author: {tip.author.username} (Reputation: {tip.author.reputation})")
            self.stdout.write(f"Content: {tip.content}")
            self.stdout.write(f"Upvotes: {upvotes_count} (By: {upvoted_by})")
            self.stdout.write(f"Downvotes: {downvotes_count} (By: {downvoted_by})")
            self.stdout.write("-" * 50)