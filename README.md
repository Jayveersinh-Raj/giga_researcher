# <img width="70" alt="image" src="https://github.com/Jayveersinh-Raj/innoagent/assets/69463767/0b07bac1-9f91-41d6-a511-55c9f0fe3498"> Giga Researcher 
Russian description can be accessed [here](README_RUS.md).
### ✨ A literature analysis tool that will help researchers study articles and write code faster.
### ✨ Giga Researcher is an autonomous system based on AI agents designed for comprehensive online research on a variety of tasks. The agent can produce detailed, factual, and unbiased research reports, with customization options for focusing on relevant resources.
### 😎 It is powered by [GigaChat](https://developers.sber.ru/docs/ru/gigachat/overview) and [GigaChain](https://github.com/ai-forever/gigachain). 

## System design:
### The workflow runs "planner", "execution", and "report generator" agents to perform the literature analysis and create a report. The planner generates research questions (RQ). Then, multiple execution agents seek the most relevant information based on RQs. Finally, the report generator filters and aggregates all crawled information and creates a research report.

![Workflow](https://github.com/Jayveersinh-Raj/innoagent/assets/69463767/bca3dc67-8812-4f77-97ab-8b589c16e176)

<br>


## ✨ How to use it

### 📖 Note: Make sure to put `GITHUB` and `GIGACHAIN` API keys in `secret_key.env`.

### 👉There are `arxiv` and `web crawl` search retrievers. Both generate reports for asked questions or prompts with `paper titles` for the former and `URL references` for the latter retrievers type.
### 👉Additionally, there is a `custom link search` that lets the user query provided `URL` to generate a report based on a prompt. This also includes code links from GitHub.

## ✨ Code structure and installations for `arxiv` and `web` search
### Install all the dependencies using `requirements.txt` by navigating to the parent directory, and creating a virtual environment (recommended).
    pip install -r requirements.txt
### 💻`arxiv_search_git` &rarr; Contains the files to run the arxiv retriever along with GitHub repo links. The `github_retrieve` directory, handles the GitHub part of the agent. `main.py` is the entry point. Navigate to the directory `arxiv_search_git` and run the following:
    cd arxiv_search_git/
    python main.py
### 💻`web_search_git` &rarr; Contains the files to run the web retriever along with GitHub repo links. The `github_retrieve` directory, handles the GitHub part of the agent. `main.py` is the entry point. Navigate to the directory `web_search_git` and run the following:
    cd web_search_git/
    python main.py    

### ✨ The solution can be accessed locally via the route below:
    http://localhost:8000/giga_research/playground/
### 📖 Note: Both the arxiv and web search should be hosted on the same address, hence, either change the ports or use them separately. Also, put your own `GITHUB` and `GIGACHAIN` API keys in `secret_key.env`.

## ✨ Code structure and installations for `custom link search`
### Install all the dependencies using `requirements.txt` by navigating to the parent directory, and creating a virtual environment (recommended).
    pip install -r requirements.txt
### `main.py` is the entry point. Navigate to the directory `custom_link_search` and run the following:
    cd custom_link_search/
    python main.py    

### ✨ The solution can be accessed locally via the route below:
    http://localhost:4000/research-assistant/playground/
### 📖 Note: Put your own `GITHUB` and `GIGACHAIN` API keys in `secret_key.env`. This service would be hosted on `port:4000`, hence can be simultaneously used with `arxiv` or `web` agent.

