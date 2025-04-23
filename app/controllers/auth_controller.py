from flask import request, jsonify
from app.models import User, db
from flask_jwt_extended import create_access_token
from datetime import timedelta

def register_user():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    contact = data.get('contact')
    username = data.get('username')
    password = data.get('password')

    if User.query.filter((User.email == email) | (User.username == username)).first():
        return jsonify({'message': 'User with this email or username already exists'}), 400

    user = User(
        name=name,
        email=email,
        contact=contact,
        username=username,
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Registration successful'}), 201


def login_user():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=1))
    return jsonify({
        'message': 'Login successful',
        'access_token': access_token,
        'user': {
            'id': user.id,
            'username': user.username,
            'name': user.name
        }
    }), 200
