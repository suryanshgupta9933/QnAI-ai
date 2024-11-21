# Importing Dependencies
import os
from langchain_core.prompts import ChatPromptTemplate

# Tagging Prompt
def tagging_prompt(title: str, body: str, tags: list):
    prompt_template = """You are responsible for analyzing and tagging questions on a tech support forum.
Accurate tagging sorts queries efficiently, helping users and support personnel locate and resolve issues quickly.

Key Guielines:
1. Tag questions with the most relevant category.
2. Use tags that are specific.
3. Avoid using tags that are too broad.
4. Choose tags that are most likely to be searched by users.
5. There are tags provieded by the user as well, extend the list if necessary.
6. Return a list of tags that best describe the issue.

Here is a question that needs to be tagged:
Question
Title: {title}
Body: {body}
Tags: {tags}

Please provide a list of tags that best fits the question.
""".format(title=title, body=body, tags=tags)
    prompt = ChatPromptTemplate(prompt_template)
    return prompt