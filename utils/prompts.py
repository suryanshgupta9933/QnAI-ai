# Importing Dependencies
import os
from langchain_core.messages import SystemMessage, HumanMessage

# Tagging Prompt
def tagging_prompt(title: str, body: str, tags: list):
    system_message = """Tag the provided question with the most relevant categories to aid in efficient query sorting.

# Guidelines

- Tags should be general, often used terms similar to those found on platforms like Stack Overflow, GitHub, or technical forums.
- Avoid overly specific, uncommon, or niche terms.
- Use simple, one or two-word tags where possible.
- Keep the tags concise and simple, minimizing the number used.
- If any additional tags are necessary beyond those provided, append them to the initial list.
- Return only the list of tags with no additional content.

# Output Format

A list of tags, formatted like: `['tag1', 'tag2', 'tag3']`
"""
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content="""Here is a question that needs to be tagged:\nQuestion\nTitle: {title}\nBody: {body}\nTags: {tags}""".format(title=title, body=body, tags=tags)),
    ]
    return messages