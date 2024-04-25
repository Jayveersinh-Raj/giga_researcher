from dotenv import load_dotenv
import os

# Load dot env for the api
load_dotenv("../secret_keys.env")

# Gigachat api key
GIGACHAT_API_KEY = os.getenv('GIGACHAT_API_KEY')

# GitHub access token
GITHUB_ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')

headers = {"Authorization": f"token {GITHUB_ACCESS_TOKEN}"}