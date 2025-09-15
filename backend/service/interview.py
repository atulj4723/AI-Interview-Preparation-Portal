from utils.db import db
from bson import ObjectId
def createInterview(user_id,title,round_name,description,question_answer):
    interview={
        "userID":user_id,
        "title":title,
        "round_name":round_name,
        "description":description,
        "question_answer":question_answer,
        "status": "Scheduled"
        }
    res=db.interviews.insert_one(interview)
    interview["_id"] = res.inserted_id
    return interview
def getInterview(user_id):
    interview=db.interviews.find({"userID":user_id})
    return interview
def getSpecificInterview(interview_id):
    id=ObjectId(interview_id)
    interview=db.interviews.find_one({"_id":id})
    return interview
