from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama
from app.vectorstore import load_vector_store
from app.config import llm  # Importing the llm from config
from app.custom_callback import FastAPIStreamingCallbackHandler
from fastapi.responses import StreamingResponse

callback = FastAPIStreamingCallbackHandler()
retriever = load_vector_store().as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=llm, retriever=retriever, return_source_documents=True
)


def answer_langchain(question: str):
    response = qa_chain.invoke(question)
    return {"answer": response["result"], "sources": response["source_documents"]}


async def answer_langchain_with_stream(question: str):
    # llm.streaming = True
    llm.callbacks = [callback]
    # qa_chain.invoke(question)
    await qa_chain.ainvoke({"query": question})

    async def event_stream():
        async for token in callback.get_stream():
            yield f"data: {token}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
