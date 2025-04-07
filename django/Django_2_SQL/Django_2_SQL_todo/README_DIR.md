# ex00: 127.0.0.1:8000/ex00/init  OK

# ex01: No view explicitly required for testing the model creation. 

psql -U djangouser -d d42

d42=# \d ex01_movies
                       Table "public.ex01_movies"
    Column     |          Type          | Collation | Nullable | Default 
---------------+------------------------+-----------+----------+---------
 title         | character varying(64)  |           | not null | 
 episode_nb    | integer                |           | not null | 
 opening_crawl | text                   |           |          | 
 director      | character varying(32)  |           | not null | 
 producer      | character varying(128) |           | not null | 
 release_date  | date                   |           | not null | 
Indexes:
    "ex01_movies_pkey" PRIMARY KEY, btree (episode_nb)
    "ex01_movies_title_e9be860e_like" btree (title varchar_pattern_ops)
    "ex01_movies_title_key" UNIQUE CONSTRAINT, btree (title)

# ex02:

127.0.0.1:8000/ex02/init        OK

127.0.0.1:8000/ex02/populate    OK

127.0.0.1:8000/ex02/display     tabla con peliculas y directores

# ex03:

127.0.0.1:8000/ex03/populate

The Phantom Menace inserted successfully.
Attack of the Clones inserted successfully.
Revenge of the Sith inserted successfully.
A New Hope inserted successfully.
The Empire Strikes Back inserted successfully.
Return of the Jedi inserted successfully.
The Force Awakens inserted successfully.

127.0.0.1:8000/ex03/display     tabla con peliculas y directores

# ex04:

127.0.0.1:8000/ex04/init        OK

127.0.0.1:8000/ex04/populate    OK

127.0.0.1:8000/ex04/display     tabla con peliculas y directores

127.0.0.1:8000/ex04/remove      sale desplegale y boton. Borrar una. 

para comprobar borrado 
psql -U djangouser -d d42
SELECT * FROM ex04_movies; salen las peliculas. 
Luego ejecutar populate para que las vuelva a poner todas. Se puede volver a comprobar que ha cargado todas otra vez

# ex05:

127.0.0.1:8000/ex05/populate    OK

127.0.0.1:8000/ex05/display     tabla con peliculas y directores

127.0.0.1:8000/ex05/remove      igual que ex04

# ex06:

127.0.0.1:8000/ex06/load_opening_crawl      Opening crawl data loaded successfully.

127.0.0.1:8000/ex06/init        OK

127.0.0.1:8000/ex06/populate    OK

127.0.0.1:8000/ex06/display     tabla movies

127.0.0.1:8000/ex06/update      se hace con SQL. desplegable seleccion peliculas para elegir y poder cambierle el resumen de la pelicula.
y se le puede poner nuevo 

para comprobar borrado 
psql -U djangouser -d d42
SELECT * FROM ex06_movies; salen las peliculas. 
Luego ejecutar populate para que las vuelva a poner todas. Se puede volver a comprobar que ha cargado todas otra vez

para volver a cargar original 127.0.0.1:8000/ex06/load_opening_crawl, si el cambio es definitivo no ejecutar mas 127.0.0.1:8000/ex06/load_opening_crawl


# ex07:

127.0.0.1:8000/ex07/load_opening_crawl      Opening crawl data loaded successfully.

127.0.0.1:8000/ex07/populate    OK

127.0.0.1:8000/ex07/display     tabla movies

127.0.0.1:8000/ex07/update      lo mismo que en ex06 pero con ORM 

para comprobar borrado 
psql -U djangouser -d d42
SELECT * FROM ex07_movie; salen las peliculas. 
Luego ejecutar populate para que las vuelva a poner todas. Se puede volver a comprobar que ha cargado todas otra vez

para volver a cargar original 127.0.0.1:8000/ex07/load_opening_crawl, si el cambio es definitivo no ejecutar mas 127.0.0.1:8000/ex07/load_opening_crawl


# ex08: 127.0.0.1:8000/ex08/init

# ex09: 127.0.0.1:8000/ex09/display

# ex10: 127.0.0.1:8000/ex10/search