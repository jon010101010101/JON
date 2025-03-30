# Usa la imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo en /code
WORKDIR /code

# Copia los archivos de requisitos a /code
COPY requirements.txt /code/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Instala PostgreSQL Client
RUN apt-get update && apt-get install -y postgresql-client

# Copia el contenido del proyecto al directorio de trabajo
COPY . /code/

# Comando por defecto para ejecutar el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]