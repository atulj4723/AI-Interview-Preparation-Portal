from flask import Blueprint, request, jsonify
from service.conversation import createConversation,getConversation
con_bp = Blueprint('conversation', __name__)
@con_bp.route("/conversation", methods=["POST"])
def create_conversation():
    data = request.get_json()
    if not data:
        return jsonify({
            "success": False,
            "error": "No data provided"
        }), 400
    try:
        user_id = data['user_id']
        interview_id = data['interview_id']
        conversations = data['conversations']
        response = createConversation(conversations, user_id, interview_id)
        return jsonify({
            "success": True,
            "data": response
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Could not create conversation",
            "details": str(e)
        }), 500
@con_bp.route("/conversation", methods=["GET"])
def get_conversation():
    user_id = request.args.get('user_id')
    interview_id = request.args.get('interview_id')
    if not user_id or not interview_id:
        return jsonify({
            "success": False,
            "error": "user_id and interview_id are required"
        }), 400
    try:
        response = getConversation(user_id, interview_id)
        return jsonify({
            "success": True,
            "data": response
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Could not fetch conversation",
            "details": str(e)
        }), 500