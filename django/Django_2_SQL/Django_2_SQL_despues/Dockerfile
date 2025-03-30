# Usa una imagen base oficial de Python
FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copia el archivo requirements.txt y instala las dependencias
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código fuente al contenedor
COPY . /code/

# Comando predeterminado para ejecutar cuando se inicie el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
