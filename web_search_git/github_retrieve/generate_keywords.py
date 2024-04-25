from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from .tokens_keys import GIGACHAT_API_KEY

# Load the GigaChat
chat = GigaChat(credentials=GIGACHAT_API_KEY,
                scope="GIGACHAT_API_CORP",
                verify_ssl_certs=False)

# Message for the GigaChat
messages = [
    SystemMessage(
        content="You are researcher that will explain any topic given to you"
    )
]


def generate_keywords(query: str) -> list:
  """
  Generate keywords from the prompt to search the github database

  Parameters:
  -----------
  query: The query from the gigachat planner agent

  Returns:
  -----------
  list: list of keywords to search in the github database
  """

  # LLM instructions
  messages.append(HumanMessage(content=f"""You are given a user prompt. The user wants to find relevant projects on GitHub, which do the software project he needs. Your task is to help the user simplify the content of his text to be suitable as a GitHub query of 2-3 words. The user prompt can be a search for a short description or a search based on the necessary functionality and microservices.
    Here are examples of a prompt and what should your output be:
    Prompt: What are the current state of the art in PEFT and LoRA?
    output: PEFT, LoRA
    Prompt: What are the existing prompt tuning techniques?
    output: prompt tuning 
    Prompt: What is the difference between transformer and informer?
    output: transformer, informer
    Here is the user prompt: {query}
    Write the output of the prompt above. Don’t write any other information so that I can directly take your output and store it as the output of the prompt."""))

  # Generate queries using keywords, entities, and Boolean operators
  res = chat(messages)
  messages.append(res)
  keywords= res.content.split()
  queries = []

  for keyword in keywords:
          query = keyword

          # Only consider repos with 10 or more stars, forks are considered.
          advanced_query = f"{query} (star:>=10 NOT fork:true)"
          queries.append(advanced_query)

  return keywords