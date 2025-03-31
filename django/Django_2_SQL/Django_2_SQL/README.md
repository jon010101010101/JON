Construir la Imagen Docker
Para construir la imagen Docker del proyecto, sigue estos pasos:

Abre una terminal y navega a la raíz del proyecto donde se encuentra el archivo docker-compose.yml.

Ejecuta el siguiente comando para construir la imagen Docker:

docker-compose build
Este comando lee el archivo Dockerfile y crea una imagen Docker que contiene todas las dependencias necesarias para ejecutar tu aplicación Django.
Durante este proceso, Docker descargará las imágenes base necesarias y ejecutará los comandos especificados en el Dockerfile.


2. Iniciar los Contenedores
Una vez que la imagen Docker se ha construido correctamente, puedes iniciar los contenedores:

En la misma terminal, ejecuta el siguiente comando:

docker-compose up
Este comando inicia todos los servicios definidos en el archivo docker-compose.yml.
Verás la salida de los registros de los contenedores en la terminal. Esto incluye los registros del servidor Django y cualquier otro servicio que hayas configurado (como la base de datos).
Para detener los contenedores, puedes presionar Ctrl + C en la terminal.
Nota: Si deseas ejecutar los contenedores en segundo plano (modo "detached"), puedes usar el siguiente comando:

docker-compose up -d
Esto iniciará los contenedores en segundo plano y podrás seguir usando la terminal.


3. Ejecutar Migraciones
Una vez que los contenedores estén en funcionamiento, necesitarás aplicar las migraciones para crear las tablas en la base de datos:

Abre una nueva terminal (sin cerrar la terminal donde están los contenedores en ejecución).

Ejecuta el siguiente comando para acceder al contenedor de Django y aplicar las migraciones:

docker-compose exec web python manage.py migrate
Aquí, web es el nombre del servicio definido en tu archivo docker-compose.yml que ejecuta la aplicación Django.
Este comando ejecuta las migraciones de la base de datos, creando las tablas necesarias según los modelos definidos en tus aplicaciones.
Nota: Si es la primera vez que ejecutas las migraciones, puede que veas mensajes indicando que se han creado nuevas tablas.

4. Cargar Datos Iniciales
Si tienes datos iniciales en los archivos JSON que deseas cargar en la base de datos, puedes hacerlo con los siguientes pasos:

Aún en la nueva terminal, ejecuta el siguiente comando para cargar los datos desde el archivo ex09_initial_data.json:

docker-compose exec web python manage.py loaddata d42/data/ex09_initial_data.json
Este comando carga los datos definidos en el archivo JSON en las tablas correspondientes de la base de datos.
Luego, carga los datos desde el archivo ex10_initial_data.json ejecutando:

docker-compose exec web python manage.py loaddata d42/data/ex10_initial_data.json
Esto asegurará que todos los datos iniciales necesarios para tu aplicación estén disponibles en la base de datos.
Verificación
Para verificar que todo esté funcionando correctamente:

Abre tu navegador web y dirígete a http://127.0.0.1:8000/ (o la dirección que hayas configurado en tu archivo docker-compose.yml).

Accede a las diferentes rutas de tu aplicación para asegurarte de que todo esté funcionando como se espera.

Detener los Contenedores
Cuando hayas terminado de trabajar con tu aplicación, puedes detener los contenedores ejecutando:

docker-compose down
Este comando detiene y elimina todos los contenedores, redes y volúmenes definidos en el archivo docker-compose.yml.








find . -name \*.pyc -delete
find . -name __pycache__ -delete