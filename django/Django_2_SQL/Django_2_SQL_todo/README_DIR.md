# ex00:   SQL

127.0.0.1:8000/ex00/init  OK
Demostración de que se ha creado la tabla
psql -U djangouser -d djangotraining
djangotraining=# \d ex00_movies
                       Table "public.ex00_movies"
    Column     |          Type          | Collation | Nullable | Default 
---------------+------------------------+-----------+----------+---------
 title         | character varying(64)  |           | not null | 
 episode_nb    | integer                |           | not null | 
 opening_crawl | text                   |           |          | 
 director      | character varying(32)  |           | not null | 
 producer      | character varying(128) |           | not null | 
 release_date  | date                   |           | not null | 
Indexes:
    "ex00_movies_pkey" PRIMARY KEY, btree (episode_nb)
    "ex00_movies_title_key" UNIQUE CONSTRAINT, btree (title)

# ex01: ORM     No view explicitly required for testing the model creation. 

Se prueba con Shell por que esta hecho con ORM
python manage.py shell 

>>> from ex01.models import Movies
>>> print(Movies._meta.db_table)  # This will print the table name
ex01_movies
>>> print(Movies._meta.get_fields())  # This will print a list of the model's fields
(<django.db.models.fields.CharField: title>, <django.db.models.fields.IntegerField: episode_nb>, <django.db.models.fields.TextField: opening_crawl>, <django.db.models.fields.CharField: director>, <django.db.models.fields.CharField: producer>, <django.db.models.fields.DateField: release_date>)


# ex02:   SQL

127.0.0.1:8000/ex02/init        OK

127.0.0.1:8000/ex02/populate    OK

127.0.0.1:8000/ex02/display     tabla con peliculas y directores

Demostración de que se ha creado la tabla
psql -U djangouser -d djangotraining
djangotraining=# \d ex02_movies
                       Table "public.ex02_movies"
    Column     |          Type          | Collation | Nullable | Default 
---------------+------------------------+-----------+----------+---------
 episode_nb    | integer                |           | not null | 
 title         | character varying(64)  |           | not null | 
 opening_crawl | text                   |           |          | 
 director      | character varying(32)  |           | not null | 
 producer      | character varying(128) |           | not null | 
 release_date  | date                   |           | not null | 
Indexes:
    "ex02_movies_pkey" PRIMARY KEY, btree (episode_nb)
    "ex02_movies_title_key" UNIQUE CONSTRAINT, btree (title)



# ex03:  ORM

127.0.0.1:8000/ex03/populate    OK

127.0.0.1:8000/ex03/display     tabla con peliculas y directores

(Django) ➜  Django_2_SQL_todo git:(main) ✗ python manage.py shell 
Python 3.10.16 | packaged by conda-forge | (main, Dec  5 2024, 14:16:10) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from ex03.models import Movies
>>> print(Movies._meta.db_table)
ex03_movies
>>> print(Movies._meta.get_fields())
(<django.db.models.fields.CharField: title>, <django.db.models.fields.IntegerField: episode_nb>, <django.db.models.fields.TextField: opening_crawl>, <django.db.models.fields.CharField: director>, <django.db.models.fields.CharField: producer>, <django.db.models.fields.DateField: release_date>)
>>> for movie in Movies.objects.all():
...     print(movie.episode_nb, movie.title, movie.director, movie.producer, movie.release_date)
... 
1 The Phantom Menace George Lucas Rick McCallum 1999-05-19
2 Attack of the Clones George Lucas Rick McCallum 2002-05-16
3 Revenge of the Sith George Lucas Rick McCallum 2005-05-19
4 A New Hope George Lucas Gary Kurtz, Rick McCallum 1977-05-25
5 The Empire Strikes Back Irvin Kershner Gary Kurtz, Rick McCallum 1980-05-17
6 Return of the Jedi Richard Marquand Howard G. Kazanjian, George Lucas, Rick McCallum 1983-05-25
7 The Force Awakens J. J. Abrams Kathleen Kennedy, J. J. Abrams, Bryan Burk 2015-12-11
>>> 


# ex04:  SQL

127.0.0.1:8000/ex04/init        OK

127.0.0.1:8000/ex04/populate    OK

127.0.0.1:8000/ex04/display     tabla Movies con peliculas y directores

