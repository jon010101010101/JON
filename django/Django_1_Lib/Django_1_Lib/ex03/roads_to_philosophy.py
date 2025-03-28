import sys
import requests
from bs4 import BeautifulSoup

def get_first_valid_link(soup):
    """Get the first valid link from a Wikipedia page's introduction."""
    content = soup.find(id="mw-content-text")
    if not content:
        return None

    for paragraph in content.select("div.mw-parser-output > p"):
        if paragraph.find('table', {'class': 'infobox'}):
            continue
        for link in paragraph.find_all('a', recursive=False):
            if link.find_parent('i') or link.find_parent('sup'):
                continue
            href = link.get('href', '')
            if href.startswith('/wiki/') and ':' not in href:
                return 'https://en.wikipedia.org' + href
    return None

def handle_redirect(soup):
    """Handle redirections within the page content."""
    redirect = soup.find('div', class_='redirectMsg')
    if redirect:
        link = redirect.find('a')
        if link:
            return 'https://en.wikipedia.org' + link['href']
    return None

def roads_to_philosophy(start_term):
    """Find the path from an initial term to the Wikipedia page 'Philosophy'."""
    url = f"https://en.wikipedia.org/wiki/{start_term.replace(' ', '_')}"
    visited = []

    try:
        while True:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            
            redirect_url = handle_redirect(soup)
            if redirect_url:
                url = redirect_url
                continue

            title = soup.find('h1', id='firstHeading').text.strip()

            if title in visited:
                print("It leads to an infinite loop !")
                return

            print(title)
            visited.append(title)

            if title == "Philosophy":
                print(f"{len(visited)} roads from {start_term} to philosophy")
                return

            next_link = get_first_valid_link(soup)
            if not next_link:
                print("It leads to a dead end !")
                return

            url = next_link

    except requests.ConnectionError:
        print("Connection Error: Could not connect to Wikipedia server.")
    except requests.Timeout:
        print("Timeout Error: The request to Wikipedia took too long.")
    except requests.HTTPError as e:
        print(f"HTTP Error: Wikipedia server responded with an error {e.response.status_code}.")
    except requests.RequestException as e:
        print(f"Request Error: A problem occurred while accessing Wikipedia: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    finally:
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 roads_to_philosophy.py \"search term\"")
        sys.exit(1)

    roads_to_philosophy(sys.argv[1])





# pip install -r requirement.txt
# python3 roads_to_philosophy.py "42 (number)" 