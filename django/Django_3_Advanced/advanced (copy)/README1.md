EX00: Modelos, artículos, tabla, login, redirect
✔️ Modelos: No se testean directamente, pero tus tests usan los modelos y crearán error si no están bien.

✔️ Cinco artículos, tres usuarios: Tus tests los crean en setUp.

✔️ Tabla de artículos: Test 1.

✔️ Redirect home: Test 14.

✔️ Login (formulario, error): Test 2, 3.

✔️ No hardcodear URLs: Tus tests usan solo reverse().

EX01: Publicaciones, detalle, logout, favoritos
✔️ Publicaciones solo del usuario: Test 4.

✔️ Detalle de artículo: Test 10.

✔️ Logout: Test 2.

✔️ Favoritos (ver, añadir, duplicados): Test 8, 9.

✔️ Links correctos: Tus tests acceden por URL con reverse().

EX02: Register, publish, add to favourite
✔️ Registro: Test 5, 6.

✔️ Publicar artículo: Test 7.

✔️ Añadir a favoritos: Test 8.

✔️ No añadir sin login: Test 16.

✔️ No publicar sin login: Test 17.

✔️ Formulario de registro (POST, confirmación): Test 5, 6.

✔️ Formulario de favoritos sin campos visibles: No es fácil testear visualmente, pero el test de añadir y duplicado lo cubre funcionalmente.

EX03: Menú en todas las páginas, login en menú, filtros
✔️ Menú en todas las páginas: Test 15.

✔️ Menú cambia según login/logout: Test 15.

✔️ Login integrado en menú, error en menú: Test 2, 3, 18.

✔️ Filtro truncate_synopsis: Test 12.

✔️ Filtro ago: Test 13.

✔️ Orden por fecha: Test 1 (implícito, pero podrías añadir un test explícito si quieres).

EX04: Bootstrap
✔️ No se testea con tests automáticos (es visual), pero si tus templates usan Bootstrap, lo cumples.

EX05: Internacionalización
✔️ Cambio de idioma, textos traducidos: Test 11.

✔️ Enlace de cambio de idioma: Puedes añadir un test que compruebe que el enlace existe.

EX06: Testing
✔️ Tests para favoritos, publicaciones y publicar: Lo tienes cubierto.



127.0.0.1:8000/



find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +

 
pkill -f "python manage.py runserver"
lsof -i :8000
kill -9 38140



# Poner contraseña
python manage.py shell

from django.contrib.auth.models import User
u = User.objects.get(username='empleado2')
u.set_password('pedro123')
u.save()

# Comprobar cambio contraseña
u = User.objects.get(username='empleado2')
u.check_password('pedro123')
