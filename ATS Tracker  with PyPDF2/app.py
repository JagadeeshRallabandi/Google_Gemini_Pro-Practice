import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import json
from dotenv import load_dotenv

load_dotenv()

# Configure the Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text

input_prompt_template = """
Hey Act Like a skilled or very experienced ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst,
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
the best assistance for improving the resume. Assign the percentage Matching based 
on the JD and the missing keywords with high accuracy.
resume: {resume_text}
description: {jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

st.title("Smart ATS")
st.text("Improve Your Resume with ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        input_prompt = input_prompt_template.format(resume_text=resume_text, jd=jd)
        response = get_gemini_response(input_prompt)
        
        try:
            # Parse the response JSON
            response_json = json.loads(response)
            st.subheader("Response")
            
            # Display the JD match percentage
            st.markdown(f"**JD Match Percentage:** {response_json.get('JD Match', 'N/A')}")
            
            # Display the missing keywords
            st.markdown("**Missing Keywords:**")
            missing_keywords = response_json.get('MissingKeywords', [])
            if missing_keywords:
                st.markdown("- " + "\n- ".join(missing_keywords))
            else:
                st.markdown("None")
            
            # Display the profile summary
            st.markdown("**Profile Summary:**")
            st.markdown(response_json.get('Profile Summary', 'N/A'))
        except json.JSONDecodeError:
            st.error("Failed to parse the response. Please try again.")
    else:
        st.write("Please upload the resume")
