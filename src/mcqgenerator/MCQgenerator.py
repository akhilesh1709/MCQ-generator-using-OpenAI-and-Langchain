import os
import json
import traceback
import pandas as pd 
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging
import streamlit as st

# Importing necessary packages from langchain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
openai_api_key = st.secrets.get("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OpenAI API key is not set. Please check your .env file.")

# Initialize the language model
llm = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo", temperature=0.7)

# Define the quiz generation template
quiz_generation_template = """
Text: {text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to ensure they conform to the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
Ensure to make {number} MCQs.

### RESPONSE_JSON
{response_json}
"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=quiz_generation_template
)

quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

# Define the quiz evaluation template
quiz_evaluation_template = """
You are an expert English grammarian and writer. Given a Multiple Choice Quiz for {subject} students,\
you need to evaluate the complexity of the questions and provide a complete analysis of the quiz. Use a maximum of 50 words for the complexity analysis. 
If the quiz does not match the cognitive and analytical abilities of the students,\
update the quiz questions that need to be changed and adjust the tone so that it perfectly fits the students' abilities.

Quiz_MCQs:
{quiz}

Please review the quiz:
"""

quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=quiz_evaluation_template
)

review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

# This is an Overall Chain where we run the two chains in Sequence
generate_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain], 
    input_variables=["text", "number", "subject", "tone", "response_json"],
    output_variables=["quiz", "review"], 
    verbose=True
)
