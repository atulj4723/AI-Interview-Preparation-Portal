from utils.db import db
def addFeedback(interviewId, feedback):
    result = db.feedbacks.insert_one({
        "feedback": feedback,
        "interviewId": interviewId
    })
    return {
        "_id": str(result.inserted_id),
        "feedback": feedback,
        "interviewId": interviewId
    }

def getFeedBack(interviewId):
    res = db.feedbacks.find_one({"interviewId": interviewId})
    if not res:
        return None
    res["_id"] = str(res["_id"])
    return res
