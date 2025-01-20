import streamlit as st
from utils.llm_handler import generate_response

# Page configuration
st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🤖")

# Title and description
st.title("TalentScout Hiring Assistant")
st.write("Welcome! I'm here to help you with the initial screening process.")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate chatbot response
    chatbot_response = generate_response(st.session_state.messages)

    # Add chatbot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": chatbot_response})
    with st.chat_message("assistant"):
        st.markdown(chatbot_response)