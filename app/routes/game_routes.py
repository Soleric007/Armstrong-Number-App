from flask import Blueprint, request, jsonify
from app.utils.armstrong import is_armstrong, find_armstrong_in_range

game_bp = Blueprint('game', __name__)

@game_bp.route('/check', methods=['POST'])
def check_armstrong():
    number = int(request.json.get('number'))
    result = is_armstrong(number)
    return jsonify({'number': number, 'is_armstrong': result})

@game_bp.route('/range', methods=['POST'])
def armstrong_range():
    start = int(request.json.get('start'))
    end = int(request.json.get('end'))
    results = find_armstrong_in_range(start, end)
    return jsonify({'range': [start, end], 'armstrong_numbers': results})
