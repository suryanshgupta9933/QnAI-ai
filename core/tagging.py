# Importing Dependencies
import os
import logging
from ast import literal_eval

from utils.llm import load_llm
from utils.prompts import tagging_prompt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_tags(title: str, body: str, tags: list):
    """
    Generate tags for a given question using a language model.
    """
    model = load_llm("llama3.2:3b")
    query = tagging_prompt(title, body, tags)
    tags = model.invoke(query)
    tags = literal_eval(tags)
    for i,tag in enumerate(tags):
        tags[i] = tag.lower().strip()
    logger.info(f"Generated tags: {tags} for question: {title}")
    return tags