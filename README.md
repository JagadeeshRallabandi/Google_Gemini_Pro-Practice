# Google Gemini Gen AI Projects

Welcome to the Google Gemini Gen AI Projects repository! This repository contains a collection of projects utilizing the Google Gemini API for various AI-driven applications. Each project is designed to run independently with Streamlit for a user-friendly interface.

## Projects

1. **ATS Tracker**
2. **Calorie Tracker with Image**
3. **Multiple Documents ChatBot**
4. **Invoice Multilingual**
5. **QA Application**
6. **Connecting with SQL**
7. **YouTube Video Transcriptor**

## Getting Started

### Prerequisites

- Python 3.9 or higher
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

### Setting Up Your Environment

1. **Clone the repository**

    ```bash
    git clone https://github.com/JagadeeshRallabandi/Google_Gemini_Pro-Practice.git
    cd Google_Gemini_Pro-Practice
    ```

2. **Create a virtual environment**

    ```bash
    virtualenv venv
    ```

3. **Activate the virtual environment**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install project requirements**

    ```bash
    pip install -r requirements.txt
    ```

### Setting Up API Keys

1. **Create a `.env` file in the root directory of your project**

    ```bash
    touch .env
    ```

2. **Add your API keys to the `.env` file**

    ```plaintext
    GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key_here
    ```

   You can obtain the Google Gemini API key from (https://aistudio.google.com/app/apikey).

### Running the Projects

1. **Navigate to the project directory**

    ```bash
    cd project_name
    ```

2. **Run the application with Streamlit**

    ```bash
    streamlit run app.py
    ```

## Project Descriptions

### ATS Tracker
An AI-powered applicant tracking system to manage and track job applications.

### Calorie Tracker with Image
A calorie tracker that uses image recognition to estimate calorie intake from food images.

### Multiple Documents ChatBot
A chatbot that can interact with and retrieve information from multiple documents.

### Invoice Multilingual
An invoice processing tool that supports multiple languages.

### QA Application
A question and answer application powered by AI.

### Connecting with SQL
A project demonstrating how to connect and interact with SQL databases.

### YouTube Video Transcriptor
A tool that transcribes YouTube videos given a link.


## Acknowledgments

- [Google Gemini](https://cloud.google.com/gemini)
