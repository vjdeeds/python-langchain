from dotenv import load_dotenv
from app.config import llm
from langchain_core.messages import HumanMessage  # ✅ updated import

load_dotenv()


def ask_langchain(question: str):
    response = llm.invoke([HumanMessage(content=question)])
    print(type(response))
    return {"answer": response.content}


# ChatOpenAI imports are commented out to avoid confusion.
# Uncomment and use the appropriate one based on your setup.
# llm = ChatOpenAI(
#     model="gpt-3.5-turbo",  # ✅ use 'model' instead of 'model_name'
#     temperature=0.7,–
#     api_key=os.getenv("OPENAI_API_KEY")
# )

# ✅ use invoke() instead of __call__
