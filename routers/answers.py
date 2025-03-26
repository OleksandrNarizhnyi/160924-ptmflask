from flask import Blueprint, request

answers_bp = Blueprint(name='answers', import_name=__name__)

@answers_bp.route('', methods=["GET", "POST"])
def get_answers():
    if request.method == "GET":
        return "ALL ANSWERS"

    if request.method == "POST":
        return "CREATE ANSWER"

@answers_bp.route('<int:id>', methods=["GET"])
def retrieve_answer(id):
    return f"ANSWER {id}"
