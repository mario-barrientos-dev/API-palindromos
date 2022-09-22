from flask import Blueprint, jsonify
welcome = Blueprint("welcome", __name__)

@welcome.route('/')
def ping():
    return jsonify({"message": "Bienvenido"})
