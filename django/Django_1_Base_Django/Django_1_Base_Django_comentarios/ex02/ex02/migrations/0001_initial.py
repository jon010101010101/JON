# Generado por Django 5.1.7 el 23 de marzo de 2025 a las 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    # Indica que esta es la migración inicial para esta aplicación
    initial = True

    # Lista de dependencias de esta migración (vacía en este caso)
    dependencies = [
    ]

    # Define las operaciones que se realizarán en la base de datos
    operations = [
        # Crea un nuevo modelo llamado 'LogEntry'
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                # Campo ID: autoincremental, clave primaria, no editable manualmente
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # Campo de texto con longitud máxima de 255 caracteres
                ('text', models.CharField(max_length=255)),
                # Campo de fecha y hora que se establece automáticamente al crear el registro
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
