import smtplib

try:
    # Conectar al servidor SMTP
    server = smtplib.SMTP("smtp.sendgrid.net", 587)
    server.ehlo()  # Identifica el cliente
    server.starttls()  # Inicia la conexión TLS
    server.ehlo()  # Reconfirma la conexión TLS
    print("Conexión TLS establecida con éxito.")

    # Iniciar sesión en SendGrid
    server.login("apikey", "TU_CLAVE_API")  # Reemplaza TU_CLAVE_API con tu clave API de SendGrid
    print("Inicio de sesión con SendGrid exitoso.")

    # Enviar correo
    server.sendmail(
        "lifetipsdjango@gmail.com",  # Correo remitente
        "jonurrutia10@gmail.com",    # Correo destinatario
        "Subject: Prueba SMTP\n\nEste es un correo de prueba enviado desde un script de Python."
    )
    print("Correo enviado con éxito.")

except smtplib.SMTPException as e:
    print(f"Error al enviar el correo: {e}")

finally:
    try:
        server.quit()
    except Exception:
        pass



# python test_sendgrid.py