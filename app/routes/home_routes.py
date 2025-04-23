from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')  # Make sure this file exists in your templates folder
