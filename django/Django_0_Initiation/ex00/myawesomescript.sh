
# Choice of interpreter
#!/bin/sh

# Check if an argument (URL) has been provided
if [ -z "$1" ]; then
  echo "Usage: $0 <bit.ly URL>" >&2
  exit 1
fi

# Get the final URL after redirects
curl -Ls -o /dev/null -w %{url_effective} "$1"




# COMENTARIOS#


# Elecccion del Interprete
#!/bin/sh


# Verificar si se ha proporcionado un argumento (URL)
if [ -z "$1" ]; then

    Inicia una estructura condicional if.
    -z es un operador que comprueba si una cadena está vacía.
    "$1" se refiere al primer argumento pasado al script.
    Si $1 está vacío (no se proporcionó ningún argumento), la condición es verdadera.

echo "Usage: $0 <bit.ly URL>" >&2
    Si no se proporcionó un argumento, muestra un mensaje de uso.
    $0 representa el nombre del script.
    >&2 redirige la salida al error estándar (stderr).
exit 1
    Termina la ejecución del script con un código de salida 1, indicando un error.
fi
    Cierra la estructura condicional if.

# Obtener la URL final después de las redirecciones
curl: Herramienta para transferir datos usando varios protocolos.
-L: Sigue las redirecciones automáticamente.
-s: Modo silencioso, suprime la barra de progreso.
-o /dev/null: Descarta el contenido de la página.
-w %{url_effective}: Muestra la URL final después de todas las redirecciones.
"$1": Usa el primer argumento proporcionado como la URL a procesar.








