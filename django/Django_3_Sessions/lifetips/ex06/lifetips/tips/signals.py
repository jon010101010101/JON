from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def update_user_permissions(sender, instance, **kwargs):
    if kwargs.get('update_fields') == {'reputation'}:
        instance.update_permissions()
