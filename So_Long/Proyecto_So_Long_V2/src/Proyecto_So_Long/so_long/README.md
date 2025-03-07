# Proyecto so_long

## Descripción
so_long es un juego 2D donde el jugador debe recolectar todos los objetos presentes en el mapa y salir eligiendo la ruta más corta posible. El juego utiliza la librería gráfica MiniLibX y está diseñado para mejorar habilidades en programación gráfica, manejo de eventos y gestión de memoria en C.

## Estructura del Proyecto

so_long/
├── include/
│ └── so_long.h
├── libft/
│ └── (código de la librería libft)
├── maps/
│ ├── map1.ber
│ ├── map2.ber
│ ├── map3.ber
│ └── map4.ber
├── src/
│ ├── main.c
│ ├── map.c
│ ├── player.c
│ ├── render.c
│ └── utils.c
├── textures/
│ ├── collectible.xpm
│ ├── empty.xpm
│ ├── exit.xpm
│ ├── player.xpm
│ └── wall.xpm
└── Makefile

text

## Requisitos
- **C**: El proyecto está escrito en C y sigue la Norma de 42.
- **MiniLibX**: Se requiere la librería gráfica MiniLibX para la gestión de ventanas y gráficos.
- **libft**: Se permite el uso de la librería libft.

## Compilación
Para compilar el proyecto, asegúrate de tener `make` instalado y ejecuta el siguiente comando en la raíz del proyecto:

```bash
make

Esto generará un ejecutable llamado so_long.
Ejecución
Para ejecutar el juego, utiliza el siguiente comando, proporcionando un archivo de mapa .ber como argumento:

bash
./so_long maps/map1.ber

Controles del Juego

    W: Mover hacia arriba.
    A: Mover hacia la izquierda.
    S: Mover hacia abajo.
    D: Mover hacia la derecha.
    ESC: Cerrar el juego.

Formato del Mapa (.ber)
El mapa debe estar compuesto por los siguientes caracteres:

    0: Espacio vacío.
    1: Muro.
    C: Coleccionable.
    E: Salida.
    P: Posición inicial del jugador.

Ejemplo de un mapa válido:

text
1111111111111
10010000000C1
1000011111001
1P0011E000001
1111111111111

Manejo de Errores
El programa manejará errores relacionados con mapas inválidos y mostrará mensajes apropiados en caso de fallos.
Bonus (Opcional)
Se pueden implementar funcionalidades adicionales como:

    Enemigos que hagan perder al jugador al tocarlos.
    Animaciones de sprites.
    Mostrar el contador de movimientos directamente en la pantalla.

Contribuciones
Si deseas contribuir al proyecto, siéntete libre de hacer un fork y enviar pull requests con mejoras o correcciones.
Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

text

### Notas:
1. Asegúrate de personalizar cualquier sección según sea necesario para reflejar con precisión tu proyecto y su estado actual.
2. Puedes agregar más detalles sobre las funciones específicas o características que hayas implementado en tu juego.
3. Si tienes una licencia específica, asegúrate de incluirla o mencionarla en el README.

Este README proporciona una visión general clara del proyecto y debería ayudar a otros a entender cómo usarlo y contribuir a él.
