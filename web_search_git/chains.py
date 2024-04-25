from langchain.chat_models.gigachat import GigaChat
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from scrape_text import scrape_text
from search import web_search
from prompts import SUMMARY_PROMPT, SEARCH_PROMPT, prompt
from utilities import collapse_list_of_lists, with_ref
import json
import os
from dotenv import load_dotenv

# Load dot env for the api
load_dotenv("../secret_keys.env")

# Gigachat api key
GIGACHAT_API_KEY = os.getenv('GIGACHAT_API_KEY')

# Scrape and summarize chain
scrape_and_summarize_chain = RunnablePassthrough.assign(
    summary = RunnablePassthrough.assign(
    text = lambda x: scrape_text(x["url"])[:10000]
)          | SUMMARY_PROMPT 
           | GigaChat(credentials = GIGACHAT_API_KEY,
                           scope="GIGACHAT_API_CORP",
                           verify_ssl_certs=False) 
           | StrOutputParser()
)          | (lambda x: f"URL: {x['url']}\n\nSUMMARY: {x['summary']}")


# Websearch chain
web_search_chain = RunnablePassthrough.assign(
    urls = lambda x: web_search(x["question"])
) | (lambda x: [{"question": x["question"], "url": u} for u in x["urls"]]) | scrape_and_summarize_chain.map()


# Search by question chain
search_question_chain = SEARCH_PROMPT | GigaChat(credentials = GIGACHAT_API_KEY,
                                                 scope="GIGACHAT_API_CORP",
                                                 verify_ssl_certs=False) | StrOutputParser() | json.loads


# Full research chain
full_research_chain = search_question_chain | (lambda x: [{"question": q} for q in x]) | web_search_chain.map()
