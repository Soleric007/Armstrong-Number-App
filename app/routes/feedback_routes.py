from flask import Blueprint, request, jsonify
from app.models import Feedback
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

feedback_bp = Blueprint('feedback_bp', __name__)

@feedback_bp.route('/', methods=['POST'])
@jwt_required()  # Ensure the user is authenticated
def submit_feedback():
    data = request.get_json()

    # Get the current user's ID (from the JWT token)
    user_id = get_jwt_identity()

    # Create a new Feedback object with name, email, message, and user_id
    new_feedback = Feedback(
        name=data.get('name'),
        email=data.get('email'),
        message=data.get('message'),
        user_id=user_id  # Link the feedback to the logged-in user
    )

    db.session.add(new_feedback)
    db.session.commit()

    return jsonify({'message': 'Feedback submitted successfully'}), 201
