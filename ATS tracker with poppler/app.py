from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai
import base64

# Configure the Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(input_text, pdf_content[0], prompt)
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit app configuration
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improve my Skills")
submit3 = st.button("What are the Keywords that are Missing")
submit4 = st.button("Percentage Match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""
input_prompt2 = """
You are a Technical Human Resource Manager with expertise in Data Science, Full Stack Web Development, and DEVOPS.
Your role is to scrutinize the resume in light of the job description provided.
Share your insights on the candidate's suitability for the role from an HR perspective.
Additionally, offer advice on enhancing the candidate's skills and identify areas to improve.
"""
input_prompt3 = """
You are a Technical Human Resource Manager with expertise in Data Science, Full Stack Web Development, and DEVOPS.
Your role is to scrutinize the resume in light of the job description provided.
Share your insights on the submitted resume. Tell me what keywords are missing in the resume for the provided job description. 
If it satisfies the job description, respond that the resume is perfect.
"""
input_prompt4 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as a percentage and then keywords missing, and last, final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        try:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_content, input_prompt1)
            st.subheader("The Response is")
            st.write(response)
        except Exception as e:
            st.write(f"Error processing the request: {e}")
    else:
        st.write("Please upload the resume")
elif submit2:
    if uploaded_file is not None:
        try:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_content, input_prompt2)
            st.subheader("The Response is")
            st.write(response)
        except Exception as e:
            st.write(f"Error processing the request: {e}")
    else:
        st.write("Please upload the resume")
elif submit3:
    if uploaded_file is not None:
        try:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_content, input_prompt3)
            st.subheader("The Response is")
            st.write(response)
        except Exception as e:
            st.write(f"Error processing the request: {e}")
    else:
        st.write("Please upload the resume")
elif submit4:
    if uploaded_file is not None:
        try:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_content, input_prompt4)
            st.subheader("The Response is")
            st.write(response)
        except Exception as e:
            st.write(f"Error processing the request: {e}")
    else:
        st.write("Please upload the resume")
