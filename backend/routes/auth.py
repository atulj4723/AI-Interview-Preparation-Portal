from flask import Blueprint, request, jsonify, make_response
from pydantic import ValidationError
from models.user import User
from service.user import createUser, FindUserByEmail, Login, FindUserById
import jwt, datetime, os

auth_bp = Blueprint('auth', __name__)

SECRET_KEY = os.getenv("JWT_SECRET")  # keep secret in env

def create_jwt(user_id):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)  # 7-day expiry
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_jwt(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# ---------------------- SIGNUP ---------------------- #
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "error": "No data provided"}), 400
    
    try:
        userData = User(**data)
    except ValidationError as e:
        error = e.errors()[0]["msg"]
        return jsonify({"success": False, "error": error}), 422
    
    check = FindUserByEmail(data['email'])
    if check:
        return jsonify({"success": False, "error": "User Already exists"}), 403
    
    try:
        user = createUser(data['name'], data['email'], data['password'], data['phone'])
        user["_id"] = str(user["_id"])
        user.pop("password", None)
    except Exception as e:
        return jsonify({"success": False, "error": "Could not create user", "details": str(e)}), 500
    
    token = create_jwt(user["_id"])

    response = make_response(jsonify({
        "success": True,
        "message": "User created successfully!",
        "data": user
    }), 201)

    response.set_cookie(
        "authToken",
        token,
        httponly=True,
        samesite="Strict",
        secure=True
    )
    return response

# ---------------------- SIGNIN ---------------------- #
@auth_bp.route("/signin", methods=["POST"])
def signin():
    data = request.get_json()
    print(SECRET_KEY)
    if not data:
        return jsonify({"success": False, "error": "No data provided"}), 400
    
    user = Login(data['identifier'], data['password'])
    if not user:
        return jsonify({"success": False, "error": "Wrong Credentials"}), 403
    
    user["_id"] = str(user["_id"])
    user.pop("password", None)

    token = create_jwt(user["_id"])

    response = make_response(jsonify({
        "success": True,
        "message": "User signed in successfully!",
        "data": user
    }), 200)

    response.set_cookie(
        "authToken",
        token,
        httponly=True,
        samesite="Strict",
        secure=True
    )
    return response

# ---------------------- SIGNOUT ---------------------- #
@auth_bp.route("/signout", methods=["POST"])
def signout():
    response = make_response(jsonify({
        "success": True,
        "message": "User signed out successfully!"
    }), 200)
    response.set_cookie("authToken", "", expires=0, httponly=True, samesite="Strict", secure=True)
    return response

# ---------------------- VERIFY ---------------------- #
@auth_bp.route("/verify", methods=["GET"])
def verify():
    authToken = request.cookies.get("authToken")
    if not authToken:
        return jsonify({"success": False, "error": "Unauthorized"}), 401
    
    decoded = verify_jwt(authToken)

    if not decoded:
        return jsonify({"success": False, "error": "Unauthorized"}), 401

    user = FindUserById(decoded["user_id"])
    print(decoded["user_id"])
    if not user:
        return jsonify({"success": False, "error": "Unauthorized"}), 401

    user["_id"] = str(user["_id"])
    user.pop("password", None)

    return jsonify({
        "success": True,
        "message": "User verified successfully!",
        "data": user
    }), 200
