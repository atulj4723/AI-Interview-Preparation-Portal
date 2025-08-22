from flask import Blueprint,request,jsonify
from pydantic import ValidationError
from models.user import User
from service.user import createUser,FindUserByEmail,Login
auth_bp = Blueprint('auth', __name__)
@auth_bp.route("/signup",methods=["POST"])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({
            "success":False,
            "error":"No data provided"
            }), 400
    
    try:
        userData=User(**data)
    except ValidationError as e:
        error = e.errors()[0]["msg"]
        return  jsonify({
            "success":False,
            "error": error
            }), 422
    
    check=FindUserByEmail(data['email'])
    if check:
        return jsonify({
            "success":False,
            "error":"User Already exist"
            }),403
    
    try:
        user= createUser(data['name'],data['email'],data['password'],data['phone'])
        if "_id" in user:
            user["_id"] = str(user["_id"])
        if "password" in user:
            del user["password"]
    except Exception as e:
        return jsonify({
            "success":False,
            "error":"Could not create user in database",
            "details":str(e)
            }),500
    
    return jsonify({
        "success":True, 
        "message": "User created successfully!",
        "data":user
        }), 201

@auth_bp.route("/signin",methods=["POST"])
def signin():
    data = request.get_json()
    if not data:
        return jsonify({
            "success":False,
            "error":"No data provided"
            }), 400
    user=Login(data['identifier'],data['password'])
    if not user:
        return jsonify({
            "success":False,
            "error":"Wrong Credentials"
            }),403
    if "_id" in user:
        user["_id"] = str(user["_id"])
    if "password" in user:
        del user["password"]

    return jsonify({ 
        "success":True,
        "message": "User signed in successfully!",
        "data":user
        }), 200