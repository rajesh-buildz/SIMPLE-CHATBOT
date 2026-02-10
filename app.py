import streamlit as st
import google.generativeai as genai

# -----------------------
# Configure Gemini API
# -----------------------
genai.configure(api_key="AIzaSyBhhCHWLl6toghKl1mhx4lIi6f8shMGWgA")

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------
# Streamlit UI
# -----------------------
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini Chatbot")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("hi")

if prompt:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini response
    response = st.session_state.chat.send_message(prompt)

    # Show assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": response.text}
    )
    with st.chat_message("assistant"):
        st.markdown(response.text)