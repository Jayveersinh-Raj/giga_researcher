from fastapi import FastAPI
from langserve import add_routes
from langchain.schema.runnable import RunnablePassthrough
from utilities import collapse_list_of_lists, with_ref
from langchain.chat_models.gigachat import GigaChat
from langchain.schema.output_parser import StrOutputParser
from github_retrieve.tokens_keys import GIGACHAT_API_KEY
from github_retrieve.repo_retrieve import retrive_repos
from chains import full_research_chain
from prompts import prompt
import uvicorn


# The GigaChat LLM initlialization
GigaChat(credentials=GIGACHAT_API_KEY,
                scope="GIGACHAT_API_CORP",
                verify_ssl_certs=False)

# The main chain, putting everything togather
chain = RunnablePassthrough.assign(
    research_summary= full_research_chain | collapse_list_of_lists
) | prompt | GigaChat(credentials = GIGACHAT_API_KEY,
                      scope="GIGACHAT_API_CORP",
                      verify_ssl_certs=False) | StrOutputParser() | with_ref | retrive_repos


# Driver code, with gigaserve hosting
if __name__ ==  "__main__":

  app = FastAPI()

  add_routes(
      app,
      chain,
      path = "/giga_research"
   )
  
  uvicorn.run(app, host="localhost", port=8000)