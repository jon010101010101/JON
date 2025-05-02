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



# EJERCICIO EX04


 → Página principal (home): muestra todos los tips y, si el usuario está logueado, también el formulario para crear un tip.

http://localhost:8000/register/ → Página de registro de usuario.

http://localhost:8000/login/ → Página de inicio de sesión (login).

http://localhost:8000/logout/ → Logout: cierra la sesión del usuario y redirige a la página principal.



# EJERCICIO EX05

http://localhost:8000/admin    

lo que se puede hacer desdde el panel de administracion

1. Gestionar usuarios y permisos
Usuarios: Crear nuevos usuarios, cambiar contraseñas, activar/desactivar cuentas, asignar permisos individuales o por grupos.

Grupos: Crear grupos de usuarios (ej: "Editores", "Moderadores") y asignarles permisos específicos. Luego, añades usuarios a esos grupos para que hereden los permisos.

Asignar el permiso can_delete_tip: Entras al usuario, buscas la sección de "Permisos de usuario" y marcas la casilla correspondiente.

2. Gestionar los modelos de tu aplicación
Ver, crear, editar y borrar instancias de tus modelos. Por ejemplo, puedes ver la lista de todos los Tip, crear nuevos, modificar el contenido de los existentes, o borrarlos.

3. Otras tareas de administración
Dependiendo de las aplicaciones que tengas instaladas, puedes gestionar otras cosas como:

Sesiones: Ver y borrar sesiones de usuario.

Archivos estáticos: Gestionar la colección de archivos estáticos del sitio.

Caché: Limpiar la caché del sitio.



# EJERCICIO EX06

Página de Inicio: http://127.0.0.1:8000/
Inicio de Sesión: http://127.0.0.1:8000/login/
Registro de Usuarios: http://127.0.0.1:8000/register/
Crear un Tip: http://127.0.0.1:8000/tips/create/
Ver Tips Creados: http://127.0.0.1:8000/tips/list/
Página de Administracion: http://127.0.0.1:8000/admin
Listado de ususarios con reputacion http://127.0.0.1:8000/users/list/
Pagina no existe http://localhost:8000/nonexistent-page


Vuelta de correo
http://127.0.0.1:8000/reset/%3Cuid%3E/%3Ctoken%3E/

Passsword reset 
http://127.0.0.1:8000/password_reset/



export PYTHONPATH=/sgoinfre/students/jurrutia/42_otrogitjon/django/Django_3_Sessions/lifetips:$PYTHONPATH


# Para sacar listado de tips metidos
python manage.py list_tips

# Para hacer test
python manage.py test













find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +

 
pkill -f "python manage.py runserver"
lsof -i :8000
kill -9 38140



cp -r ex05 ex06
