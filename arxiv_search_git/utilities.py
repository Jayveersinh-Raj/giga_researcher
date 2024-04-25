# List to store the paper titles
titles_list = []

def add_titles(text: str) -> str:
    """
    Adds titles of the papers for reference

    Parameters:
    -----------
    text: The content with titles of paper

    Returns:
    ----------
    str: The content with titles of papers as a reference
    """

    split_text = text.split(':-')
    titles_list.append(split_text[1])
    return text


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
     
    content = []
    for l in list_of_lists:
        content.append("\n\n".join(l))
    return "\n\n".join(content)


def with_ref(text):
    """
    Adds references with the text.

    Parameters:
    -----------
    text: The content in text format (str)

    Returns:
    ----------
    str: content with the titles of papers as references 
    """

    string_url = "\n*".join(titles_list)
    return text + "\n\nReferences \n-------------- \n" + '*' + string_url

