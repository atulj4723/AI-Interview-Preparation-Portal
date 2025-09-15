from utils.db import db
def createConversation(conversations,user_id,interview_id):
    conversation={
        "userID":user_id,
        "interviewID":interview_id,
        "conversations":conversations
        }
    res=db.conversations.insert_one(conversation)
    conversation["_id"] = str(res.inserted_id)
    return conversation
def getConversation(user_id,interview_id):
    conversation=db.conversations.findOne({"userID":user_id,"interviewID":interview_id})
    conversation["_id"]=str(conversation["_id"])
    return conversation

    