from flask import Blueprint,request,jsonify
from pydantic import ValidationError
from models.user import User
from service.user import createUser,FindUserByEmail,Login
auth_bp = Blueprint('auth', __name__)
@auth_bp.route("/signup",methods=["POST"])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({"error":"No data provided"}), 400
    
    try:
        userData=User(**data)
    except ValidationError as e:
        error_details = []
        for error in e.errors():
            error_details.append({
                "field": ".".join(str(loc) for loc in error["loc"]), # e.g., "phone"
                "message": error["msg"] # The error message string
            })
        return  jsonify({"error": "Invalid data provided", "details": error_details}), 422
    
    check=FindUserByEmail(data['email'])
    if check:
        return jsonify({"error":"User Already exist"}),402
    
    try:
        createUser(data['name'],data['email'],data['password'],data['phone'])
    except Exception as e:
        return jsonify({"error":"Could not create user in database","details":str(e)}),500
    
    return jsonify({ "message": "User created successfully!"}), 201

@auth_bp.route("/signin",methods=["POST"])
def signin():
    data = request.get_json()
    if not data:
        return jsonify({"error":"No data provided"}), 400
    if not Login(data['email'],data['password']):
        return jsonify({"error":"Wrong Credentials"}),400

    return "signin"