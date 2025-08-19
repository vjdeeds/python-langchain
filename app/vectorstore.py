from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from app.docLoader import load_pdf
from app.config import embeddings, CHROMA_PATH

import os


def load_vector_store():
    if not os.path.exists(CHROMA_PATH):
        # Load the PDF document
        document_into_chunks = load_pdf(
            "C:/Users/Dell/OneDrive/Desktop/Invoice4930864.pdf"
        )

        # Create a vector store using Chroma
        vector_store = Chroma.from_documents(document_into_chunks, embeddings)

        return vector_store
    else:
        # Load the existing vector store from disk
        return Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=OllamaEmbeddings(model="nomic-embed-text"),
        )
