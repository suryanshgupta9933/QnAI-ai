# Importing Dependencies
import os
import logging
from langchain_openai import ChatOpenAI
from langchain_ollama.llms import OllamaLLM

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_llm(model_name: str):
    try:
        if model_name == "gemma:2b":
            model = OllamaLLM(model="gemma:2b")
        if model_name == "qwen2.5:3b":
            model = OllamaLLM(model="qwen2.5:3b")
        if model_name == "llama3.2:3b":
            model = OllamaLLM(model="llama3.2:3b")
        logger.info("Model loaded successfully!")
        return model
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        return None