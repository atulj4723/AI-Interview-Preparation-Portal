from utils.db import db
def getProfile(user_id):
    user=db.profiles.find_one({"userID":user_id})
    return user
def createProfile(user_id, resume):
    profile={
        "userID":user_id,
        "resume":resume
        }
    res=db.profiles.insert_one(profile)
    profile["_id"] = res.inserted_id
    return profile
def updateProfile(user_id, resume):
    profile={
        "userID":user_id,
        "resume":resume
        }
    res=db.profiles.update_one({"userID":user_id},{"$set":profile},upsert=True)
    profile["_id"] = res.upserted_id
    return profile