127.0.0.1:8000/ex04/remove      sale desplegale y boton. Borrar una. 

para comprobar borrado 
psql -U djangouser -d djangotraining
SELECT * FROM ex04_movies; salen las peliculas. 
Luego ejecutar populate para que las vuelva a poner todas. Se puede volver a comprobar que ha cargado todas otra vez


djangotraining=# \d ex04_movies
                       Table "public.ex04_movies"
    Column     |          Type          | Collation | Nullable | Default 
---------------+------------------------+-----------+----------+---------
 title         | character varying(64)  |           | not null | 
 episode_nb    | integer                |           | not null | 
 opening_crawl | text                   |           |          | 
 director      | character varying(32)  |           | not null | 
 producer      | character varying(128) |           | not null | 
 release_date  | date                   |           | not null | 
Indexes:
    "ex04_movies_pkey" PRIMARY KEY, btree (episode_nb)
    "ex04_movies_title_key" UNIQUE CONSTRAINT, btree (title)

ddjangotraining=# SELECT title FROM ex04_movies;
          title          
-------------------------
 The Phantom Menace
 Attack of the Clones
 Revenge of the Sith
 A New Hope
 The Empire Strikes Back
 Return of the Jedi
 The Force Awakens
(7 rows)

cuando se ha eliminado una 

djangotraining=# SELECT title FROM ex04_movies;
          title          
-------------------------
 The Phantom Menace
 Attack of the Clones
 Revenge of the Sith
 The Empire Strikes Back
 Return of the Jedi
 The Force Awakens
(6 rows)

djangotraining=# 

Para volver a cargar ejecutar populate display y remove y se vuelven a cargar

# ex05:  ORM

127.0.0.1:8000/ex05/populate    OK

127.0.0.1:8000/ex05/display     tabla Movies con peliculas y directores

127.0.0.1:8000/ex05/remove      sale desplegale y boton.

* Para probar que ha borrado
python manage.py shell
from ex05.models import Movies
* Cuenta las peliculas que estan
Movies.objects.count()
* Ver si una pelicula en concreto esta eliminada
Movies.objects.filter(title="The Phantom Menace").exists() da True o False
* Ver la peliculas que quedan
remaining_movies = Movies.objects.all()
for movie in remaining_movies:
    print(movie.title)

>>> from ex05.models import Movies
>>> Movies.objects.count()
7
>>> remaining_movies = Movies.objects.all()
>>> for movie in remaining_movies:
...     print(movie.title)
... 
The Phantom Menace
Attack of the Clones
Revenge of the Sith
A New Hope
The Empire Strikes Back
Return of the Jedi
The Force Awakens
>>> Movies.objects.count()
6
>>> remaining_movies = Movies.objects.all()
>>> for movie in remaining_movies:
...     print(movie.title)
... 
The Phantom Menace
Attack of the Clones
Revenge of the Sith
The Empire Strikes Back
Return of the Jedi
The Force Awakens
>>> 


# ex06:   SQL

127.0.0.1:8000/ex06/init        OK

127.0.0.1:8000/ex06/populate    OK

127.0.0.1:8000/ex06/display     tabla movies

127.0.0.1:8000/ex06/update      se hace con SQL. desplegable seleccion peliculas para elegir y poder cambierle el resumen de la pelicula.
y se le puede poner nuevo 

para comprobar borrado 
psql -U djangouser -d d42
SELECT * FROM ex06_movies; salen las peliculas. 
Luego ejecutar populate para que las vuelva a poner todas. Se puede volver a comprobar que ha cargado todas otra vez

para volver a cargar original 


# ex07:  ORM  ACTUALIZACION DE DATOS

127.0.0.1:8000/ex07/populate    OK, y carga opening_crawl 

127.0.0.1:8000/ex07/display     tabla movies

127.0.0.1:8000/ex07/update      desplegable seleccion peliculas para elegir y poder cambierle el resumen de la pelicula. 

* Para probar que ha borrado
python manage.py shell
from ex07.models import Movie
* Ver la peliculas que quedan
movies = Movie.objects.all()
for movie in movies:
    print(movie.title, movie.opening_crawl)
* Ver si una pelicula en concreto esta cambiado el opening_crawl

>>> movie = Movie.objects.get(title="The Phantom Menace")
>>> print(movie.opening_crawl)
Turmoil has engulfed the
Galactic Republic. The taxation
of trade routes to outlying star
systems is in dispute.

