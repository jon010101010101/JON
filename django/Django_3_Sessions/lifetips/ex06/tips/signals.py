from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps  # Importación necesaria para get_model

@receiver(post_save, sender=apps.get_model('tips', 'CustomUser'))  # Cambia 'ex06.tips' a 'tips'
def assign_permissions_on_user_creation(sender, instance, created, **kwargs):
    """
    Asigna permisos automáticamente al crear un nuevo usuario.
    """
    if created:  # Solo asigna permisos al crear un usuario
        content_type = ContentType.objects.get_for_model(instance.__class__)

        # Crear o buscar el permiso para "can_downvote_tip"
        can_downvote_permission, _ = Permission.objects.get_or_create(
            codename='can_downvote_tip',
            defaults={
                'name': 'Can downvote tip',
                'content_type': content_type,
            }
        )

        # Crear o buscar el permiso para "can_delete_tip"
        can_delete_tip_permission, _ = Permission.objects.get_or_create(
            codename='can_delete_tip',
            defaults={
                'name': 'Can delete tip',
                'content_type': content_type,
            }
        )

        # Asignar permisos iniciales según la reputación
        if instance.reputation >= 15:
            instance.user_permissions.add(can_downvote_permission)
        if instance.reputation >= 30:
            instance.user_permissions.add(can_delete_tip_permission)


@receiver(post_save, sender=apps.get_model('tips', 'CustomUser'))  # Cambia 'ex06.tips' a 'tips'
def update_permissions_on_reputation_change(sender, instance, **kwargs):
    """
    Actualiza los permisos cuando cambia la reputación del usuario.
    """
    content_type = ContentType.objects.get_for_model(instance.__class__)

    # Obtener los permisos existentes
    can_downvote_permission = Permission.objects.get(
        codename='can_downvote_tip',
        content_type=content_type,
    )
    can_delete_tip_permission = Permission.objects.get(
        codename='can_delete_tip',
        content_type=content_type,
    )

    # Reasignar permisos según la reputación actual
    if instance.reputation >= 15:
        instance.user_permissions.add(can_downvote_permission)
    else:
        instance.user_permissions.remove(can_downvote_permission)

    if instance.reputation >= 30:
        instance.user_permissions.add(can_delete_tip_permission)
    else:
        instance.user_permissions.remove(can_delete_tip_permission)