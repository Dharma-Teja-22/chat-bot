import streamlit as st
import google.generativeai as genai
import os
import time

def generate_response(prompt):
    genai.configure(api_key=os.environ["api_key"])

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[]
    )
    
    response = chat_session.send_message(prompt)
    
    for word in response.text.split():
        yield word + " "
        time.sleep(0.05)  

def main():
    # st.title("GPT using Generative AI")
    st.markdown("<h1 style='text-align: center; color: white;'>GPT using Generative AI</h1>", unsafe_allow_html=True)


    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        login = st.button("Login")

        if login:
            if username == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.success("Logged in successfully!")
            else:
                st.error("Incorrect username or password")
    else:
        if "chats" not in st.session_state:
            st.session_state["chats"] = ["How can I help you"]

        # Display previous chats
        for i, chat in enumerate(st.session_state["chats"]):
            if i % 2 == 0:
                st.chat_message("assistant").write(chat)
            else:
                st.chat_message("user").write(chat)

        # Get new user input
        data = st.chat_input("Enter prompt")

        if data:
            st.session_state["chats"].append(data)
            st.chat_message("user").write(data)
            
            response_placeholder = st.empty()
            response_text = ""
            
            for word in generate_response(data):
                response_text += word
                response_placeholder.chat_message("assistant").write(response_text)
            
            st.session_state["chats"].append(response_text)

if __name__ == "__main__":
    main()
