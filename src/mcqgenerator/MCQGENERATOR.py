import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
from src.mcqgenerator.logger import logger

# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
# 
# import PyPDF2

from dotenv import load_dotenv
load_dotenv()
apiKey = "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"

apiKey = os.getenv("OPENAI_API_KEY") 
llm = ChatOpenAI(openai_api_key=apiKey,model_name="gpt-3.5-turbo",temperature=0.5)




TEMPLATE="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
Ensure to make {number} MCQS
### RESPONSE_JSON
{response_json}
"""

quiz_prompt = PromptTemplate(
    input_variables=["text","number","subject","tone","response_json"],
    template = TEMPLATE
)

quiz_chain = LLMChain(llm=llm,prompt=quiz_prompt,output_key="quiz",verbose=True)

TEMPLATE2 = """
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis if the quiz is not at per with the cognitive and analytical abilities of the students, \
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}
Check from an expert English Writer of the above quiz:" \
"""
quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject","quiz"],
    template=TEMPLATE2
    )
review_chain = LLMChain(llm=llm,prompt=quiz_evaluation_prompt,output_key="review",verbose=True)

generate_evaluate_chain = SequentialChain(chains=[quiz_chain,review_chain],input_variables=["text","number","subject","tone","response_json"],output_variables=["quiz","review"],verbose=True)