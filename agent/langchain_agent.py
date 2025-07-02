import os
import requests
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_community.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()


from pydantic import BaseModel

class CalendarInput(BaseModel):
    summary: str
    start: str
    end: str

# 🧠 Define the function used as tool
def book_tool(summary: str, start: str, end: str):
    data = {"summary": summary, "start": start, "end": end}
    res = requests.post("http://localhost:8000/book", json=data)
    return res.json().get("message", "Failed to book event.")

# 🔧 Tool list
from langchain.agents import Tool

tools = [
    Tool(
        name="BookAppointment",
        func=book_tool,
        description=(
            "Use this tool to book a Google Calendar meeting. "
            "Provide input in the format: "
            '{"summary": "Meeting title", "start": "YYYY-MM-DDTHH:MM:SS", "end": "YYYY-MM-DDTHH:MM:SS"}'
        )
    )
]


# 💡 Define the LLM
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0,
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENAI_API_KEY")  
)

agent = initialize_agent(
    tools,
    llm,
    agent_type="chat-conversational",
    handle_parsing_errors=True  
)
