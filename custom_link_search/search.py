from langchain.utilities import DuckDuckGoSearchAPIWrapper

ddg_search = DuckDuckGoSearchAPIWrapper()

# Const of the total number of results to consider
RESULTS_PER_QUESTION = 3

def web_search(query: str, num_results: int = RESULTS_PER_QUESTION) -> str:
    """
    Searches the web with a query

    Parameters:
    -----------
    query: search query
    num_results: number of results per query

    Returns:
    -----------
    list of relevant urls
    """
    
    results = ddg_search.results(query, num_results)
    return [r["link"] for r in results]
