from langchain_ollama import ChatOllama, OllamaEmbeddings

llm = ChatOllama(model="phi3", temperature=0.3)
# llm = Ollama(model="tinyllama")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

CHROMA_PATH = "chroma_db"
