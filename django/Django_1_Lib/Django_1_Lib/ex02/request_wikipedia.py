import requests 
import json 
import dewiki 
import sys  

def request_wikipedia(search_term):
    """
    Fetches information from Wikipedia for a given search term and saves it to a file.

    Args:
    search_term (str): The term to search for on Wikipedia.

    The function performs the following steps:
    1. Formats the filename based on the search term.
    2. Makes a request to the Wikipedia API.
    3. Processes the response and extracts the relevant content.
    4. Deformats the wiki content.
    5. Saves the content to a file.

    If successful, it prints a success message. Otherwise, it prints an error message.
    """
    # Format the filename by replacing spaces with underscores and adding .wiki extension
    filename = search_term.replace(" ", "_") + ".wiki"
    
    # Configure the Wikipedia API URL (in English)
    url = "https://en.wikipedia.org/w/api.php"
    
    # Define a dictionary params and set the parameters for the API request
    params = {
        "action": "query",
        "format": "json", 
        "titles": search_term,  
        "prop": "extracts",  
        "explaintext": True, 
        "exintro": True, 
        "redirects": 1,  
        "exsectionformat": "plain" 
    }

    try:
        # Define a User-Agent to identify the request, otherwise it returns blank
        headers = {'User-Agent': 'request_wikipedia'}
        
        # Make a GET request to the Wikipedia API with the defined User-Agent
        response = requests.get(url, params=params, headers=headers)
        
        response.raise_for_status()
        
        data = response.json()
        
        # Get the first (and only) page from the result
        page = next(iter(data["query"]["pages"].values()))
        
        # Check if the extract is present and not empty
        if "extract" in page and len(page["extract"].strip()) > 0:
            content = dewiki.from_string(page["extract"])
        else:
            content = f"No information available on Wikipedia for: {search_term}"
        
        # Write the deformatted content to the file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        
        print(f"File {filename} created successfully.")
    
    except requests.RequestException as e:
        print(f"Error making the request: {e}")
    
    except json.JSONDecodeError:
        print("Error decoding the JSON response.")
    
    except Exception as e:
        print(f"Unexpected error: {e}")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 request_wikipedia.py \"search term\"")
    else:
        request_wikipedia(sys.argv[1])



# pip install -r requirement.txt
# python3 request_wikipedia.py "Albert Einstein"
