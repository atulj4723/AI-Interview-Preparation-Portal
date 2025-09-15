from utils.db import db
from datetime import datetime
import bcrypt
from bson import ObjectId
def createUser(name,email,password,phone):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashpass = bcrypt.hashpw(password_bytes, salt).decode('utf-8')
    created_at=datetime.now()
    user={
        "name":name,
        "email":email,
        "password":hashpass,
        "phone":phone,
        "created_at":created_at
        }
    res=db.users.insert_one(user)
    user["_id"] = res.inserted_id
    return user

def FindUserByEmail(email):
    res=db.users.find_one({"email":email})
    return res

def Login(identifier,password):
    res=db.users.find_one({"$or":[{"email":identifier},{"phone":identifier}]})
    if not res:
        return None
    login_password_bytes = password.encode('utf-8')
    stored_password=res['password'].encode('utf-8')
    is_match = bcrypt.checkpw(login_password_bytes, stored_password)
    if is_match:
        return res
    return None
def FindUserById(user_id):
    try:
        user_obj_id = ObjectId(user_id)
        res = db.users.find_one({"_id": user_obj_id})
        res['_id']=str(res['_id'])
        print(res)
        return res
    except Exception as e:
        print("Error in FindUserById:", e)
        return None
