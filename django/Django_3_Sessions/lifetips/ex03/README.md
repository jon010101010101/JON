# EJERCICIO EX00

desde ex00

python manage.py migrate

luego 

python manage.py runserver


http://localhost:8000/


# EJERCICIO EX01

desde ex01

http://localhost:8000/ → página principal (home)

http://localhost:8000/register/ → registro

http://localhost:8000/login/ → login

http://localhost:8000/logout/ → logout


# EJERCICIO EX02




http://localhost:8000/ → Página principal (home): muestra los tips y, si el usuario está logueado, el formulario para crear un tip.

http://localhost:8000/register/ → Página de registro de usuario.

http://localhost:8000/login/ → Página de login.

http://localhost:8000/logout/ → Logout (cierra la sesión y redirige a la home).

* para visualizar lo que hemos metido tips
sqlite3 db.sqlite3
* ver las tablas
.tables
* ver el contenido
SELECT * FROM tips_tip;
* ver el contenido mas claro
.headers ON
.mode column
SELECT * FROM tips_tip;
* Salir
.quit

o ejecutar python see_tips.py

# EJERCICIO EX03

Si esta registrado puede votar a favor o contra pero solo una vez. Tmbien puede borrar y desaparecce de la base de datos y de mostrarse en pantalla

Si no esta registrado puede verlos pero no votar ni borrar

http://localhost:8000/ → Página principal (home): muestra los tips y, si el usuario está logueado, el formulario para crear un tip.

http://localhost:8000/register/ → Página de registro de usuario.

http://localhost:8000/login/ → Página de login.

http://localhost:8000/logout/ → Logout (cierra la sesión y redirige a la home).



find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +

 
pkill -f "python manage.py runserver"
lsof -i :8000
kill -9 38140



cp -r ex02 ex03
