from scrape_text import success_urls

def collapse_list_of_lists(list_of_lists: list) -> str:
    """
    Joining several lists to put together a chunk of content for report.

    Parameters:
    -----------
    list_of_list: lists with content 

    Returns:
    -----------
    str: The concatinated (joined) one string format content
    """

    # List to store content
    content = []
    for l in list_of_lists:
        content.append("\n\n".join(l))
    return "\n\n".join(content)


def with_ref(text: str) -> str:
    """
    Adds references with the text.

    Parameters:
    -----------
    text: The content in text format (str)

    Returns:
    ----------
    str: content with the references
    """

    string_url = "\n*".join(success_urls)
    return text + "\n\nReferences \n-------------- \n" + '*' + string_url