import torch
from .embeddings import sentence_encoder
import requests
import base64
import re

def match_repository(gigachain_text: str, repo_url: str) -> tuple[float, str]:
    """
    Matches the repository based on Gigachain text similarity using embeddings.

    Parameters:
    -----------
    gigachain_text: The Gigachain-generated detailed text.
    repo_url: The URL of the repository to match.

    Returns:
    -----------
    A tuple containing the similarity score and summary of the repository.
    """

    # Clean the readme for similarity
    summary = clean_readme(get_readme(repo_url))

    # Generate embeddings for Gigachain text and repository summary
    gigachain_embedding = sentence_encoder.encode(gigachain_text, convert_to_tensor=True)
    summary_embedding = sentence_encoder.encode(summary, convert_to_tensor=True)

    gigachain_embedding = gigachain_embedding.unsqueeze(0)  # Add a leading dimension for batch size (1)
    summary_embedding = summary_embedding.unsqueeze(0)  # Do the same for summary embedding
    similarity = torch.nn.functional.cosine_similarity(gigachain_embedding, summary_embedding).item()


    similarity = torch.nn.functional.cosine_similarity(gigachain_embedding, summary_embedding).item()

    return similarity, summary


def rank_repositories(repositories: tuple[str, float, str], number_of_repo: int = 5) -> list:
    """
    Implement ranking logic based on similarity and returns top 5 

    Parameters:
    -----------
    repositories: tuples with similarity, summary, and html_url
    number_of_repo: total repos to consider and give it to the user, by default 5

    Returns:
    -----------
    list: the urls of the top #number_of_repo based on similarity, by default 5
    """

    ranked_repos = sorted(repositories, key=lambda repo: repo["similarity"], reverse=True)
    ranked_repos = ranked_repos[:number_of_repo]
    ranked_repos = [item['html_url'] for item in ranked_repos]
    return ranked_repos


def get_readme(repo_url: str) -> str:
  """
  Retrieves the README content from a GitHub repository URL.

  Parameters:
  -----------
  repo_url: The URL of the GitHub repository.

  Returns:
  ----------
  A string containing the README content, or None if an error occurs.
  """

  base_url = "https://api.github.com/repos/"
  username, repo_name = repo_url.split("/")[-2:]  # Extract username and repo name
  url = f"{base_url}{username}/{repo_name}/contents/README.md"

  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    if "content" in data:
              readme_content = base64.b64decode(data["content"]).decode("utf-8")
              return readme_content
    else:
              print("README not found.")
              return " "
  else:
    print(f"Error retrieving README: {response.status_code}")
    return " "


def clean_readme(content: str) -> str:
    """
    Cleans the readme using regular expressions

    Parameters:
    -----------
    content: content of the readme file

    Returns:
    -----------
    str: cleaned readme content
    """

    # Remove the specified structure
    content = re.sub(r'\[\!\[.*?\)\(', '', content)

    # Remove images
    content = re.sub(r'\!\[image\]\([^)]+\)', '', content)

    # Remove links
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
    # Remove HTML tags and their content
    content = re.sub(r'<[^>]*>', '', content)

    # Remove standalone links without anchor text
    content = re.sub(r'https?://\S+', '', content)

    # Remove emojis
    content = re.sub(r'[^\x00-\x7F]+', '', content)
    # Remove patterns ![text](...)
    content = re.sub(r'\!\[.*?\]\(.*?\)', '', content)

    # Remove patterns ![text](...)
    content = re.sub(r'\!\[[^\]]*\]\([^\)]*\)', '', content)


    # Remove everything between two | characters on a single line
    content = re.sub(r'\|[^|]*\|', '', content)

    # Remove everything between two colons if they are separated by multiple -
    content = re.sub(r':-{2,}:', '', content)

    # Remove patterns ![text](...)
    content = re.sub(r"\!\[[^\]]*\]\([^\)]*\)", '', content)

    # Remove patterns ![text](...
    content = re.sub(r'\!\[[^\]]*\]\(', '', content)

    # Remove duplicate newlines
    content = re.sub(r'\n{2,}', '\n', content)

    # Remove duplicate spaces
    content = re.sub(r' {2,}', ' ', content)

    # Remove lines with only whitespace
    content = re.sub(r'^\s*\n', '', content, flags=re.MULTILINE)
    return content
