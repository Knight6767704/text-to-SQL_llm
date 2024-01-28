from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

prompt = [
    """
      You are an expert in converting English questions to SQL query!
      The SQL database has the name STUDENT1 and has the following columns- NAME,
      CLASS, SECTION, and MARKS \n\nFor example,\nExample 1-How many entries of records are 
      present?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT1;
      \nExample 2-Tell me all the students studying in Data Science class?, the SQL
      command will be something like this SELECT * FROM STUDENT1
      WHERE CLASS="Data Science";
      Also, the SQL code should not have ``` in the beginning or end, and SQL word in the output.
    """
]

st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    
    # Assuming response contains a valid SQL query
    data = read_sql_query(response, "student1.db")
    
    st.subheader("The response is")
    for row in data:
        st.write(row)
