import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
##function to load Gemini Pro Model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")
def get_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

input=st.text_input("Input:",key="input")
upload_file= st.file_uploader("Choose an Image...",type=["jpg","jpeg","png"])
image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption = "Upload Image",use_column_width=True)
submit=st.button("Tell me about the Image")

if submit:
    response=get_response(input,image)
    st.subheader("The Response is")
    st.write(response)
