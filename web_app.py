import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="My Gemini Chatbot", page_icon="🤖")
st.title("🤖 My First Gemini Web App")

# --- Authentication ---
# Try to get the API key from Streamlit's secrets management
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except (KeyError, FileNotFoundError):
    # If not found in secrets, try to get it from environment variables
    # This allows the app to still run locally
    api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Your Google API Key is not set! Please add it to your Streamlit secrets or set the environment variable.")
    st.stop()

genai.configure(api_key=api_key)

# --- Model and Chat Initialization ---
if "model" not in st.session_state:
    st.session_state.model = genai.GenerativeModel('gemini-1.5-flash')
if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.model.start_chat(history=[])

# --- Display existing chat messages ---
for message in st.session_state.chat.history:
    role = "assistant" if message.role == 'model' else message.role
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# --- Handle user input ---
if prompt := st.chat_input("What would you like to ask?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.chat.send_message(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.text)