import logging
import os
from typing import List
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from pinecone import Pinecone
from config import Config

logger = logging.getLogger(__name__)

class VectorStore:
    
    def __init__(self, collection_name: str = "website_content"):
        self.index_name = Config.PINECONE_INDEX_NAME
        if not Config.PINECONE_API_KEY:
            raise ValueError("Pinecone API Key is missing.")
    
    def _reset_collection(self):
        try:
            logger.info("Resetting Pinecone index...")
            pc = Pinecone(api_key=Config.PINECONE_API_KEY)
            index = pc.Index(self.index_name)
            index.delete(delete_all=True)
            logger.info(f"Cleared Pinecone index '{self.index_name}'.")
        except Exception as e:
            if "NOT_FOUND" in str(e) or "404" in str(e):
                logger.warning(f"Index '{self.index_name}' does not exist yet. Skipping reset.")
            else:
                logger.error(f"Failed to reset Pinecone index: {e}")
                raise RuntimeError("Could not reset Pinecone index.")

    def create_collection(self, documents: List[Document], embedding_function):
        if not documents:
            logger.warning("No documents provided to create collection.")
            return None
            
        logger.info(f"Creating vector store (Pinecone) with {len(documents)} documents.")
        
        self._reset_collection()
        
        vectorstore = PineconeVectorStore.from_documents(
            documents=documents,
            embedding=embedding_function,
            index_name=self.index_name,
            pinecone_api_key=Config.PINECONE_API_KEY
        )
        
        logger.info("Vector store created and persisted.")
        return vectorstore

    def as_retriever(self, vectorstore):
        return vectorstore.as_retriever(search_kwargs={"k": Config.RETRIEVAL_TOP_K})
