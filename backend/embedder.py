import logging
from langchain_openai import OpenAIEmbeddings
from config import Config

logger = logging.getLogger(__name__)

class Embedder:
    
    def __init__(self):
        self.provider = Config.EMBEDDING_PROVIDER
        self.model = Config.EMBEDDING_MODEL
        
    def get_embedding_function(self):
        logger.info(f"Initializing {self.provider} embeddings with model: {self.model}")
        
        if self.provider == "openai":
            if not Config.OPENAI_API_KEY:
                raise ValueError("OpenAI API key is not configured.")
            
            output = OpenAIEmbeddings(
                model=self.model,
                openai_api_key=Config.OPENAI_API_KEY
            )
            logger.info(f"OpenAI embeddings initialized successfully (model: {self.model}, dimensions: 1536)")
        else:
            raise ValueError(f"Unsupported embedding provider: {self.provider}")
        
        return output
