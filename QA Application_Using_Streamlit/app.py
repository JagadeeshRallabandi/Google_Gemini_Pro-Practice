from dotenv import load_dotenv
load_dotenv()## Loading all the enviroment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
##function to load Gemini Pro Model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_response(question):
    response=model.generate_content(question)
    return response.text
##initialize streamlit
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

input=st.text_input("Input:",key="input")
submit=st.button("Ask the Question")

if submit:
    response=get_response(input)
    st.subheader("The Response is")
    st.write(response)
