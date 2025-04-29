from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps  # Importación necesaria para obtener modelos dinámicamente
import logging

# Configuración del logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@receiver(post_save, sender=apps.get_model('tips', 'CustomUser'))
def assign_permissions_on_user_creation(sender, instance, created, **kwargs):
    logger.debug("Señal 'assign_permissions_on_user_creation' ejecutada.")
    if created:
        try:
            logger.debug(f"Usuario creado: {instance.username}, Reputación: {instance.reputation}")

            # Obtener el ContentType del modelo Tip (corregido)
            content_type = ContentType.objects.get_for_model(apps.get_model('tips', 'Tip'))
            logger.debug(f"Content Type obtenido: {content_type}")

            # Buscar o crear permisos personalizados
            can_downvote_permission, created_downvote = Permission.objects.get_or_create(
                codename='can_downvote_tip',
                defaults={'name': 'Can downvote a tip', 'content_type': content_type},
            )
            logger.debug(f"Permiso 'can_downvote_tip': {can_downvote_permission}, Creado: {created_downvote}")

            can_delete_tip_permission, created_delete = Permission.objects.get_or_create(
                codename='can_delete_tip',
                defaults={'name': 'Can delete tip', 'content_type': content_type},
            )
            logger.debug(f"Permiso 'can_delete_tip': {can_delete_tip_permission}, Creado: {created_delete}")

            # Asignar permisos basado en la reputación
            if instance.reputation >= 15:
                instance.user_permissions.add(can_downvote_permission)
                logger.debug(f"Permiso 'can_downvote_tip' asignado a {instance.username}.")
            if instance.reputation >= 30:
                instance.user_permissions.add(can_delete_tip_permission)
                logger.debug(f"Permiso 'can_delete_tip' asignado a {instance.username}.")

        except Exception as e:
            logger.error(f"Error asignando permisos en la creación del usuario: {e}")


@receiver(post_save, sender=apps.get_model('tips', 'CustomUser'))
def update_permissions_on_reputation_change(sender, instance, **kwargs):
    logger.debug("Señal 'update_permissions_on_reputation_change' ejecutada.")
    try:
        logger.debug(f"Usuario actualizado: {instance.username}, Reputación: {instance.reputation}")

        # Obtener el ContentType del modelo Tip (corregido)
        content_type = ContentType.objects.get_for_model(apps.get_model('tips', 'Tip'))
        logger.debug(f"Content Type obtenido: {content_type}")

        # Obtener permisos existentes
        can_downvote_permission = Permission.objects.get(
            codename='can_downvote_tip',
            content_type=content_type,
        )
        logger.debug(f"Permiso obtenido: {can_downvote_permission}")

        can_delete_tip_permission = Permission.objects.get(
            codename='can_delete_tip',
            content_type=content_type,
        )
        logger.debug(f"Permiso obtenido: {can_delete_tip_permission}")

        # Reasignar permisos basado en la reputación actual
        if instance.reputation >= 15:
            instance.user_permissions.add(can_downvote_permission)
            logger.debug(f"Permiso 'can_downvote_tip' reasignado a {instance.username}.")
        else:
            instance.user_permissions.remove(can_downvote_permission)
            logger.debug(f"Permiso 'can_downvote_tip' eliminado de {instance.username}.")

        if instance.reputation >= 30:
            instance.user_permissions.add(can_delete_tip_permission)
            logger.debug(f"Permiso 'can_delete_tip' reasignado a {instance.username}.")
        else:
            instance.user_permissions.remove(can_delete_tip_permission)
            logger.debug(f"Permiso 'can_delete_tip' eliminado de {instance.username}.")

    except Permission.DoesNotExist as e:
        logger.error(f"Permiso no encontrado: {e}")
    except Exception as e:
        logger.error(f"Error actualizando permisos según la reputación: {e}")