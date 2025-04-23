from flask import Blueprint, request, jsonify
from app.models import Feedback
from app import db

feedback_bp = Blueprint('feedback_bp', __name__)

@feedback_bp.route('/', methods=['POST'])
def submit_feedback():
    data = request.get_json()

    new_feedback = Feedback(
        name=data.get('name'),
        email=data.get('email'),
        message=data.get('message')
    )

    db.session.add(new_feedback)
    db.session.commit()

    return jsonify({'message': 'Feedback submitted successfully'}), 201
