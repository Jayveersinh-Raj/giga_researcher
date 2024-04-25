# Summary template
SUMMARY_TEMPLATE = """{text} 

-----------

Using the above text, answer in short the following question: 

> {question}

-----------
if the question cannot be answered using the text, imply summarize the text. Include all factual information, numbers, stats etc if available.""" 


# Research prompt
RESEARCH_REPORT_TEMPLATE = """Information:
--------
{research_summary}
--------

Using the above information, answer the following question or topic: "{question}" in a detailed report -- \
The report should focus on the answer to the question, should be well structured, informative, \
in depth, with facts and numbers if available and a minimum of 1,200 words.

You should strive to write the report as long as you can using all relevant and necessary information provided.
You must write the report with markdown syntax.
You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions.
Write all used source urls at the end of the report, and make sure to not add duplicated sources, but only one reference for each.
You must write the report in apa format. If the question is in Russian report should also be in Russian.
Please do your best, this is very important to my career.""" 