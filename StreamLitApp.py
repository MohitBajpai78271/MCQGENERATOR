import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from src.mcqgenerator.logger import logger
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQGENERATOR import generate_evaluate_chain

with open('/Users/mac/Desktop/MCQGEN/Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

st.title('MCQ Creator Application with Langchain 🚀')

with st.form("user_inputs"):
    uploaded_file = st.file_uploader("Upload a PDF or File")
    mcq_count = st.number_input("No of mcq's", min_value=3, max_value=50)
    subject = st.text_input("Insert Subject", max_chars=20)
    tone = st.text_input("Complexity level of Questions", max_chars=20, placeholder="Simple")
    button = st.form_submit_button('Create MCQs')

if button and uploaded_file is not None and mcq_count and subject and tone:
    with st.spinner("Loading..."):
        try:
            text = read_file(uploaded_file)
            with get_openai_callback() as cb:
                response = generate_evaluate_chain({
                    "text": text,
                    "number": mcq_count,
                    "subject": subject,
                    "tone": tone,
                    "response_json": json.dumps(RESPONSE_JSON)
                })
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            st.error("Error occurred during MCQ generation.")
        else:
            st.write(f"Total Tokens: {cb.total_tokens}")
            st.write(f"Prompt Tokens: {cb.prompt_tokens}")
            st.write(f"Completion Tokens: {cb.completion_tokens}")
            st.write(f"Total Cost: {cb.total_cost}")
            if isinstance(response, dict):
                quiz = response.get("quiz", None)
            else:
                quiz = None
            if quiz is not None:
                table_data = get_table_data(quiz)
                if table_data is not None:
                    df = pd.DataFrame(table_data)
                    df.index = df.index + 1
                    st.table(df)
                    st.text_area(label="Review", value=response.get("review", ""))
                else:
                    st.error("Error in generating table data.")
            else:
                st.error("Quiz data not found in response.")
else:
    st.info("Please fill in all fields and upload a file to generate MCQs.")
