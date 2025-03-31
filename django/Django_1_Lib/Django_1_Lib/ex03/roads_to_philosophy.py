import sys 
import requests 
from bs4 import BeautifulSoup 

def get_first_valid_link(soup):
    """
    Retrieves the first valid link from a Wikipedia page.

    Args:
    - soup (BeautifulSoup): BeautifulSoup object containing the HTML content of the page.

    Returns:
    - str: URL of the first valid link found.
    - None: If no valid link is found.
    """
    content = soup.find(id="mw-content-text")
    if not content:
        return None

    for paragraph in content.select("p"):
        for link in paragraph.find_all('a', recursive=False): 
            href = link.get('href', '') 
            if href.startswith('/wiki/') and ':' not in href and not href.startswith('/wiki/Help:') and not href.startswith('/wiki/Wikipedia:'):
                return 'https://en.wikipedia.org' + href 
    return None

def roads_to_philosophy(start_term):
    """
    Finds the path from a starting term to the 'Philosophy' page on Wikipedia.

    Args:
    - start_term (str): Initial term from which to begin the search.

    Returns:
    - None: Prints the path taken and number of steps to reach 'Philosophy',
      or reports if a dead end or infinite loop is encountered.
    """

    url = f"https://en.wikipedia.org/wiki/{start_term.replace(' ', '_')}"
    
    visited = []

    try:
        while True:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                response = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')
                
                title = soup.find('h1', id='firstHeading').text.strip()

                if title in visited:
                    print("It leads to an infinite loop !")
                    return

                print(title)
                visited.append(title)

                if title == "Philosophy":
                    print(f"{len(visited)} roads from {start_term} to philosophy !")
                    return

                next_link = get_first_valid_link(soup)
                if not next_link: 
                    print("It's a dead end !")
                    return

                url = next_link

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 404:
                    print("It's a dead end !")
                else:
                    print(f"HTTP Error occurred: {e}") 
                return

            except (requests.Timeout, requests.RequestException) as e: 
                print(f"An error occurred during the request: {e}") 
                return

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.") 

if __name__ == "__main__":
    """
    Main entry point of the program. Processes command line arguments and 
    calls the `roads_to_philosophy` function with the provided starting term.
    
    Usage:
      python3 roads_to_philosophy.py "starting term"
    
    Example:
      python3 roads_to_philosophy.py "42 (number)"
    """

    if len(sys.argv) != 2: 
        print("Usage: python3 roads_to_philosophy.py \"search term\"")
        sys.exit(1) 

    roads_to_philosophy(sys.argv[1]) 





# pip install -r requirement.txt
# python3 roads_to_philosophy.py "42 (number)" 