Hoping to resolve the matter
with a blockade of deadly
battleships, the greedy Trade
Federation has stopped all
shipping to the small planet
of Naboo.

While the Congress of the
Republic endlessly debates
this alarming chain of events,
the Supreme Chancellor has
secretly dispatched two Jedi
Knights, the guardians of
peace and justice in the
galaxy, to settle the conflict....
>>> 

>>> from ex07.models import Movie
>>> >>> movie = Movie.objects.get(title="The Phantom Menace")
>>> print(movie.opening_crawl)
cambio
>>> 


# ex08: SQL

127.0.0.1:8000/ex08/init   OK: ex08_planets and ex08_people tables successfully created!

comprobacion de que las tablas se han creado con la estructura correcta

d42=# SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
AND table_name IN ('ex08_planets', 'ex08_people');
  table_name  
--------------
 ex08_people
 ex08_planets
(2 rows)

d42=# SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'ex08_planets';
   column_name   |     data_type     | is_nullable 
-----------------+-------------------+-------------
 id              | bigint            | NO
 name            | character varying | NO
 climate         | character varying | YES
 diameter        | integer           | YES
 orbital_period  | integer           | YES
 population      | bigint            | YES
 rotation_period | integer           | YES
 surface_water   | double precision  | YES
 terrain         | character varying | YES
(9 rows)

d42=# SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'ex08_people';
 column_name |     data_type     | is_nullable 
-------------+-------------------+-------------
 id          | bigint            | NO
 name        | character varying | NO
 birth_year  | character varying | YES
 gender      | character varying | YES
 eye_color   | character varying | YES
 hair_color  | character varying | YES
 height      | integer           | YES
 mass        | double precision  | YES
 homeworld   | character varying | YES
(9 rows)


127.0.0.1:8000/ex08/populate        OK pero ha tenido que cargar las tablas

Comprobacion
psql -U djangouser -d djangotraining

SELECT * FROM ex08_planets LIMIT 10;
id |   name    |       climate       | diameter | orbital_period |  population   | rotation_period | surface_water |                 terrain                  
----+-----------+---------------------+----------+----------------+---------------+-----------------+---------------+------------------------------------------
  1 | Alderaan  | temperate           |    12500 |            364 |    2000000000 |              24 |            40 | grasslands, mountains
  2 | Yavin IV  | temperate, tropical |    10200 |           4818 |          1000 |              24 |             8 | jungle, rainforests
  6 | Hoth      | frozen              |     7200 |            549 |               |              23 |           100 | tundra, ice caves, mountain ranges
  7 | Dagobah   | murky               |     8900 |            341 |               |              23 |             8 | swamp, jungles
  8 | Bespin    | temperate           |   118000 |           5110 |       6000000 |              12 |             0 | gas giant
  9 | Endor     | temperate           |     4900 |            402 |      30000000 |              18 |             8 | forests, mountains, lakes
 10 | Naboo     | temperate           |    12120 |            312 |    4500000000 |              26 |            12 | grassy hills, swamps, forests, mountains
 11 | Coruscant | temperate           |    12240 |            368 | 1000000000000 |              24 |               | cityscape, mountains
 12 | Kamino    | temperate           |    19720 |            463 |    1000000000 |              27 |           100 | ocean
 13 | Geonosis  | temperate, arid     |    11370 |            256 |  100000000000 |              30 |             5 | rock, desert, mountain, barren

djangotraining=# SELECT * FROM ex08_people LIMIT 10;
 id |        name        | birth_year | gender | eye_color |  hair_color   | height | mass | homeworld_id 
----+--------------------+------------+--------+-----------+---------------+--------+------+--------------
  1 | Luke Skywalker     | 19BBY      | male   | blue      | blond         |    172 |   77 |           62
  2 | C-3PO              | 112BBY     | n/a    | yellow    | n/a           |    167 |   75 |           62
  3 | R2-D2              | 33BBY      | n/a    | red       | n/a           |     96 |   32 |           10
  4 | Darth Vader        | 41.9BBY    | male   | yellow    | none          |    202 |  136 |           62
  5 | Leia Organa        | 19BBY      | female | brown     | brown         |    150 |   49 |            1
  6 | Owen Lars          | 52BBY      | male   | blue      | brown, grey   |    178 |  120 |           62
  7 | Beru Whitesun lars | 47BBY      | female | blue      | brown         |    165 |   75 |           62
  8 | R5-D4              |            | n/a    | red       | n/a           |     97 |   32 |           62
  9 | Biggs Darklighter  | 24BBY      | male   | brown     | black         |    183 |   84 |           62
 10 | Obi-Wan Kenobi     | 57BBY      | male   | blue-gray | auburn, white |    182 |   77 |           22
