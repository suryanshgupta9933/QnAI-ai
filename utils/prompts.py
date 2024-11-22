# Importing Dependencies
import os
from langchain_core.messages import SystemMessage, HumanMessage

# Tagging Prompt
def tagging_prompt(title: str, body: str, tags: list):
    system_message = """You are responsible for analyzing and tagging questions on a tech support forum.
Accurate tagging sorts queries efficiently, helping users and support personnel locate and resolve issues quickly.

Key Guielines:
1. Tag questions with the most relevant category.
2. Create tags that are broad and general like you would find on stackoverflow, tech support forums, github etc.
3. Avoid using tags that are too specific.
4. Choose tags that are most likely to be searched by users.
5. There are tags provieded by the user as well, extend the list only if necessary.
6. Only return a list of tags that best describe the issue and nothing else in response.
7. For example: ['tag1', 'tag2', 'tag3']

Please provide a list of tags that best fits the question.
"""
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content="""Here is a question that needs to be tagged:\nQuestion\nTitle: {title}\nBody: {body}\nTags: {tags}""".format(title=title, body=body, tags=tags)),
    ]
    return messages