from flask import Blueprint, request, jsonify
from app.models import db, User
from app.utils.helpers import hash_password, verify_password, generate_token
from app.utils.validators import is_valid_email, is_strong_password

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    
    # Get required fields from the data
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    email = data.get('email')
    
    # Create the new user instance
    user = User(username=username, name=name, email=email)
    user.set_password(password)  # Set the hashed password
    
    # Add the user to the database
    db.session.add(user)
    db.session.commit()

    # Generate the token after user is created
    # Generate JWT token for the user

    return jsonify({
        'message': 'Registration successful'  # Return the token as part of the response
    }), 201
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and verify_password(password, user.password_hash):
        token = generate_token(user.id)
        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        }), 200

    return jsonify({'message': 'Invalid credentials'}), 401
