from flask import Blueprint, jsonify

workouts = Blueprint("workouts", __name__)

@workouts.route("/")
def index():
    return jsonify(id=str(1))
