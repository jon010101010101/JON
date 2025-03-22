import sys  # Importa el módulo sys para manejar argumentos de la línea de comandos
import requests  # Importa requests para realizar solicitudes HTTP
from bs4 import BeautifulSoup  # Importa BeautifulSoup para analizar HTML

def get_first_valid_link(soup):
    """
    Obtiene el primer enlace válido de una página de Wikipedia.

    Args:
    - soup (BeautifulSoup): Objeto BeautifulSoup con el contenido HTML de la página.

    Returns:
    - str: URL del primer enlace válido encontrado.
    - None: Si no se encuentra ningún enlace válido.
    """
    # Busca el contenido principal de la página
    content = soup.find(id="mw-content-text")
    if not content:  # Si no hay contenido principal, retorna None
        return None

    # Itera sobre los párrafos dentro del contenido principal
    for paragraph in content.select("p"):
        for link in paragraph.find_all('a', recursive=False):  # Encuentra enlaces dentro del párrafo
            href = link.get('href', '')  # Obtiene el atributo href del enlace
            # Verifica si el enlace es válido (no enlaces especiales ni páginas de ayuda)
            if href.startswith('/wiki/') and ':' not in href and not href.startswith('/wiki/Help:') and not href.startswith('/wiki/Wikipedia:'):
                return 'https://en.wikipedia.org' + href  # Retorna la URL completa del enlace válido
    return None  # Si no se encuentra ningún enlace válido, retorna None

def roads_to_philosophy(start_term):
    """
    Encuentra el camino desde un término inicial hasta la página 'Philosophy' en Wikipedia.

    Args:
    - start_term (str): Término inicial desde donde comienza la búsqueda.

    Returns:
    - None: Imprime el camino recorrido y el número de pasos hasta llegar a 'Philosophy',
      o informa si se encuentra un callejón sin salida o un bucle infinito.
    """
    # Construye la URL inicial basada en el término proporcionado
    url = f"https://en.wikipedia.org/wiki/{start_term.replace(' ', '_')}"
    
    # Lista para almacenar las páginas visitadas
    visited = []

    try:
        while True:  # Bucle infinito para continuar navegando por los enlaces válidos
            try:
                # Configura los encabezados para la solicitud HTTP
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                # Realiza una solicitud GET a la URL actual
                response = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
                response.raise_for_status()  # Lanza una excepción si ocurre un error HTTP

                # Analiza el contenido HTML de la página con BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Obtiene el título de la página actual
                title = soup.find('h1', id='firstHeading').text.strip()

                # Verifica si esta página ya fue visitada (para evitar bucles infinitos)
                if title in visited:
                    print("It leads to an infinite loop !")  # Mensaje indicando bucle infinito
                    return

                # Imprime el título de la página actual y lo agrega a la lista de páginas visitadas
                print(title)
                visited.append(title)

                # Verifica si hemos llegado a la página "Philosophy"
                if title == "Philosophy":
                    print(f"{len(visited)} roads from {start_term} to philosophy !")  # Mensaje indicando éxito
                    return

                # Obtiene el siguiente enlace válido
                next_link = get_first_valid_link(soup)
                if not next_link:  # Si no hay un enlace válido, indica callejón sin salida
                    print("It's a dead end !")
                    return

                # Actualiza la URL para continuar con el siguiente enlace
                url = next_link

            except requests.exceptions.HTTPError as e:  # Maneja errores HTTP específicos
                if e.response.status_code == 404:  # Si ocurre un error 404, indica callejón sin salida
                    print("It's a dead end !")
                else:
                    print(f"HTTP Error occurred: {e}")  # Mensaje indicando otro error HTTP
                return

            except (requests.Timeout, requests.RequestException) as e:  # Maneja otros errores de solicitud HTTP
                print(f"An error occurred during the request: {e}")  # Mensaje indicando error general en la solicitud
                return

    except KeyboardInterrupt:  # Maneja interrupciones del usuario con Ctrl+C
        print("\nProgram interrupted by user.")  # Mensaje indicando interrupción del programa

if __name__ == "__main__":
    """
    Punto de entrada principal del programa. Procesa los argumentos de línea de comandos y 
    llama a la función `roads_to_philosophy` con el término inicial proporcionado.
    
    Uso:
      python3 roads_to_philosophy.py "término inicial"
    
    Ejemplo:
      python3 roads_to_philosophy.py "42 (number)"
    """
    if len(sys.argv) != 2:  # Verifica que se haya pasado exactamente un argumento al programa
        print("Usage: python3 roads_to_philosophy.py \"search term\"")  # Mensaje indicando uso correcto del programa
        sys.exit(1)  # Finaliza el programa con código de salida 1 (error)

    roads_to_philosophy(sys.argv[1])  # Llama a la función principal con el término inicial proporcionado




# pip install -r requirement.txt
# python3 roads_to_philosophy.py "42 (number)" 


