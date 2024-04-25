import requests
from bs4 import BeautifulSoup

def scrape_text(url: str) -> str:
    """
    The function to scrape the text from the url

    Parameters:
    -----------
    url: The link to retrieve information

    Returns:
    -----------
    str: The content retreived from the link
    """
    
    try:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the content of the request with BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract all text from the webpage
            page_text = soup.get_text(separator=" ", strip=True)
            return page_text
        
        else:
            return f"Failed to retrieve the webpage: Status code {response.status_code}"
        
    except Exception as e:
        print(e)
        return f"Failed to retrieve the webpage: {e}"
