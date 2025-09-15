from utils.ai import AIClient
from pydantic import BaseModel
from typing import List, Dict
import json
from utils.ai import AIClient
from pydantic import BaseModel
from typing import List

class QAItem(BaseModel):
    """Defines the structure for a single question-answer pair."""
    question: str
    answer: str

def generateQuestions(job_description, resume, round_name="Technical Interview"):
    """
    Generates interview questions based on the provided role and skills.
    """

    prompt = f"""
    You are an interview assistant. 
    Based on the following data, generate 5 interview questions 
    and return them in **strict JSON array** format.

    data: job description: {job_description}
    data: resume: {resume}
    data: round name: {round_name}

    Example JSON:
    [
        {{"question": "What is OOP?", "answer": "OOP stands for Object-Oriented Programming..."}},
        {{"question": "Explain SOLID principles.", "answer": "SOLID is an acronym for..."}},
        {{"question": "How do you manage memory in C++?", "answer": "I manage memory using..."}},
        {{"question": "What is REST API?", "answer": "REST stands for Representational State Transfer..."}},
        {{"question": "How would you optimize a SQL query?", "answer": "Optimizing a SQL query involves..."}}
    ]
    """

    config = {
        "response_mime_type": "application/json",
        "response_schema": {
            "type": "array",
            "items": QAItem.model_json_schema()  # ✅ just array of QAItem
        }
    }

    response = AIClient(prompt, config)
    return response

def generateConfig(questions,resume,jobDescription,round_name):
    return f"""
    You are an AI Interviewer conducting the {round_name}.
    Ask questions from the predefined list one by one, 
    like a real human interviewer. Do not skip or mix them. 
    Wait for the candidate’s response after each question.

    ### Data:
    - Resume: {resume}
    - Job Description: {jobDescription}
    - Round Name: {round_name}

    ### Predefined Question Set:
    {questions}

    ### Rules:
    1. Start with a greeting: "Good <name of candidate from the resume>! Let's begin with the interview."
    2. Ask questions strictly from the predefined list, in order.
    3. Ask only one question at a time.
    4. Do NOT answer on behalf of the candidate.
    5. Keep tone professional and conversational.
    6. If the candidate asks for clarification, provide a brief explanation.
    7. After all questions are asked, conclude with: "Thank you for your time. We will get back to you soon."
    8. Do NOT provide any evaluation or feedback during the interview.
    """
def AIInterviewStimulation(questions,resume,jobDescription,round_name,content):
    prompt=generateConfig(questions,resume,jobDescription,round_name)
    config={
        "response_mime_type": "text/plain",
        "system_instruction": prompt,
    }
    response = AIClient(content, config)
    return response.text
def generateSummary(resume, questionAnswer, userAnswer, job_description, round_name) :
    return f"""
    You are an AI interview assistant. 
    Your role is to evaluate candidate answers strictly and fairly.

    ### Input Data:
    - **Round Name**: {round_name}
    - **Job Description**: {job_description}
    - **Resume Data**: {resume}
    - **Interview Question And Model Answers**: {questionAnswer}
    - **User Answer **: {userAnswer}

    ### Instructions:
    1. Analyze the candidate's resume and match it with the job description.
    2. Compare the candidate’s answer to the provided **model answer**.
    3. Highlight **strengths** and **weaknesses** in the candidate’s response.
    4. Give a **score from 1 to 10** with justification.
    5. Output the result strictly in JSON format with the following schema:

    {{
        "roundName": "{round_name}",
        "jobTitle": "<job title extracted from job description>",
        "evaluation": {{
            "strengths": ["..."],
            "weaknesses": ["..."],
            "score": 0,
            "justification": "..."
        }}
    }}
    """
def generateFeedback(resume, questionAnswer, userAnswer, job_description, round_name) :
    prompt=generateSummary(resume, questionAnswer, userAnswer, job_description, round_name)
    config={
        "response_mime_type": "application/json",
        "response_schema": {
            "type": "object",
            "properties": {
                "roundName": {"type": "string"},
                "jobTitle": {"type": "string"},
                "evaluation": {
                    "type": "object",
                    "properties": {
                        "strengths": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "weaknesses": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "score": {"type": "integer", "minimum": 1, "maximum": 10},
                        "justification": {"type": "string"}
                    },
                    "required": ["strengths", "weaknesses", "score", "justification"]
                }
            },
            
        }
    }
    response = AIClient(prompt, config)
    return json.loads(response)["parsed"]

def convertTextToJSON(text):
    prompt=f"""
    Convert the following text to a JSON object. 
    Ensure the JSON is properly formatted.

    Text:
    {text}
    Do not add any extra information or explanation.
    Example JSON format:
    {{
        "key1": "value1",
        "key2": "value2",
        ...
    }}
    """
    config={
        "response_mime_type": "application/json",
    }
    response = AIClient(prompt, config)
    return response

