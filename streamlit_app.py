# streamlit_app.py
import streamlit as st
from chatbot import chatbot_response

st.set_page_config(page_title="Customer Support Chatbot", page_icon="🤖")

st.title("🤖 AI Customer Support Chatbot")
st.markdown("Ask your question and get instant responses!")

# Chat UI
user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    response = chatbot_response(user_input)
    st.text_area("Bot:", value=response, height=100, max_chars=None)
