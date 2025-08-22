from utils.db import db
from datetime import datetime
import bcrypt
def createUser(name,email,password,phone):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashpass = bcrypt.hashpw(password_bytes, salt)
    created_at=datetime.now()
    res=db.users.insert_one({"name":name,"email":email,"password":hashpass,"phone":phone,"created_at":created_at})
    return res.inserted_id
def FindUserByEmail(email):
    res=db.users.find_one({"email":email})
    if res:
        return res
def Login(email,password):
    res=FindUserByEmail(email)
    if res:
        login_password_bytes = password.encode('utf-8')
        password=res['password']
        is_match = bcrypt.checkpw(login_password_bytes, password)
        if is_match:
            return res
