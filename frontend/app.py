import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agent.langchain_agent import agent
from dotenv import load_dotenv
import os

load_dotenv()


st.title("🧠 A Google Calender AI agent") 

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.write(f"**You:** {msg['user']}")
    st.write(f"**Bot:** {msg['bot']}")

user_input = st.chat_input("Type your request...")

if user_input:
    try:
        response = agent.run({"input": ...}) 
    except Exception as e:
        response = f"❌ Error: {str(e)}"
    
    st.session_state.messages.append({"user": user_input, "bot": response})
    st.rerun()
