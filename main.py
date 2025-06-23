import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="📘 Homework Solver AI", layout="centered")

st.title("📘 Homework Solver AI")
st.caption("Ask any question from school and get step-by-step answers.")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Type your homework question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Solving..."):
        response = open
