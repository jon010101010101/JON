import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ex06.settings')
django.setup()

from django.contrib.auth import get_user_model
from tips.models import Tip

User = get_user_model()

for user in User.objects.all():
    print(f"\nUser: {user.username}")
    user_total = 0
    tips = Tip.objects.filter(author=user)
    if not tips:
        print("  No tips.")
    for tip in tips:
        print(f"  Tip #{tip.id}: {tip.content}")
        upvoters = tip.upvotes.all()
        downvoters = tip.downvotes.all()
        tip_score = 0
        for u in upvoters:
            print(f"    Voted by: {u.username} (+5)")
            tip_score += 5
        for u in downvoters:
            print(f"    Voted by: {u.username} (-2)")
            tip_score -= 2
        print(f"    Tip score: {tip_score}")
        user_total += tip_score
    print(f"  Calculated reputation total: {user_total}")
    print(f"  Stored reputation: {user.reputation}")
    if user_total > 30:
        print("  Puede votar en contra y borrar.")
    elif user_total > 15:
        print("  Puede votar en contra.")


# python check_reputation.py
