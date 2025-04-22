from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import Tip
from django.contrib.auth import get_user_model

@receiver(m2m_changed, sender=Tip.upvotes.through)
@receiver(m2m_changed, sender=Tip.downvotes.through)
def update_user_reputation(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        user = instance.author
        upvotes = instance.upvotes.count()
        downvotes = instance.downvotes.count()
        reputation = (upvotes * 5) - (downvotes * 2)
        user.reputation = reputation
        user.save()

@receiver(post_delete, sender=Tip)
def tip_deleted(sender, instance, **kwargs):
    user = instance.author
    upvotes = instance.upvotes.count()
    downvotes = instance.downvotes.count()
    reputation = (upvotes * 5) - (downvotes * 2)
    user.reputation = reputation
    user.save()
