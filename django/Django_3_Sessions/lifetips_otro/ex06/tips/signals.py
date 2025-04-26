from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser, Tip

@receiver(post_save, sender=CustomUser)
def assign_permissions_on_user_creation(sender, instance, created, **kwargs):
    """Asigna permisos automáticamente al crear un nuevo usuario."""
    if created:  # Solo asigna permisos al crear un usuario
        # Cambiar el content_type al modelo Tip
        content_type = ContentType.objects.get_for_model(Tip)

        # Crear o buscar el permiso para "can_downvote_tip"
        can_downvote_permission, _ = Permission.objects.get_or_create(
            codename='can_downvote_tip',
            defaults={
                'name': 'Can downvote tip',
                'content_type': content_type,  # Asociar al modelo Tip
            }
        )

        # Crear o buscar el permiso para "can_delete_tip"
        can_delete_tip_permission, _ = Permission.objects.get_or_create(
            codename='can_delete_tip',
            defaults={
                'name': 'Can delete tip',
                'content_type': content_type,  # Asociar al modelo Tip
            }
        )

        # Asignar permisos iniciales según la reputación
        if instance.reputation >= 15:
            instance.user_permissions.add(can_downvote_permission)
        if instance.reputation >= 30:
            instance.user_permissions.add(can_delete_tip_permission)
