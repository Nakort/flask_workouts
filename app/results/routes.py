from flask import Blueprint, jsonify

results = Blueprint("results", __name__)

@results.route("/")
def index():
    return jsonify(id=str(1))
