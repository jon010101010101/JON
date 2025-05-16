from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Chatroom, Message


class ChatTests(TestCase):
    """
    Tests obligatorios y opcionales para las funcionalidades de chat.
    """

    def setUp(self):
        """Prepara los datos iniciales para los tests."""
        self.user1 = User.objects.create_user(username="user1", password="pass1")
        self.user2 = User.objects.create_user(username="user2", password="pass2")
        self.chatroom = Chatroom.objects.create(name="General")

    # ========================
    # Tests Obligatorios
    # ========================

    def test_01_chatroom_access(self):
        """[1. Obligatorio] Verifica que solo los usuarios autenticados pueden acceder a las salas de chat."""
        # Acceso sin autenticación
        response = self.client.get(reverse("chatroom", args=[self.chatroom.id]))
        self.assertNotEqual(response.status_code, 200)

        # Acceso con autenticación
        self.client.login(username="user1", password="pass1")
        response = self.client.get(reverse("chatroom", args=[self.chatroom.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.chatroom.name)

    def test_02_send_message(self):
        """[2. Obligatorio] Verifica que los usuarios pueden enviar mensajes en las salas de chat."""
        self.client.login(username="user1", password="pass1")
        response = self.client.post(
            reverse("send_message", args=[self.chatroom.id]),
            {"message": "Hello, world!"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world!")
        self.assertContains(response, "user1")

    def test_03_message_visibility(self):
        """[3. Obligatorio] Verifica que los mensajes enviados son visibles para todos los usuarios conectados."""
        self.client.login(username="user1", password="pass1")
        self.client.post(
            reverse("send_message", args=[self.chatroom.id]),
            {"message": "Message for all"},
        )

        # Otro usuario se conecta y ve el mensaje
        self.client.logout()
        self.client.login(username="user2", password="pass2")
        response = self.client.get(reverse("chatroom", args=[self.chatroom.id]))
        self.assertContains(response, "Message for all")

    def test_04_join_notification(self):
        """[4. Obligatorio] Verifica que se muestra un mensaje cuando un usuario se une a la sala."""
        self.client.login(username="user1", password="pass1")
        response = self.client.get(reverse("chatroom", args=[self.chatroom.id]))
        self.assertContains(response, "user1 has joined the chat")

    def test_05_leave_notification(self):
        """[5. Obligatorio] Verifica que se muestra un mensaje cuando un usuario abandona la sala."""
        self.client.login(username="user1", password="pass1")
        self.client.get(reverse("chatroom", args=[self.chatroom.id]))
        self.client.logout()

        # Otro usuario ve el mensaje de salida
        self.client.login(username="user2", password="pass2")
        response = self.client.get(reverse("chatroom", args=[self.chatroom.id]))
        self.assertContains(response, "user1 has left the chat")

    def test_06_message_order(self):
        """[6. Obligatorio] Verifica que los mensajes se muestran en orden ascendente (de más antiguo a más reciente)."""
        self.client.login(username="user1", password="pass1")
        self.client.post(
            reverse("send_message", args=[self.chatroom.id]),
            {"message": "First message"},
        )
        self.client.post(
            reverse("send_message", args=[self.chatroom.id]),
            {"message": "Second message"},
        )
        self.client.post(
            reverse("send_message", args=[self.chatroom.id]),
            {"message": "Third message"},
        )

        response = self.client.get(reverse("chatroom", args=[self.chatroom.id]))
        self.assertContains(response, "First message")
        self.assertContains(response, "Second message")
        self.assertContains(response, "Third message")
        self.assertGreater(
            response.content.decode().index("First message"),
            response.content.decode().index("Second message"),
        )

    # ========================
    # Tests Opcionales
    # ========================

    def test_07_message_length_limit(self):
        """[7. Opcional] Verifica que no se pueden enviar mensajes que excedan el límite de longitud."""
        self.client.login(username="user1", password="pass1")
        long_message = "a" * 501  # Mensaje de 501 caracteres
        response = self.client.post(
            reverse("send_message", args=[self.chatroom.id]),
            {"message": long_message},
        )
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, "Message too long")

    def test_08_empty_message(self):
        """[8. Opcional] Verifica que no se pueden enviar mensajes vacíos."""
        self.client.login(username="user1", password="pass1")
        response = self.client.post(
            reverse("send_message", args=[self.chatroom.id]),
            {"message": ""},
        )
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, "Message cannot be empty")

    def test_09_reconnect_behavior(self):
        """[9. Opcional] Verifica que un usuario que se desconecta y vuelve a conectarse aparece como nuevo participante."""
        self.client.login(username="user1", password="pass1")
        self.client.get(reverse("chatroom", args=[self.chatroom.id]))
        self.client.logout()

        # Reingreso del mismo usuario
        self.client.login(username="user1", password="pass1")
        response = self.client.get(reverse("chatroom", args=[self.chatroom.id]))
        self.assertContains(response, "user1 has joined the chat")

    def test_10_user_list_update(self):
        """[10. Opcional] Verifica que la lista de usuarios conectados se actualiza dinámicamente."""
        self.client.login(username="user1", password="pass1")
        self.client.get(reverse("chatroom", args=[self.chatroom.id]))

        # Otro usuario se conecta
        self.client.logout()
        self.client.login(username="user2", password="pass2")
        response = self.client.get(reverse("chatroom", args=[self.chatroom.id]))
        self.assertContains(response, "user1")
        self.assertContains(response, "user2")

    def test_11_message_editing(self):
        """[11. Opcional] Verifica que un usuario puede editar sus mensajes (si está permitido)."""
        self.client.login(username="user1", password="pass1")
        message = Message.objects.create(
            chatroom=self.chatroom, user=self.user1, content="Original message"
        )

        # Editar el mensaje
        response = self.client.post(
            reverse("edit_message", args=[message.id]),
            {"content": "Edited message"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Edited message")