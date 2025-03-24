# Importa el módulo models de Django para definir modelos de base de datos
from django.db import models

# Define un modelo llamado LogEntry
class LogEntry(models.Model):
    # Campo de texto con longitud máxima de 255 caracteres
    text = models.CharField(max_length=255)
    
    # Campo de fecha y hora que se establece automáticamente al crear el registro
    timestamp = models.DateTimeField(auto_now_add=True)

    # Método que define cómo se representa el objeto como cadena de texto
    def __str__(self):
        # Devuelve una cadena con el formato "timestamp: texto"
        return f"{self.timestamp}: {self.text}"
