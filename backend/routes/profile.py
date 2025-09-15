from flask import Blueprint, request, jsonify
from pypdf import PdfReader
from service.profile import getProfile, createProfile,updateProfile
import json
from service.ai import convertTextToJSON
profile_bp = Blueprint('profile', __name__)
@profile_bp.route("/profile/<user_id>", methods=["GET"])
def get_profile(user_id):
    user = getProfile(user_id)
    if not user:
        return jsonify({
            "success": False,
            "error": "Profile not found"
        }), 404
    if "_id" in user:
        user["_id"] = str(user["_id"])
    return jsonify({
        "success": True,
        "data": user
    }), 200

@profile_bp.route("/profile", methods=["POST"])
def create_profile():
    file = request.files["file"]
    data = request.form.to_dict()
    if file.filename == "":
        return jsonify({
            "success": False,
            "error": "No selected file"
        }), 400
    if not data or 'user_id' not in data :
        return jsonify({
            "success": False,
            "error": "user_id and resume are required"
        }), 400
    try:
        reader = PdfReader(file)
        extracted_text = ""
        for page in reader.pages:
            extracted_text += page.extract_text() or ""
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Failed to read PDF file",
            "details": str(e)
        }), 500
    ai=convertTextToJSON(extracted_text)
    resume=json.loads(ai.text)
    try:
        profile = createProfile(data['user_id'], resume)
        if "_id" in profile:
            profile["_id"] = str(profile["_id"])
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Could not create profile in database",
            "details": str(e)
        }), 500
    return jsonify({
        "success": True,
        "message": "Profile created successfully!",
        "data": profile
    }), 201

@profile_bp.route("/profile", methods=["PUT"])
def update_profile():
    file = request.files["file"]
    data = request.form.to_dict()

    if file.filename == "":
        return jsonify({
            "success": False,
            "error": "No selected file"
        }), 400
    if not data or 'user_id' not in data :
        return jsonify({
            "success": False,
            "error": "user_id and resume are required"
        }), 400
    
    try:
        reader = PdfReader(file)
        extracted_text = ""
        for page in reader.pages:
            extracted_text += page.extract_text() or ""

    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Failed to read PDF file",
            "details": str(e)
        }), 500
    ai=convertTextToJSON(extracted_text)
    resume=json.loads(ai.text)
    try:
        profile = updateProfile(data['user_id'], resume)
        if "_id" in profile:
            profile["_id"] = str(profile["_id"])
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Could not update profile in database",
            "details": str(e)
        }), 500
    return jsonify({
        "success": True,
        "message": "Profile updated successfully!",
        "data": profile
    }), 201