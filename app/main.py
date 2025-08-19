from fastapi import FastAPI
from app.chatbot import ask_langchain
from app.rag_engine import answer_langchain, answer_langchain_with_stream
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "FastAPI + LangChain is running!"}


@app.get("/ask_chatbot")
def ask_chatbot(q: str):
    return ask_langchain(q)


@app.get("/ask_rag")
def ask(q: str):
    return answer_langchain(q)


@app.get("/stream")
async def stream(q: str):
    return await answer_langchain_with_stream(q)
