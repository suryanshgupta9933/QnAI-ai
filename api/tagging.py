# Importing Dependencies
import logging
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status

from core.tagging import generate_tags

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create Tagging Model
class CreateTags(BaseModel):
    title: str
    body: str
    tags: list

# Generate tags
@router.post("/generate_tags", status_code=status.HTTP_201_CREATED)
def generate_tags_endpoint(tags: CreateTags):
    """
    Generate tags for a question using a language model.
    """
    try:
        generated_tags = generate_tags(tags.title, tags.body, tags.tags)
        return {
            "tags": generated_tags
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate tags: {e}")