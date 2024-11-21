# Importing Dependencies
import os
import logging

from utils.llm import load_llm
from utils.prompts import tagging_prompt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_tags(title: str, body: str, tags: list):
    """
    Generate tags for a given question using a language model.
    """
    model = load_llm()
    prompt = tagging_prompt(title, body, tags)
    chain = prompt | model
    tags = chain.invoke(
        {
            "title": title,
            "body": body,
            "tags": tags
        }
    )
    logger.info(f"Generated tags: {tags} for question: {title}")
    return tags
    