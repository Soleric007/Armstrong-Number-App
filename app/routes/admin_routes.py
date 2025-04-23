from flask import Blueprint, jsonify
from app.models import User, Feedback

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/users', methods=['GET'])
def all_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'username': u.username} for u in users])

@admin_bp.route('/admin/feedbacks', methods=['GET'])
def all_feedbacks():
    feedbacks = Feedback.query.all()
    return jsonify([{'name': f.name, 'email': f.email, 'message': f.message} for f in feedbacks])
