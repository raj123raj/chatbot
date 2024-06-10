## loading all the environment variables
from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai
import numpy as np
import pandas as pd

st.markdown("# Simple Chat Bot page 🎈")
st.sidebar.markdown("# Chat Bot page 🎈")

GOOGLE_API_KEY = "**************" #Replace your api_key here
genai.configure(api_key=GOOGLE_API_KEY)

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

#st.set_page_config(page_title="Q&A Demo")

st.header("Chat Bot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [19.0760, 72.8777],
    columns=['lat', 'lon'])

#st.map(map_data)        
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")