from email.message import EmailMessage
import smtplib

msg = EmailMessage()
msg.set_content("Este es un correo de prueba enviado desde Python.")
msg["Subject"] = "Prueba SMTP con EmailMessage"
msg["From"] = "lifetipsdjango@gmail.com"
msg["To"] = "destinatario@gmail.com"

try:
    server = smtplib.SMTP("smtp.sendgrid.net", 2525)  # Cambia el puerto si es necesario
    server.starttls()
    server.login("apikey", "TU_CLAVE_API")  # Reemplaza TU_CLAVE_API con la clave API
    server.send_message(msg)
    print("Correo enviado con éxito.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
finally:
    try:
        server.quit()
    except Exception:
        pass

# python send_email.py