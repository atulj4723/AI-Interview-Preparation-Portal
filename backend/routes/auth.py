from flask import Blueprint,request,jsonify
from pydantic import ValidationError
from models.user import User
from service.user import createUser,FindUserByEmail,Login
auth_bp = Blueprint('auth', __name__)
@auth_bp.route("/signup",methods=["POST"])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({"message":"No data provided"}), 400
    
    try:
        userData=User(**data)
    except ValidationError as e:
        error = e.errors()[0]["msg"]
        
        return  jsonify({"message": error}), 422
    
    check=FindUserByEmail(data['email'])
    if check:
        return jsonify({"message":"User Already exist"}),402
    
    try:
        user= createUser(data['name'],data['email'],data['password'],data['phone'])
    except Exception as e:
        return jsonify({"message":"Could not create user in database","details":str(e)}),500
    
    return jsonify({ "message": "User created successfully!","data":user}), 201

@auth_bp.route("/signin",methods=["POST"])
def signin():
    data = request.get_json()
    if not data:
        return jsonify({"message":"No data provided"}), 400
    user=Login(data['email'],data['password'])
    if not user:
        return jsonify({"message":"Wrong Credentials"}),400
    return jsonify({ "message": "User created successfully!","data":user}), 201