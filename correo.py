# envia_correo.py
# ---------------------------------------------------------

from email.mime.text import MIMEText
from smtplib import SMTP

class Correo:
    def __init__(self,nombre,direccion,texto):
        self.nombre = nombre
        self.direccion = direccion
        self.texto = texto

    def manda_correo(self):
        from_address = "origen@correo.com"
        to_address = self.direccion
        message = "Hola " + self.nombre + ", \n\n" + self.texto
     
        mime_message = MIMEText(message, "plain")
        mime_message["From"] = from_address
        mime_message["To"] = to_address
        mime_message["Subject"] = "Saludos " + self.nombre

        smtp = SMTP('servidordecorreo.com', 587)
        smtp.login("usuario", "contraseña")
        smtp.sendmail(from_address, to_address, mime_message.as_string())
        smtp.quit()

