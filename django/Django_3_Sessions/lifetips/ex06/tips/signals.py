from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from .models import CustomUser, Tip

# Asigna permisos automáticamente al crear un nuevo usuario según su reputación inicial
@receiver(post_save, sender=CustomUser)
def assign_permissions_on_user_creation(sender, instance, created, **kwargs):
    """
    Asigna permisos automáticamente al crear un nuevo usuario.
    """
    if created:
        content_type = ContentType.objects.get_for_model(Tip)

        # Busca o crea el permiso para downvote
        can_downvote_permission, _ = Permission.objects.get_or_create(
            codename='can_downvote_tip',
            defaults={
                'name': 'Can downvote tip',
                'content_type': content_type,
            }
        )

        # Busca o crea el permiso para borrar tips
        can_delete_tip_permission, _ = Permission.objects.get_or_create(
            codename='can_delete_tip',
            defaults={
                'name': 'Can delete tip',
                'content_type': content_type,
            }
        )

        # Asigna permisos iniciales según la reputación
        if instance.reputation >= 15:
            instance.user_permissions.add(can_downvote_permission)
        if instance.reputation >= 30:
            instance.user_permissions.add(can_delete_tip_permission)

# Actualiza los permisos del usuario según su reputación
def update_user_permissions(user):
    """
    Actualiza los permisos del usuario basándose en su reputación.
    """
    content_type = ContentType.objects.get_for_model(Tip)
    can_downvote_permission = Permission.objects.get(codename='can_downvote_tip', content_type=content_type)
    can_delete_tip_permission = Permission.objects.get(codename='can_delete_tip', content_type=content_type)

    # Permiso para downvote
    if user.reputation >= 15 and can_downvote_permission not in user.user_permissions.all():
        user.user_permissions.add(can_downvote_permission)
    elif user.reputation < 15 and can_downvote_permission in user.user_permissions.all():
        user.user_permissions.remove(can_downvote_permission)

    # Permiso para borrar tips
    if user.reputation >= 30 and can_delete_tip_permission not in user.user_permissions.all():
        user.user_permissions.add(can_delete_tip_permission)
    elif user.reputation < 30 and can_delete_tip_permission in user.user_permissions.all():
        user.user_permissions.remove(can_delete_tip_permission)

# Signal para recalcular la reputación y permisos tras borrar un tip
@receiver(post_delete, sender=Tip)
def tip_deleted(sender, instance, **kwargs):
    """
    Recalcula la reputación del autor del tip borrado y actualiza sus permisos.
    """
    author = instance.author
    # Recalcula la reputación sumando los votos de todos los tips restantes del autor
    tips = Tip.objects.filter(author=author)
    upvotes = sum(tip.upvotes.count() for tip in tips)
    downvotes = sum(tip.downvotes.count() for tip in tips)
    author.reputation = max(upvotes * 5 - downvotes * 2, -20)  # Límite inferior -20
    author.save()
    update_user_permissions(author)

# Signal para recalcular la reputación y permisos tras guardar un tip (crear, upvote, downvote)
@receiver(post_save, sender=Tip)
def tip_saved(sender, instance, **kwargs):
    """
    Actualiza la reputación del autor y sus permisos cuando se guarda un tip (por votos o edición).
    """
    author = instance.author
    tips = Tip.objects.filter(author=author)
    upvotes = sum(tip.upvotes.count() for tip in tips)
    downvotes = sum(tip.downvotes.count() for tip in tips)
    author.reputation = max(upvotes * 5 - downvotes * 2, -150)
    author.save()
    update_user_permissions(author)

# Signal para notificar por email si se restablece la contraseña de un usuario
@receiver(post_save, sender=CustomUser)
def notify_password_reset(sender, instance, update_fields=None, **kwargs):
    """
    Envía un correo cuando se restablece la contraseña del usuario.
    """
    if update_fields and 'password' in update_fields:
        send_mail(
            subject='Tu contraseña ha sido restablecida',
            message=(
                'Hola, tu contraseña ha sido restablecida recientemente. '
                'Si no fuiste tú, por favor contacta con soporte inmediatamente.'
            ),
            from_email='support@lifetips.com',
            recipient_list=[instance.email],
        )
