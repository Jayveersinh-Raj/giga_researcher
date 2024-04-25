# <img width="70" alt="image" src="https://github.com/Jayveersinh-Raj/innoagent/assets/69463767/0b07bac1-9f91-41d6-a511-55c9f0fe3498"> Giga Researcher 
### ✨ A literature analysis tool that will help researchers study articles and write code faster.
### ✨ Giga Researcher is an autonomous agent designed for comprehensive online research on a variety of tasks. The agent can produce detailed, factual, and unbiased research reports, with customization options for focusing on relevant resources.
### 😎 It is powered by [GigaChat](https://developers.sber.ru/docs/ru/gigachat/overview) and [GigaChain](https://github.com/ai-forever/gigachain). 

## System design:
### The main idea is to run "planner" and "execution" agents, whereas the planner generates questions to research, and the execution agents seek the most related information based on each generated research question. Finally, the reporter generator filters and aggregates all related information and creates a research report.

![Workflow](https://github.com/Jayveersinh-Raj/innoagent/assets/69463767/bca3dc67-8812-4f77-97ab-8b589c16e176)

<br>


## ✨ How to use it
### 👉There are 2 retrievers, one is `arxiv` search and the other is `web crawl`.
### 👉Both generates reports according to the asked question, or given prompt along with `URL references` for `web crawl`, and `paper titles` for `arxiv`.
### 👉Additionally there is a `custom link search` that takes in a `URL`, and lets the user query the URL to generate a report based on the question or given prompt. This also includes code links from Git Hub.

## ✨ Code structure and installations for `arxiv` and `web` search
### Install all the dependencies using `requirements.txt` by navigating to the parent directory, and creating a virtual environment (if needed).
    pip install -r requirements.txt
### 💻`arxiv_search_git` &rarr; Contains the files to run the arxiv retriever along with GitHub repo links. The `github_retrieve` directory, handles the github part of the agent. `main.py` is the entry point. Navigate to the directory `arxiv_search_git` and run the following:
    python main.py
### 💻`web_search_git` &rarr; Contains the files to run the web retriever along with GitHub repo links. The `github_retrieve` directory, handles the github part of the agent. `main.py` is the entry point. Navigate to the directory `web_search_git` and run the following:
    python main.py    

### ✨ Now it'll be hosted on the local machine, go to the route below, which is the default:
    http://localhost:8000/giga_research/playground/
### 📖 Note: Both the arxiv and web search should be hosted on the same address, hence, either change the ports or use them separately. Also, put your own `GITHUB` and `GIGACHAIN` API keys in `secret_key.env`.

## ✨ Code structure and installations for `custom link search`
### Install all the dependencies using `requirements.txt` by navigating to the parent directory, and creating a virtual environment (if needed).
    pip install -r requirements.txt
### `main.py` is the entry point. Navigate to the directory `custom_link_search` and run the following:
    python main.py    

### ✨ Now it'll be hosted on the local machine, go to the route below, which is the default:
    http://localhost:4000/research-assistant/playground/
### 📖 Note: Put your own `GITHUB` and `GIGACHAIN` API keys in `secret_key.env`. This service would be hosted on `port:4000`, hence can be simultaneously used with `arxiv` or `web` agent.

