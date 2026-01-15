import logging
import requests
from langchain_core.embeddings import Embeddings
from config import Config
from typing import List

logger = logging.getLogger(__name__)

class JinaEmbeddings(Embeddings):
    """Custom Jina embeddings implementation using Jina AI API"""
    
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
        self.api_url = "https://api.jina.ai/v1/embeddings"
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of documents"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "input": texts
        }
        
        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        
        return [item["embedding"] for item in result["data"]]
    
    def embed_query(self, text: str) -> List[float]:
        """Embed a single query"""
        return self.embed_documents([text])[0]

class Embedder:
    
    def __init__(self):
        self.provider = Config.EMBEDDING_PROVIDER
        self.model = Config.EMBEDDING_MODEL
        
    def get_embedding_function(self):
        logger.info(f"Initializing {self.provider} embeddings with model: {self.model}")
        
        if self.provider == "jina":
            if not Config.JINA_API_KEY:
                raise ValueError("Jina API key is not configured.")
            
            output = JinaEmbeddings(
                api_key=Config.JINA_API_KEY,
                model=self.model
            )
            logger.info(f"Jina embeddings initialized successfully (model: {self.model}, dimensions: 768)")
        else:
            raise ValueError(f"Unsupported embedding provider: {self.provider}")
        
        return output
