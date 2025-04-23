import bcrypt
from flask_jwt_extended import create_access_token
from datetime import timedelta

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# Keep only this version of generate_token using Flask-JWT-Extended
def generate_token(identity, expires_in=24):
    return create_access_token(identity=identity, expires_delta=timedelta(hours=expires_in))
