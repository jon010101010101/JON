# Usa la imagen base de Python 3.10
FROM python:3.10

# Establece el directorio de trabajo en /code
WORKDIR /code

# Copia los archivos de requisitos a /code
COPY requirements.txt /code/

# Instala dependencias necesarias para Django y PostgreSQL
RUN apt-get update && \
    apt-get install -y netcat-openbsd postgresql-client && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copia el script de espera al contenedor
COPY wait_for_db.sh /code/

# Copia el contenido del proyecto al directorio de trabajo
COPY . /code/

# Hacer el script ejecutable
RUN chmod +x wait_for_db.sh

# Comando por defecto para ejecutar el script de espera y luego el servidor de Django
CMD ./wait_for_db.sh && python manage.py runserver 0.0.0.0:8000
