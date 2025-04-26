import smtplib

# Configuración del servidor SMTP
smtp_server = "smtp.sendgrid.net"
smtp_port = 587
smtp_user = "apikey"  # Nombre de usuario siempre es "apikey"
smtp_password = "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"

# Configuración del correo
from_email = "lifetipsdjango@gmail.com"  # Cambia si es necesario
to_email = "jonurrutia10@gmail.com"  # Cambia por el correo del destinatario
subject = "Prueba SMTP desde Python"
body = "Este es un correo de prueba desde Python usando SendGrid."

# Conexión al servidor SMTP
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Inicia conexión segura
        server.login(smtp_user, smtp_password)
        
        # Mensaje con todos los encabezados necesarios
        message = f"From: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{body}"
        
        # Enviar el correo
        server.sendmail(from_email, to_email, message)
        print("Correo enviado exitosamente.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")


# python sendgrid_test.py