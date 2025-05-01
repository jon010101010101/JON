from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
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


def update_user_permissions(user):
    """Actualiza los permisos del usuario basándose en su reputación."""
    content_type = ContentType.objects.get_for_model(Tip)
    can_downvote_permission = Permission.objects.get(codename='can_downvote_tip', content_type=content_type)
    can_delete_tip_permission = Permission.objects.get(codename='can_delete_tip', content_type=content_type)

    if user.reputation >= 15 and can_downvote_permission not in user.user_permissions.all():
        user.user_permissions.add(can_downvote_permission)
    elif user.reputation < 15 and can_downvote_permission in user.user_permissions.all():
        user.user_permissions.remove(can_downvote_permission)

    if user.reputation >= 30 and can_delete_tip_permission not in user.user_permissions.all():
        user.user_permissions.add(can_delete_tip_permission)
    elif user.reputation < 30 and can_delete_tip_permission in user.user_permissions.all():
        user.user_permissions.remove(can_delete_tip_permission)


@receiver(post_delete, sender=Tip)
def tip_deleted(sender, instance, **kwargs):
    """Recalcula la reputación del autor del tip borrado y actualiza sus permisos."""
    author = instance.author
    # Recalcular la reputación sumando los votos de los tips restantes del autor
    reputation = Tip.objects.filter(author=author).aggregate(
        total_upvotes=Sum('upvotes'),
        total_downvotes=Sum('downvotes')
    )
    upvotes = reputation['total_upvotes'] or 0
    downvotes = reputation['total_downvotes'] or 0
    author.reputation = (upvotes * 5) - (downvotes * 2)
    author.save()
    update_user_permissions(author)  # Actualizar permisos


@receiver(post_save, sender=Tip)
def tip_saved(sender, instance, **kwargs):
    """Actualiza la reputación del autor y sus permisos cuando se guarda un tip (upvote/downvote)."""
    author = instance.author
    # Recalcular la reputación sumando los votos de los tips del autor
    reputation = Tip.objects.filter(author=author).aggregate(
        total_upvotes=Sum('upvotes'),
        total_downvotes=Sum('downvotes')
    )
    upvotes = reputation['total_upvotes'] or 0
    downvotes = reputation['total_downvotes'] or 0
    author.reputation = (upvotes * 5) - (downvotes * 2)
    author.save()
    update_user_permissions(author)  # Actualizar permisos