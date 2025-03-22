# Importa el módulo requests para realizar solicitudes HTTP
import requests  
# Importa el módulo json para manejar datos JSON
import json  
# Importa el módulo dewiki para desformatear contenido wiki
import dewiki  
# Importa el módulo sys para manejar argumentos de línea de comandos
import sys  

# Define una función llamada request_wikipedia que toma un término de búsqueda
def request_wikipedia(search_term):
    # Formatea el nombre del archivo reemplazando espacios por guiones bajos, y 
    # le añade la extensión .wiki
    filename = search_term.replace(" ", "_") + ".wiki"
    
    # Configura la URL de la API de Wikipedia (cambia a inglés si es necesario)
    url = "https://es.wikipedia.org/w/api.php"
    
    # Define un diccionario params y configura los parámetros para la solicitud 
    # a la API
    # "action": "query" realiza una consulta
    # "format": "json"  la respuesta debe ser en formato json
    # "titles": search_term  Define el título o término de búsqueda que se está 
    #           consultando en Wikipedia.
    # "explaintext": True: Indica que el extracto debe ser en texto plano
    # "exintro": True: Especifica que se desea obtener solo la introducción (intro) del 
    #           extracto, es decir, el primer párrafo o sección introductoria de la página.
    # "redirects": 1: Sigue redirecciones automáticamente
    # "exsectionformat": "plain": Formato de texto plano
    params = {
        "action": "query",  # Realiza una consulta
        "format": "json",  # La respuesta debe ser en formato json
        "titles": search_term,  # Define el título o término de búsqueda
        "prop": "extracts",  # Propiedad para obtener extractos
        "explaintext": True,  # Indica que el extracto debe ser en texto plano
        "exintro": True,  # Obtiene solo la introducción del extracto
        "redirects": 1,  # Sigue redirecciones automáticamente
        "exsectionformat": "plain"  # Formato de texto plano
    }

    try:
        # Define un User-Agent para identificar la solicitud, sino devuelve en blanco
        headers = {'User-Agent': 'equest_wikipedia'}
        
        # Realiza la solicitud GET a la API de Wikipedia con el User-Agent definido
        response = requests.get(url, params=params, headers=headers)
        
        # Lanza una excepción si la respuesta HTTP no es exitosa
        response.raise_for_status()
        
        # Convierte la respuesta JSON a un diccionario de Python
        data = response.json()
        
        # Obtiene la primera (y única) página del resultado
        page = next(iter(data["query"]["pages"].values()))
        
        # Verifica si el extracto está presente y no vacío
        if "extract" in page and len(page["extract"].strip()) > 0:
            # Desformatea el contenido wiki usando dewiki
            content = dewiki.from_string(page["extract"])
        else:
            # Si no hay contenido, escribe un mensaje alternativo
            content = f"No hay información disponible en Wikipedia para: {search_term}"
        
        # Escribe el contenido desformateado en el archivo
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        
        # Imprime un mensaje de éxito al crear el archivo
        print(f"Archivo {filename} creado exitosamente.")
    
    except requests.RequestException as e:
        # Maneja errores de solicitud HTTP
        print(f"Error al realizar la solicitud: {e}")
    
    except json.JSONDecodeError:
        # Maneja errores de decodificación JSON
        print("Error al decodificar la respuesta JSON.")
    
    except Exception as e:
        # Maneja cualquier otro error inesperado
        print(f"Error inesperado: {e}")

# Verifica si el script se está ejecutando directamente (no importado como módulo)
if __name__ == "__main__":
    # Verifica si se proporcionó exactamente un argumento de línea de comandos
    if len(sys.argv) != 2:
        # Imprime el mensaje de uso si no se proporcionó un argumento
        print("Uso: python3 request_wikipedia.py \"término de búsqueda\"")
    else:
        # Llama a la función principal con el término de búsqueda proporcionado
        request_wikipedia(sys.argv[1])


# pip install -r requirements.txt.
#python3 request_wikipedia.py "Albert Einstein"


