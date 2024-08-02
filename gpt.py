import streamlit as st
import google.generativeai as genai


def generate_response(prompt):
    genai.configure(api_key="AIzaSyBCjsa0d1qUbfgvIRJQZc4VM2FPEh4leK0")

    # Create the model
    generation_config = {"temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
    history=[
    ]

    )
    response = chat_session.send_message(prompt)
    yield response.text


data = st.chat_input("enter prompt")

    
if "chats" not in st.session_state:
    st.session_state["chats"] = ["How can I help you"]

for i, chat in enumerate(st.session_state["chats"]):
    if i % 2 == 0:
        st.chat_message("assistant").write(chat)
    else:
        st.chat_message("user").write(chat)
    
if data:
    st.session_state["chats"].append(data)
    st.chat_message("user").write(data)
    response = generate_response(data)
    st.session_state["chats"].append(response)
    st.chat_message("assistant").write_stream(response)
       
