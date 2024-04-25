from langchain.chat_models.gigachat import GigaChat
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from prompts import SUMMARY_PROMPT, SEARCH_PROMPT, prompt
from retrieve import retriever
from utilities import add_titles, collapse_list_of_lists, with_ref
from dotenv import load_dotenv
import os
import json

# Load dot env for the api
load_dotenv("../secret_keys.env")

# Gigachat api key
GIGACHAT_API_KEY = os.getenv('GIGACHAT_API_KEY')

# Search question chain
search_question_chain = SEARCH_PROMPT | GigaChat(credentials = GIGACHAT_API_KEY,
                                                 scope="GIGACHAT_API_CORP",
                                                 verify_ssl_certs=False) | StrOutputParser() | json.loads


# Scrape and Summarize chain
scrape_and_summarize_chain = RunnablePassthrough.assign(
    summary =  SUMMARY_PROMPT | GigaChat(credentials = GIGACHAT_API_KEY,
                                         scope="GIGACHAT_API_CORP",
                                         verify_ssl_certs=False) 
                              | StrOutputParser()
) | (lambda x: f"Title:- {x['doc'].metadata['Title']}:-\n\nSUMMARY: {x['summary']}") | add_titles


# Web search chain
web_search_chain = RunnablePassthrough.assign(
    docs = lambda x: retriever.get_summaries_as_docs(x["question"])
)| (lambda x: [{"question": x["question"], "doc": u} for u in x["docs"]]) | scrape_and_summarize_chain.map()

# Full research chain
full_research_chain = search_question_chain | (lambda x: [{"question": q} for q in x]) | web_search_chain.map()


# The final chain, putting everything together
chain = RunnablePassthrough.assign(
    research_summary= full_research_chain | collapse_list_of_lists
) | prompt | GigaChat(credentials = GIGACHAT_API_KEY,
                      scope="GIGACHAT_API_CORP",
                      verify_ssl_certs=False) | StrOutputParser() | with_ref