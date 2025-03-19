import sys
import requests
from bs4 import BeautifulSoup

def get_first_valid_link(soup):
    """
    Obtiene el primer enlace válido de una página de Wikipedia.

    Args:
    - soup (BeautifulSoup): Objeto BeautifulSoup que contiene el contenido HTML de la página.

    Returns:
    - str: URL del primer enlace válido encontrado.
    - None: Si no se encuentra ningún enlace válido.
    """
    # Busca el contenido principal de la página
    content = soup.find(id="mw-content-text")
    if not content:
        return None

    # Itera sobre los párrafos del contenido principal
    for paragraph in content.select("p"):
        for link in paragraph.find_all('a', recursive=False):
            href = link.get('href', '')
            # Verifica si el enlace es válido (no es un enlace a ayuda o páginas especiales)
            if href.startswith('/wiki/') and ':' not in href and not href.startswith('/wiki/Help:') and not href.startswith('/wiki/Wikipedia:'):
                return 'https://en.wikipedia.org' + href
    return None

def roads_to_philosophy(start_term):
    """
    Encuentra el camino desde un término inicial hasta la página de Wikipedia 'Philosophy'.

    Args:
    - start_term (str): Término inicial desde donde comienza la búsqueda.

    Returns:
    - None: Imprime el camino recorrido y el número de pasos al llegar a 'Philosophy',
      o informa si se encuentra un callejón sin salida o un bucle infinito.
    """
    # Construye la URL inicial basada en el término proporcionado
    url = f"https://en.wikipedia.org/wiki/{start_term.replace(' ', '_')}"
    
    # Lista para almacenar las páginas visitadas
    visited = []

    try:
        while True:
            try:
                # Configura los encabezados para la solicitud HTTP
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                # Realiza una solicitud GET a la URL actual
                response = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
                response.raise_for_status()  # Lanza una excepción si ocurre un error HTTP

                # Analiza el contenido HTML de la página
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Obtiene el título de la página actual
                title = soup.find('h1', id='firstHeading').text.strip()

                # Verifica si ya se ha visitado esta página (bucle infinito)
                if title in visited:
                    print("It leads to an infinite loop !")
                    break

                # Imprime el título de la página actual y lo agrega a la lista de visitados
                print(title)
                visited.append(title)

                # Verifica si se ha llegado a la página "Philosophy"
                if title == "Philosophy":
                    break

                # Obtiene el siguiente enlace válido
                next_link = get_first_valid_link(soup)
                if not next_link:
                    print("It leads to a dead end !")
                    break

                # Actualiza la URL para continuar con el siguiente enlace
                url = next_link

            except requests.Timeout:
                print("Error: The request timed out.")  # Error por tiempo de espera agotado
                break
            except requests.HTTPError as e:
                print(f"HTTP Error occurred: {e}")  # Error HTTP específico
                break
            except requests.RequestException as e:
                print(f"An error occurred during the request: {e}")  # Otro error relacionado con solicitudes HTTP
                break

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")  # Manejo de interrupciones con Ctrl+C
    finally:
        # Imprime el número total de pasos recorridos al final del programa
        if visited:
            print(f"{len(visited)} roads from {start_term} to {'philosophy' if title == 'Philosophy' else 'error'} !")
        else:
            print("No pages were successfully visited.")

if __name__ == "__main__":
    """
    Punto de entrada principal del programa. Procesa los argumentos de línea de comandos y 
    llama a la función `roads_to_philosophy` con el término inicial proporcionado.
    
    Uso:
      python3 roads_to_philosophy.py "término inicial"
    
    Ejemplo:
      python3 roads_to_philosophy.py "42 (number)"
    """
    # Verifica que se haya pasado exactamente un argumento al programa
    if len(sys.argv) != 2:
        print("Usage: python3 roads_to_philosophy.py \"search term\"")
        sys.exit(1)

    # Obtiene el término inicial desde los argumentos y llama a la función principal
    roads_to_philosophy(sys.argv[1])


