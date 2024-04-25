import requests
from bs4 import BeautifulSoup

# list for the urls used in the contents
success_urls = []

def scrape_text(url: str) -> str:
    """
    Scrapes the text from the url

    Parameters:
    -----------
    url: url to scrape the text from

    Returns:
    -----------
    str: text extracted from the url
    """

    # Send a GET request to the webpage
    try:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # save the urls
            success_urls.append(url)

            # Parse the content of the request with BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract all text from the webpage
            page_text = soup.get_text(separator=" ", strip=True)

            # Print the extracted text
            return page_text
        else:
            return f"Failed to retrieve the webpage: Status code {response.status_code}"
    except Exception as e:
        print(e)
        return f"Failed to retrieve the webpage: {e}"
    