(10 rows)


127.0.0.1:8000/ex08/display     tabla con personajes y planetas


Characters and their Planets
Character	Planet	Climate
Saesee Tiin	Iktotch	arid, rocky, windy
Tion Medon	Utapau	temperate, arid, windy


# ex09: ORM Foreign Key

127.0.0.1:8000/ex09/display         tabla con personas cuyo planeta es ventoso o moderamente ventoso

* Carga de registros a la base de datos
python manage.py loaddata ex09/fixtures/ex09_initial_data.json 

python manage.py shell
Para verificar los registros en la tabla Planets
from ex09.models import Planets
Planets.objects.all()
<QuerySet [<Planets: Alderaan>, <Planets: Yavin IV>, <Planets: Bespin>, <Planets: Endor>, <Planets: Kamino>, <Planets: Utapau>, <Planets: Mustafar>, <Planets: Rodia>, <Planets: Kashyyyk>, <Planets: Polis Massa>, <Planets: Bestine IV>, <Planets: Chandrila>, <Planets: Ryloth>, <Planets: Glee Anselm>, <Planets: Tatooine>, <Planets: Hoth>, <Planets: Dagobah>, <Planets: Mygeeto>, <Planets: Felucia>, <Planets: Cato Neimoidia>, '...(remaining elements truncated)...']>

Para verificar los registros en la tabla People:
from ex09.models import People
People.objects.all()
<QuerySet [<People: Obi-Wan Kenobi>, <People: Anakin Skywalker>, <People: Chewbacca>, <People: Han Solo>, <People: Greedo>, <People: Jabba Desilijic Tiure>, <People: Wedge Antilles>, <People: Yoda>, <People: Palpatine>, <People: Boba Fett>, <People: IG-88>, <People: Bossk>, <People: Lando Calrissian>, <People: Lobot>, <People: Ackbar>, <People: Wicket Systri Warrick>, <People: Qui-Gon Jinn>, <People: Jar Jar Binks>, <People: Darth Maul>, <People: Ayla Secura>, '...(remaining elements truncated)...']>
>>> 

verificar la creacion de las tablas

>>> from ex09.models import People
>>> print(Planets._meta.fields)
(<django.db.models.fields.BigAutoField: id>, <django.db.models.fields.CharField: name>, <django.db.models.fields.CharField: climate>, <django.db.models.fields.IntegerField: diameter>, <django.db.models.fields.PositiveIntegerField: orbital_period>, <django.db.models.fields.BigIntegerField: population>, <django.db.models.fields.PositiveIntegerField: rotation_period>, <django.db.models.fields.FloatField: surface_water>, <django.db.models.fields.TextField: terrain>, <django.db.models.fields.DateTimeField: created>, <django.db.models.fields.DateTimeField: updated>)

>>> from ex09.models import Planets
>>> print(Planets._meta.fields)
(<django.db.models.fields.BigAutoField: id>, <django.db.models.fields.CharField: name>, <django.db.models.fields.CharField: climate>, <django.db.models.fields.IntegerField: diameter>, <django.db.models.fields.PositiveIntegerField: orbital_period>, <django.db.models.fields.BigIntegerField: population>, <django.db.models.fields.PositiveIntegerField: rotation_period>, <django.db.models.fields.FloatField: surface_water>, <django.db.models.fields.TextField: terrain>, <django.db.models.fields.DateTimeField: created>, <django.db.models.fields.DateTimeField: updated>)
>>> 

# ex10: ORM Many to Many

http://127.0.0.1:8000/ex10/         sale desplegable para haber busqueda y un listado con la busqueda


* Carga de registros
python manage.py loaddata ex10/fixtures/ex10_initial_data.json
_initial_data.json
Installed 154 object(s) from 1 fixture(s)

psql -U djangouser -d djangotraining
