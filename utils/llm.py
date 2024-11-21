# Importing Dependencies
import os
import logging
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_llm():
    model = OllamaLLM(model="gemma:2b")
    logger.info("Model loaded successfully!")
    return model