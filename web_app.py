import streamlit as st
import google.generativeai as genai

# Set the title for your web app
st.set_page_config(page_title="My Gemini Chatbot", page_icon="🤖")
st.title("🤖 My First Gemini Web App")

# --- Authentication ---
# In a real-world app, you'd use Streamlit's secrets management.
# For this tutorial, we'll rely on the environment variable you've already set.
try:
    # This automatically uses the GOOGLE_API_KEY from your environment
    genai.configure()
except Exception as e:
    # If the key is not found, show an error and stop the app
    st.error("Your Google API Key is not set! Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

# --- Model and Chat Initialization ---
# This ensures that the model and chat history are saved across user interactions
if "model" not in st.session_state:
    st.session_state.model = genai.GenerativeModel('gemini-1.5-flash')
if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.model.start_chat(history=[])

# --- Display existing chat messages ---
for message in st.session_state.chat.history:
    # Use "assistant" for the model's role for a nice icon
    role = "assistant" if message.role == 'model' else message.role
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# --- Handle user input ---
if prompt := st.chat_input("What would you like to ask?"):
    # Display the user's message in the chat interface
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send the user's message to Gemini and get the response
    response = st.session_state.chat.send_message(prompt)

    # Display the bot's response
    with st.chat_message("assistant"):
        st.markdown(response.text)