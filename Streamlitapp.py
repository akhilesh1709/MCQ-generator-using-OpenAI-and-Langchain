import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st  
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQgenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

with open('response.json','r') as file:
    RESPONSE_JSON = json.load(file)

st.title("MCQs creator application with langchain")

with st.form("user_inputs"):
    uploaded_file = st.file_uploader("Upload a PDF or txt file ")

    mcq_count = st.number_input("No. of MCQs",min_value=3, max_value=50)

    subject = st.text_input("Inser subject",max_chars=20)

    tone = st.text_input("Complexity level of questions",max_chars=20, placeholder="Simple")

    button = st.form_submit_button("Create MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text = read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain({
                        "text":text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone":tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
