 Lista de artículos
GET
http://localhost:8000/articles/

2. Publicaciones del usuario autenticado
GET
http://localhost:8000/publications/

3. Registro de usuario
GET / POST
http://localhost:8000/register/

4. Login
POST
(El login se hace desde el formulario en /articles/, no desde /login/)

5. Logout
GET
http://localhost:8000/logout/

6. Publicar artículo
GET / POST
http://localhost:8000/publish/

7. Favoritos
GET
http://localhost:8000/favourites/

8. Añadir a favoritos
POST
http://localhost:8000/add-favourite/<pk>/
(Cambia <pk> por el ID de un artículo real, por ejemplo 1, 2, 3...)

9. Mensajes de favoritos
GET
http://localhost:8000/favourite-added/
http://localhost:8000/already-favourite/

10. Detalle de artículo
GET
http://localhost:8000/articles/<pk>/
(Cambia <pk> por el ID de un artículo real)

Internacionalización (cambio de idioma en la URL)
Si tienes configurado el middleware de idiomas y las rutas traducidas:

Español:

http://localhost:8000/es/articles/

http://localhost:8000/es/favourites/

http://localhost:8000/es/publications/

http://localhost:8000/es/articles/<pk>/

Inglés:

http://localhost:8000/en/articles/

http://localhost:8000/en/favourites/

http://localhost:8000/en/publications/

http://localhost:8000/en/articles/<pk>/

Redirección Home
GET
http://localhost:8000/
(Debe redirigir a /articles/)



# TESTS

Para ejecutar los dos test a la vez
python manage.py test

Para ejecutar solo Acccount
python manage.py test account


Para ejecutar solo Chat
python manage.py test chat












# Para arrancar el servidor Redis
/sgoinfre/students/jurrutia/redis-stable/src/redis-server

# Para dejarlo en segundo plano
src/redis-server &


python manage.py runserver



find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +

 
pkill -f "python manage.py runserver"
lsof -i :8000
kill -9 38140


./stop.sh       
./start.sh
