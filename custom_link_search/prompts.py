from langchain.prompts import ChatPromptTemplate
from templates import SUMMARY_TEMPLATE, RESEARCH_REPORT_TEMPLATE

# System prompt
WRITER_SYSTEM_PROMPT = "You are an AI critical thinker research assistant. Your sole purpose is to write well written, critically acclaimed, objective and structured reports on given text with references."

# Summary prompt
SUMMARY_PROMPT = ChatPromptTemplate.from_template(SUMMARY_TEMPLATE)

# Search prompt
SEARCH_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "user",
            "User will give you the url: {url}; Write 3 google search queries to search in that form an "
            "objective opinion from the following: {question}\n"
            "You must respond with a list of strings in the following format: "
            '["url", "query 1", "query 2", "query 3"].',
        ),
    ]
)

# Messages prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", WRITER_SYSTEM_PROMPT),
        ("user", RESEARCH_REPORT_TEMPLATE),
    ]
)
