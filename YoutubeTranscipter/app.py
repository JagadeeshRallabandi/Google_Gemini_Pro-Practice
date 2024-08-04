import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
import re

# Load environment variables
load_dotenv()

# Configure the generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define prompt for the AI
prompt = """You are a YouTube Video Summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. The transcript text will be appended here:
"""

# Function to extract video ID from YouTube URL
def extract_video_id(youtube_url):
    video_id = None
    # Match the typical YouTube URL patterns
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, youtube_url)
        if match:
            video_id = match.group(1)
            break
    return video_id

# Function to fetch available transcript languages
def fetch_available_languages(video_id):
    try:
        transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        languages = {t.language_code: t.language for t in transcripts}
        return languages
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

# Function to extract transcript details
def extract_transcript_details(video_id, language='en'):
    try:
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        transcript = " ".join([item["text"] for item in transcript_text])
        return transcript
    except NoTranscriptFound:
        st.error(f"No transcript found for language: {language}")
        return None
    except TranscriptsDisabled:
        st.error(f"Transcripts are disabled for this video.")
        return None
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

# Function to generate summary using Gemini model
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit UI
st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

video_id = None
languages = None
if youtube_link:
    video_id = extract_video_id(youtube_link)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
        with st.spinner("Fetching available languages..."):
            languages = fetch_available_languages(video_id)
        if languages:
            language = st.selectbox("Select Transcript Language:", list(languages.values()))
        else:
            st.error("No available languages for transcripts.")
    else:
        st.error("Invalid YouTube URL. Please enter a correct YouTube video link.")

if st.button("Get Detailed Notes", key="generate_notes"):
    if video_id and languages:
        selected_language_code = list(languages.keys())[list(languages.values()).index(language)]
        with st.spinner("Extracting transcript..."):
            transcript_text = extract_transcript_details(video_id, selected_language_code)
        
        if transcript_text:
            with st.spinner("Generating summary..."):
                summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)
        else:
            st.error("Failed to extract transcript. Please check the video link and try again.")
    else:
        st.error("Please enter a valid YouTube link and select a language.")
