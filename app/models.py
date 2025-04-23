from datetime import datetime
from app import db
from app.utils.helpers import hash_password, verify_password
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)

    address = db.relationship('Address', backref='user', uselist=False)
    attempts = db.relationship('Attempt', backref='user', lazy=True)
    feedbacks = db.relationship('Feedback', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = hash_password(password)
    
    def check_password(self, password):
        return verify_password(password, self.password_hash)

class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    zip_code = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Attempt(db.Model):
    __tablename__ = 'attempts'

    id = db.Column(db.Integer, primary_key=True)
    input_type = db.Column(db.String(10))  # 'single' or 'range'
    input_value = db.Column(db.String(50))
    result = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
class Feedback(db.Model):
    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)  # Add name
    email = db.Column(db.String(120), nullable=False)  # Add email
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Corrected foreign key reference to users

    user = db.relationship('User', backref='feedbacks', lazy=True)

    def __init__(self, name, email, message, user_id):
        self.name = name
        self.email = email
        self.message = message
        self.user_id = user_id
