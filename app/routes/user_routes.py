from flask import Blueprint, request, jsonify
from app.models import db, Feedback
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    # Assuming you track stats in User model
    user = User.query.get(user_id)
    return jsonify({
        'username': user.username,
        'games_played': user.games_played,
        'best_score': user.best_score,
        'total_wins': user.total_wins
    })

@user_bp.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    feedback = Feedback(name=data['name'], email=data['email'], message=data['message'])
    db.session.add(feedback)
    db.session.commit()
    return jsonify({'message': 'Feedback submitted successfully'})
