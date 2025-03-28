# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en /code
WORKDIR /code

# Copia el archivo de requisitos y luego instala las dependencias
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . /code/

# Expone el puerto de la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]