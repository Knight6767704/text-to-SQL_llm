# Streamlit Gemini SQL App

## Overview
This Streamlit app demonstrates the integration of Google's Gemini language model for generating SQL queries based on natural language questions. The app connects to a SQLite database (`student1.db`) with a table named `STUDENT1` containing information about students.

## Requirements
- Python 3.8+
- [Streamlit](https://www.streamlit.io/)
- [Google GenerativeAI](https://pypi.org/project/google-generativeai/)
- [SQLite](https://www.sqlite.org/)

## Setup
1. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
    ```
2. Run the database
   ```bash
   python sql.py
    ```
3. Create a .env file and keep GOOGLE_API_KEY="your_api"
4. Run the application using
  ```bash
   streamlit run app.py
  ```
This project is present at https://huggingface.co/spaces/knight6767704/sql_text_extractor
